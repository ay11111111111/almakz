from django.urls import path, include
from . import views


urlpatterns = [
    path('news', views.NewsView.as_view()),
    path('portfolio', views.PortfolioView.as_view()),
]
