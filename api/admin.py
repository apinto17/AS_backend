from django.contrib import admin
from .models import CrawledData, Projects, Categories

admin.site.register(CrawledData)
admin.site.register(Projects)
admin.site.register(Categories) 