# api/management/commands/userseed.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Cria os grupos e usuários de teste (Admin, Gerentes, Operadores).'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE(
            '--- Iniciando script de criação de usuários e grupos ---'
        ))

        # 1. Criar os Grupos
        grupo_gerentes, created = Group.objects.get_or_create(name='Gerentes')
        if created:
            self.stdout.write(self.style.SUCCESS("Grupo 'Gerentes' CRIADO."))
        else:
            self.stdout.write("Grupo 'Gerentes' já existe.")

        grupo_operadores, created = Group.objects.get_or_create(name='Operadores')
        if created:
            self.stdout.write(self.style.SUCCESS("Grupo 'Operadores' CRIADO."))
        else:
            self.stdout.write("Grupo 'Operadores' já existe.")

        self.stdout.write(self.style.NOTICE('\n--- Criando usuários ---'))

        # 2. Criar SuperUsuário 'admin'
        try:
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS("Superusuário 'admin' CRIADO com senha 'admin123'."))

        except IntegrityError:
            self.stdout.write("Superusuário 'admin' já existe.")
            admin_user = User.objects.get(username='admin')

        # 3. Criar Usuário 'gerente'
        try:
            gerente = User.objects.create_user(
                username='gerente', 
                password='senha123', 
                first_name='Gerente de Teste'
            )
            gerente.groups.add(grupo_gerentes)
            self.stdout.write(self.style.SUCCESS("Usuário 'gerente' CRIADO e adicionado ao grupo 'Gerentes'."))

        except IntegrityError:
            self.stdout.write("Usuário 'gerente' já existe, garantindo grupo...")
            gerente = User.objects.get(username='gerente')
            if not gerente.groups.filter(name='Gerentes').exists():
                gerente.groups.add(grupo_gerentes)

        # 4. Criar Usuário 'operador'
        try:
            operador = User.objects.create_user(
                username='operador', 
                password='senha123', 
                first_name='Operador de Teste'
            )
            operador.groups.add(grupo_operadores)
            self.stdout.write(self.style.SUCCESS("Usuário 'operador' CRIADO e adicionado ao grupo 'Operadores'."))

        except IntegrityError:
            self.stdout.write("Usuário 'operador' já existe, garantindo grupo...")
            operador = User.objects.get(username='operador')
            if not operador.groups.filter(name='Operadores').exists():
                operador.groups.add(grupo_operadores)

        self.stdout.write(self.style.SUCCESS('\n--- Script Concluído ---'))