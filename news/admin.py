from django.contrib import admin
from .models import newsArticoliModels, newsGiornalistiModels
# Register your models here.

admin.site.register(newsArticoliModels)
admin.site.register(newsGiornalistiModels)
