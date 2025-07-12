
from rest_framework import  serializers

from employee.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        # fields = '__all__'
        exclude = ["password"]

    pass

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm password")

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        employee= Employee.objects.create_user(**validated_data)  # 自动哈希密码
        return employee