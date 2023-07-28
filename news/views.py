from rest_framework import generics
from rest_framework.permissions import AllowAny

from news.models import News
from news.serializers import NewsSerializer


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
