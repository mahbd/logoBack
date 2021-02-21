from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('site-data', views.SiteDataViewSet, 'site-data')
router.register('works', views.WorkDataViewSet, 'works')

urlpatterns = [
    path('', include(router.urls)),
]
