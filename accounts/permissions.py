from rest_framework import permissions


# 自定义用户的权限


class AccoutsPermissions(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        method = request.method
        # 查询和增加用户，所有人都可以
        if method in permissions.SAFE_METHODS or method == "POST":
            return True
        # 只有管理员能删除
        if method == "DELETE" and request.user.is_staff == 1:
            return True
        # 每个用户只能修改自己的信息
        if request.user.id == obj.id:
            return True
        return False
