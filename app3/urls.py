from django.urls import path
from app3.views import *
app_name='anything'
urlpatterns=[
    path('test3/',test3,name='test3'),
    path('US/',US,name='US'),
]