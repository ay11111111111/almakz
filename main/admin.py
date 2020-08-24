from django.contrib import admin
from .models import New, Portfolio

class NewsAdmin(admin.ModelAdmin):
    list_display = ['header','text','date_published']

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(New, NewsAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
