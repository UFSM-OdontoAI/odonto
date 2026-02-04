from django.urls import path
from . import views
from .views_image import serve_image

urlpatterns = [
    path('<str:split>/', views.image_list, name='image_list'),
    path('<str:split>/<int:image_id>/', views.image_detail, name='image_detail'),

    # 🔧 ESTA LINHA É A FALTANTE
    path('image/<str:split>/<str:filename>/', serve_image, name='serve_image'),
]

