from django.urls import path
from app2.views import *
app_name='anything'
urlpatterns=[
    path('test2/',test2,name='test2'),
    path('Aus/',Aus,name='Aus'),
]
