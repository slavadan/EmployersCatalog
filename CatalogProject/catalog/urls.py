from django.urls import path
from .views import AllEmployeeViewSet
from rest_framework.routers import DefaultRouter


app_name = 'catalog'
router = DefaultRouter()
router.register(r'employers/all', AllEmployeeViewSet)

urlpatterns = router.urls


