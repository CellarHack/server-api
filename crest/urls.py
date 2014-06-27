from django.conf.urls import patterns, include, url

from rest_framework import routers

from views import MetricViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r'metric', MetricViewSet)
router.register(r'event', EventViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
