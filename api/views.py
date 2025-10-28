from rest_framework import viewsets, permissions
from .serializers import UserSerializer, OrdemProducaoSerializer
from django.contrib.auth.models import User
from .models import OrdemProducao

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return User.objects.order_by('id')
        return User.objects.filter(pk=user.pk)
    
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.owner == request.user
    
class OrdemProducaoViewSet(viewsets.ModelViewSet):
    serializer_class = OrdemProducaoSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Gerentes').exists():
            
            return OrdemProducao.objects.all().order_by('-criado_em')

        return OrdemProducao.objects.filter(owner=user).order_by('-criado_em')

    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)