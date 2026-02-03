from django.urls import path
from . import views
from .views_image import serve_image

urlpatterns = [
 path('<str:split>/', views.image_list),
 path('<str:split>/<int:image_id>/', views.image_detail),
 path('image/<str:split>/<str:filename>/', serve_image),
]
