from django.urls import include, path
from rest_framework import routers
from . import views
from api.api.Login import LoginAPI
from api.api.SignUp import SignUpAPI
from api.api.Assembly import AssemblyList, AssemblyDetail
from api.api.CrawledData import CrawledDataDetail

from rest_framework.urlpatterns import format_suffix_patterns



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('item/search', views.search_item),
    path('user/login', LoginAPI.as_view()),
    path('user/signup', SignUpAPI.as_view()),
    path('assembly/', AssemblyList.as_view()),
    path('assembly/<int:pk>/', AssemblyDetail.as_view()),
    path('item/<int:pk>/', CrawledDataDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)