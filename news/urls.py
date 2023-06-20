from django.urls import include, path
from rest_framework import routers
from. import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ptt', views.PttViewSet)
router.register(r'diary', views.DiaryViewSet)
router.register(r'text', views.TextViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]