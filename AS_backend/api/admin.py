from django.contrib import admin
from .models import Item, User, Assembly

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Assembly)