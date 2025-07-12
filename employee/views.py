from rest_framework.decorators import action
from rest_framework import viewsets, generics,status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import EmployeeSerializer, RegisterSerializer



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get_permissions(self):
        if self.action == "create":
            # 创建用户（POST /employee/）：允许匿名访问
            return [IsAdminUser()]
        elif self.action in ["update", "partial_update", "destroy", "list"]:
            return [IsAdminUser()]
        elif self.action == "retrieve":
            return [IsAuthenticated()]
        return super().get_permissions()
    @action(detail=False, methods=["post"], url_path="register", permission_classes=[AllowAny])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()
            return Response({"message": "注册成功", "username": employee.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()
    serializer_class = RegisterSerializer