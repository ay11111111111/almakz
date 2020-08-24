from ..models import New, Portfolio
from .serializers import *
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, ListAPIView
from drf_yasg import openapi


class NewsView(ListAPIView):
    serializer_class = NewSerializer
    queryset = New.objects.all()


class PortfolioView(ListAPIView):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()
