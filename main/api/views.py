from ..models import New, Portfolio
from .serializers import *
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, ListAPIView
from drf_yasg import openapi
from rest_framework.response import Response


# class NewsView(ListAPIView):
#     serializer_class = NewSerializer(many=True, context={"request": request})
#     queryset = New.objects.all()
#
#
# class PortfolioView(ListAPIView):
#     serializer_class = PortfolioSerializer
#     queryset = Portfolio.objects.all()

@swagger_auto_schema(method='get', operation_description="GET list of news")
@api_view(['GET'])
def news_list(request):
    news = New.objects.all()
    serializer = NewSerializer(news, many=True, context={"request": request})
    return Response(serializer.data)


@swagger_auto_schema(method='get', operation_description="GET list of news")
@api_view(['GET'])
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolios, many=True, context={"request": request})
    return Response(serializer.data)
