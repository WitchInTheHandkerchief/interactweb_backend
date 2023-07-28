from django.urls import path

from news import views

urlpatterns = [
    path("list_news/", views.NewsAPIView.as_view())
]
