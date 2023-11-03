from rest_framework import serializers
from .models import CustomUser

# 序列化账户模型


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    
    # 元数据
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name']

