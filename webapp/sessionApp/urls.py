from django.urls import path
from .import views
urlpatterns=[
    path('',views.sessionExample),
    path('first/',views.storeData)
]