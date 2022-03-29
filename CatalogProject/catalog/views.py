from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer, CustomUserSerializer
from .mypermissions import IsStaff
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('level', )
    permission_classes = (IsStaff, )


# Create your views here.
class PersonalView(APIView):

    def get(self, request, format=None):
        user = request.user
        if user.id is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
