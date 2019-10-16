from django.urls import path, re_path
from rest_framework import routers
from .api import LeadViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads') #路由为   ；视图函数；命名
urlpatterns = router.urls
