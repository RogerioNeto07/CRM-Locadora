from rest_framework import permissions

class IsDonoDaEmpresa(permissions.BasePermission):
    """
    Permissão personalizada para permitir acesso apenas ao dono da empresa.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser