from django.urls import path, include
from . import views


urlpatterns = [
    path('news', views.news_list),
    path('portfolio', views.portfolio_list),
]
