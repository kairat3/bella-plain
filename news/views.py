from rest_framework import generics
from news import serializers
from news.models import News


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsRetrieveApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
