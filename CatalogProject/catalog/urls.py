from django.urls import path
from .views import EmployeeViewSet, PersonalView
from rest_framework.routers import DefaultRouter


app_name = 'catalog'
router = DefaultRouter()
router.register(r'employers/all', EmployeeViewSet)

urlpatterns = [
    path('personal/', PersonalView.as_view())
]

urlpatterns += router.urls


