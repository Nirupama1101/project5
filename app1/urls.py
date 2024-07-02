from django.urls import path
from app1.views import *
app_name='anything'
urlpatterns=[
    path('test1/',test1,name='test1'),
    path('India/',India,name='India'),
]