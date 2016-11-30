from django.contrib import admin
from app.models import Scrape
# Register your models here.


    
class ScrapeModel(admin.ModelAdmin):
    model=Scrape
admin.site.register(Scrape,ScrapeModel)
