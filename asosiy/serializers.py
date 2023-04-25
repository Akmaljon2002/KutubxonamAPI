from rest_framework import serializers
from .models import *

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class AudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audios
        fields = '__all__'