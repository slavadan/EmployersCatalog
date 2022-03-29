from django.urls import path
from .views import EmployeeViewSet, PersonalView, OneLevelEmployeeViewSet
from rest_framework.routers import DefaultRouter


app_name = 'catalog'
router = DefaultRouter()
router.register(r'employers/all', EmployeeViewSet)

urlpatterns = [
    path('personal/', PersonalView.as_view()),
    path(
        'employers/<int:level>/',
        OneLevelEmployeeViewSet.as_view({'get': 'list'})
    ),
]

urlpatterns += router.urls


