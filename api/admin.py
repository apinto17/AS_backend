from django.contrib import admin
from .models import CrawledData, Assembly, Categories

admin.site.register(CrawledData)
admin.site.register(Assembly)
admin.site.register(Categories) 