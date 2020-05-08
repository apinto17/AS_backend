from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('item/', views.get_item_by_category),
    path('item/search', views.search_item),
    path('user/login', views.login),
    path('user/signup', views.sign_up),
    path('project', views.save_project),
]