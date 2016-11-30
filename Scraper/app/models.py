"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Scrape(models.Model):
        ActivityName=models.CharField("ActivityName",max_length=100,null=False, unique=True, blank=True)
        Email=models.CharField(max_length=50,null=True,unique=False, blank=True)
        Website=models.URLField(null=True,blank=True)
        Phone=models.CharField(max_length=50,null=True,unique=False, blank=True)
        Province=models.CharField("Province",max_length=10,null=False, blank=True)
        City=models.CharField("City",max_length=100,null=False, blank=True)
        Category=models.TextField("Category", unique=False, null=False, blank=True)
        Description=models.TextField("Description", unique=False, null=False, blank=True)
       
        def __str__(self):
            return (self.ActivityName)
