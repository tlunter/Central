from django.db import models
from django.utils.encoding import smart_str
from django.utils.hashcompat import md5_constructor, sha_constructor
from django.utils.crypto import constant_time_compare
from app.auth.models import User, Group

def get_hexdigest(algorithm, salt, raw_password):
    """
    Returns a string of the hexdigest of the given plaintext password and salt
    using the given algorithm ('md5', 'sha1' or 'crypt').
    """
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'crypt':
        try:
            import crypt
        except ImportError:
            raise ValueError('"crypt" password algorithm not supported in this environment')
        return crypt.crypt(raw_password, salt)

    if algorithm == 'md5':
        return md5_constructor(salt + raw_password).hexdigest()
    elif algorithm == 'sha1':
        return sha_constructor(salt + raw_password).hexdigest()
    raise ValueError("Got unknown password algorithm type in password.")

def check_password(raw_password, enc_password):
    """
    Returns a boolean of whether the raw_password was correct. Handles
    encryption formats behind the scenes.
    """
    algo, salt, hsh = enc_password.split('$')
    return constant_time_compare(hsh, get_hexdigest(algo, salt, raw_password))

class ChannelManager(models.Manager):
    def create_channel(self, name, password=None, operators=None):

        channel = self.model(name=name)

        channel.set_password(password)
        channel.save(using=self._db)

        if isinstance(operators, basestring):
            try:
                group = Group.objects.get(name=operators)
            except Group.DoesNotExist:
                pass
            else:
                channel.operators.add(group)
        elif isinstance(operators, Group):
            channel.operators.add(operators)
        elif hasattr(operators, '__iter__') and hasattr(operators, '__len__'):
            for operator_group in operators:
                if isinstance(operator_group, str):
                    try:
                        group = Group.objects.get(name=operator_group)
                    except Group.DoesNotExist:
                        pass
                    else:
                        channel.operators.add(group)
                elif isinstance(operator_group, Group):
                    channel.operators.add(operator_group)

        return channel

    def get_by_natural_key(self, name):
        return self.get(name=name)

class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    operators = models.ManyToManyField(Group, related_name='operators', blank=True)
    active_users = models.ManyToManyField(User, related_name='active_users', blank=True)
    password = models.CharField(max_length=128, blank=True)
    objects = ChannelManager()

    def natural_key(self):
        return self.name

    def set_password(self, raw_password):
        if raw_password is not None:
            import random
            algo = 'sha1'
            salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
            hsh = get_hexdigest(algo, salt, raw_password)
            self.password = '%s$%s$%s' % (algo, salt, hsh)

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        encryption formats behind the scenes.
        """
        # Backwards-compatibility check. Older passwords won't include the
        # algorithm or salt.
        if self.password == '' or self.password == None:
            return True

        if '$' not in self.password:
            is_correct = (self.password == get_hexdigest('md5', '', raw_password))
            if is_correct:
                # Convert the password to the new, more secure format.
                self.set_password(raw_password)
                self.save()
            return is_correct
        return check_password(raw_password, self.password)

    def set_active(self, user):
        if user is None:
            raise User.DoesNotExist

        self.active_users.add(user)

    def set_inactive(self, user):
        if user is None:
            raise User.DoesNotExist

        self.active_users.remove(user)

class MessageManager(models.Manager):
    def create_message(self, user, message, channel):
        try:
            channel_obj = Channel.objects.get(name = channel)
        except Channel.DoesNotExist:
            return None

        message_obj = self.model(user = user, message = message, channel = channel_obj)
        message_obj.save()

        return message_obj

class Message(models.Model):
    user = models.ForeignKey(User)
    time_created = models.DateTimeField(auto_now_add=True)
    time_editted = models.DateTimeField(auto_now=True)
    message = models.TextField()
    channel = models.ForeignKey(Channel)
    objects = MessageManager()
