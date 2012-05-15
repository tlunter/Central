from django.test import TestCase
from django.db import IntegrityError
from app.accounts.models import Group
from app.channels.models import Channel

class ChannelPassCreationTest(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.name = "Test Channel"
		cls.password = "testpassword"
		cls.channel = Channel.objects.create_channel(cls.name, cls.password)

	def test_check_true_password(self):
		self.assertTrue(self.channel.check_password(self.password))

	def test_check_false_password(self):
		self.assertFalse(self.channel.check_password(self.password + '1'))

	def test_unique_name(self):
		with self.assertRaises(IntegrityError):
			Channel.objects.create_channel(self.name, self.password)

class ChannelNoPassCreationTest(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.name = "Test Passwordless"
		cls.password = None
		cls.channel = Channel.objects.create_channel(cls.name,cls.password)

	def test_check_true_password(self):
		self.assertTrue(self.channel.check_password(self.password))

	def test_check_false_password(self):
		self.assertTrue(self.channel.check_password(str(self.password) + '1'))

	def test_unique_name(self):
		with self.assertRaises(IntegrityError):
			Channel.objects.create_channel(self.name, self.password)

class ChannelGroupAddingTest(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.name = "Group Channel"
		cls.group_name = "Group"
		cls.group = Group.objects.create(name=cls.group_name)
		cls.group2_name = "Group 2"
		cls.group2 = Group.objects.create(name=cls.group2_name)

	def tearDown(self):
		channel = Channel.objects.get(name=self.name)
		channel.delete()

	def test_group_add_string(self):
		channel = Channel.objects.create_channel(self.name, operators=self.group_name)

		self.assertEqual(channel.name, self.name)

		# Need to convert to list from a QuerySet
		self.assertEqual(list(channel.operators.all()),[self.group])

	def test_group_add_group(self):
		channel = Channel.objects.create_channel(self.name, operators=self.group)

		self.assertEqual(channel.name, self.name)

		# Need to convert to list from a QuerySet
		self.assertEqual(list(channel.operators.all()),[self.group])

	def test_group_add_list_of_string(self):
		channel = Channel.objects.create_channel(self.name, operators=[self.group_name, self.group2_name])

		self.assertEqual(channel.name, self.name)

		# Need to convert to list from a QuerySet

	def test_group_add_list_of_group(self):
		channel = Channel.objects.create_channel(self.name, operators=[self.group, self.group2])

		self.assertEqual(channel.name, self.name)

		# Need to convert to list from a QuerySet
		self.assertEqual(list(channel.operators.all()),[self.group,self.group2])