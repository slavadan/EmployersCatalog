from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from .mypermissions import IsStaff


# Create your views here.
class AllEmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsStaff,)


# Create your views here.
# class EmployeeWithEqLevel(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = (IsStaff, )
