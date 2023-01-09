from django.urls import path
from app2.views import *

app_name=('madhu')

urlpatterns=[

    path('slogan/',slogan,name='slogan'),
]