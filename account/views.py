from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from django.contrib.auth.models import Permission, Group
from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([])
def session_status(request):
    if request.user.is_authenticated:
        return Response({'logged_in': True})
    return Response({'logged_in': False}, status=401)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"detail": "Logout successful."})

class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    只读权限列表和详情接口
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAdminUser]  # 只有管理员可以访问

class ContentTypeSerializer(ModelSerializer):
    class Meta:
        model = ContentType
        fields = "__all__"

class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]