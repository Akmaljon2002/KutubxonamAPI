from django.shortcuts import render
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics


class AudiosViewSet(generics.ListAPIView):
    queryset = Audios.objects.all()
    serializer_class = AudiosSerializer

class AudioDetailAPIView(generics.RetrieveAPIView):
    queryset = Audios.objects.all()
    serializer_class = AudiosSerializer

class TopicsAPIView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)