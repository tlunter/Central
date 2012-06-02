from django.utils.encoding import smart_unicode
from django.core.serializers.json import Serializer

class MySerializer(Serializer):
    def end_object(self, obj):
        self.objects.append(self._current)

        self._current = None

serializers = MySerializer()
