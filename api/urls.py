from django.urls import include, path
from rest_framework import routers
from . import views
from api.api.Login import LoginAPI
from api.api.SignUp import SignUpAPI


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('item/', views.get_item_by_category),
    path('item/search', views.search_item),
    path('user/login', LoginAPI.as_view()),
    path('user/signup', SignUpAPI.as_view()),
    path('project', views.save_project),
]