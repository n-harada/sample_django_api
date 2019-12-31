# mysns/post/urls.py
 
from django.contrib.auth import get_user_model
from django.urls import path

from . import views


from rest_framework import routers
from .views import GoodsAPIViewSet


router = routers.DefaultRouter()
router.register(r'good', GoodsAPIViewSet)
app_name = 'distribution'

urlpatterns = [
    path('api/goods/latest/', views.LatestGoodsAPIView.as_view()),
]
