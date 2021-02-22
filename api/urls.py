from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('site-data', views.SiteDataViewSet, 'site-data')
router.register('works', views.WorkDataViewSet, 'works')

urlpatterns = [
    path('subscribe/', csrf_exempt(views.NewsletterSubscriberView.as_view())),
    path('message/', csrf_exempt(views.MessageView.as_view())),
    path('', include(router.urls)),
]
