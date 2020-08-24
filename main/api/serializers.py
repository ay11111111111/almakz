from rest_framework import serializers
from ..models import New, Portfolio

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['header','text','date_published', 'img']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['name', 'description', 'img']
