#!/bin/bash

# 🚀 Script de Setup para Testes da API Petshop Django

echo "🐾 Configurando ambiente para testes da API Petshop Django..."

# Verificar se o Django está instalado
if ! python -c "import django" &> /dev/null; then
    echo "❌ Django não encontrado. Instalando dependências..."
    pip install -r requirements.txt
fi

# Fazer migrações
echo "🔄 Executando migrações do banco de dados..."
python manage.py makemigrations
python manage.py migrate

# Verificar se já existe superusuário
echo "👤 Verificando superusuário..."
if python manage.py shell -c "from django.contrib.auth.models import User; exit(0 if User.objects.filter(is_superuser=True).exists() else 1)"; then
    echo "✅ Superusuário já existe!"
else
    echo "🔑 Criando superusuário padrão..."
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell
    echo "✅ Superusuário criado: admin / admin123"
fi

# Criar dados de exemplo
echo "📊 Criando dados de exemplo..."
python manage.py shell << EOF
from django.contrib.auth.models import User, Group
from api.models import OrdemProducao

# Criar grupo de gerentes se não existir
gerentes_group, created = Group.objects.get_or_create(name='Gerentes')
if created:
    print("✅ Grupo 'Gerentes' criado")

# Criar usuário de teste se não existir
test_user, created = User.objects.get_or_create(
    username='testuser',
    defaults={
        'email': 'test@example.com',
        'is_staff': False,
        'is_superuser': False
    }
)
if created:
    test_user.set_password('test123')
    test_user.save()
    print("✅ Usuário de teste criado: testuser / test123")

# Criar gerente de teste se não existir
manager_user, created = User.objects.get_or_create(
    username='manager',
    defaults={
        'email': 'manager@example.com',
        'is_staff': True,
        'is_superuser': False
    }
)
if created:
    manager_user.set_password('manager123')
    manager_user.groups.add(gerentes_group)
    manager_user.save()
    print("✅ Gerente criado: manager / manager123")

# Criar ordens de exemplo
admin_user = User.objects.get(username='admin')

ordens_exemplo = [
    {'produto': 'Ração Premium para Cães', 'quantidade': 50},
    {'produto': 'Ração para Gatos Filhotes', 'quantidade': 30},
    {'produto': 'Brinquedo para Cães', 'quantidade': 100},
    {'produto': 'Areia Sanitária', 'quantidade': 75},
    {'produto': 'Petisco Natural', 'quantidade': 200}
]

for ordem_data in ordens_exemplo:
    ordem, created = OrdemProducao.objects.get_or_create(
        produto=ordem_data['produto'],
        defaults={
            'quantidade': ordem_data['quantidade'],
            'owner': admin_user
        }
    )
    if created:
        print(f"✅ Ordem criada: {ordem_data['produto']}")

print(f"📊 Total de ordens: {OrdemProducao.objects.count()}")
print(f"👥 Total de usuários: {User.objects.count()}")
EOF

echo ""
echo "🎉 Setup concluído com sucesso!"
echo ""
echo "📋 Informações para testes:"
echo "   🔑 Admin: admin / admin123"
echo "   👤 Usuário: testuser / test123"
echo "   👨‍💼 Gerente: manager / manager123"
echo ""
echo "🚀 Para iniciar o servidor:"
echo "   python manage.py runserver"
echo ""
echo "📡 Endpoints disponíveis:"
echo "   🔐 POST /api/token/ (autenticação)"
echo "   👥 GET /api/users/ (usuários)"
echo "   📋 GET /api/ordens-producao/ (ordens)"
echo ""
echo "📁 Arquivos Postman criados em:"
echo "   📄 postman/Petshop_Django_API.postman_collection.json"
echo "   🌍 postman/Petshop_Development.postman_environment.json"
echo "   📚 postman/API_Documentation.md"
echo ""
echo "💡 Importe esses arquivos no Postman para testar a API!"