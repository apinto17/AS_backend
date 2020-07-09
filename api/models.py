from django.db import models
import jsonfield
from django.contrib.auth.models import User


class Categories(models.Model):
    primary_category = models.TextField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    input_category = models.TextField(blank=True, null=True)
    output_category = models.TextField(blank=True, null=True)
    output_category_ui = models.TextField(db_column='output_category_UI', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CrawledData(models.Model):
    item_description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    item_specifications = jsonfield.JSONField(blank=True, null=True) 
    input_category = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=45, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    image_source = models.TextField(blank=True, null=True)
    txntime = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawled_data'



class Assembly(models.Model):
    user_id = models.CharField(max_length=45, blank=False, null=False)
    project_name = models.TextField(blank=True, null=True)
    items = jsonfield.JSONField(blank=False, null=False) 
    txntime = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


