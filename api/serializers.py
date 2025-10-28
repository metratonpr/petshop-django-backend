from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import OrdemProducao

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class OrdemProducaoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = OrdemProducao
        fields = ['id', 'owner', 'produto', 'quantidade', 'data_criacao']