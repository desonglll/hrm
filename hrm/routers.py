from rest_framework import routers

from account.views import PermissionViewSet, ContentTypeViewSet, GroupViewSet
from employee.views import EmployeeViewSet, RegisterView

router = routers.DefaultRouter()
router.register("employee", EmployeeViewSet)

router.register('contenttypes/contenttype',ContentTypeViewSet)
router.register('auth/permission', PermissionViewSet)
router.register('auth/group',GroupViewSet)
