from django.urls import path

from news import views

urlpatterns = [
    path("list_news/", views.NewsAPIView.as_view()),
    path("list_three_news/", views.ThreeLastNewsAPIView.as_view())
]
