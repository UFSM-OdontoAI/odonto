from django.urls import path,include
from viewer.views import home
urlpatterns = [
 path('',home),
 path('viewer/',include('viewer.urls')),
]
