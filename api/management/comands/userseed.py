from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Criando grupos e usuarios iniciais'

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
            self.stdout.write(self.style.SUCCESS("Superusuário 'admin' CRIADO com"+
                                                 " senha 'admin123'."))

        except IntegrityError:
            self.stdout.write("Superusuário 'admin' já existe.")
            admin_user = User.objects.get(username='admin')
