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
    #
    # def valitation_location(self, qiymat):
    #     if qiymat[:-4] != ".mp3":
    #         raise serializers.ValidationError("Faylni noto'g'ri kiritdingiz")
    #     return qiymat