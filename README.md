# 🏭 Sistema de Ordens de Produção - Django Backend

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/REST-API-02569B?style=for-the-badge&logo=django&logoColor=white" alt="REST API">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" alt="JWT">
</div>

<div align="center">
  <h3>🚀 API RESTful para gerenciamento de ordens de produção com Django REST Framework</h3>
  <p>
    <a href="#-características">Características</a> •
    <a href="#-instalação">Instalação</a> •
    <a href="#-uso">Uso</a> •
    <a href="#-api-endpoints">API</a> •
    <a href="#-postman">Postman</a> •
    <a href="#-contribuição">Contribuição</a>
  </p>
</div>

---

## 📋 Sobre o Projeto

Este é um **backend robusto** desenvolvido com **Django REST Framework** para **gerenciamento de ordens de produção**. O sistema oferece uma API RESTful completa para controle de usuários, ordens de produção e sistema de permissões granular.

### 🎯 Objetivo

Fornecer uma solução backend escalável e segura para **sistemas de gerenciamento de produção**, com autenticação JWT, controle de permissões por usuário e funcionalidades administrativas.

## ✨ Características

- 🔐 **Autenticação JWT** com `djangorestframework-simplejwt`
- 🛡️ **Sistema de permissões** com `django-guardian`  
- 👥 **Gerenciamento de usuários** com diferentes níveis de acesso
- 📋 **Ordens de produção** com controle de propriedade
- 📊 **API RESTful** completa com Django REST Framework
- 🗄️ **Banco de dados** SQLite (facilmente migrável para PostgreSQL/MySQL)
- 🔒 **Segurança** implementada com melhores práticas
- � **Collections Postman** prontas para uso
- 🧪 **Script de setup** automatizado para testes
- 🚀 **Pronto para produção** com configurações otimizadas

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.11+ | Linguagem principal |
| **Django** | 5.2.7 | Framework web |
| **Django REST Framework** | 3.15.2 | API REST |
| **SimpleJWT** | 5.3.0 | Autenticação JWT |
| **Django Guardian** | 2.4.0 | Permissões por objeto |
| **Django CORS Headers** | 4.3.1 | Configuração CORS |
| **Python Decouple** | 3.8 | Gerenciamento de configurações |
| **Pillow** | 10.1.0 | Processamento de imagens |
| **Coverage** | 7.3.2 | Cobertura de testes |
| **SQLite** | 3.x | Banco de dados (desenvolvimento) |

## 📦 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git

### 🚀 Método Rápido (Recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/metratonpr/petshop-django-backend.git
cd petshop-django-backend

# 2. Execute o script de setup automatizado
./setup_api_tests.sh
```

### 📝 Instalação Manual

#### 1. Clone o repositório

```bash
git clone https://github.com/metratonpr/petshop-django-backend.git
cd petshop-django-backend
```

#### 2. Crie um ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Configure o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

#### 6. Execute o servidor

```bash
python manage.py runserver
```

O servidor estará rodando em `http://127.0.0.1:8000/`

## 🚀 Uso

### 👤 Usuários de Teste Criados

O script de setup cria automaticamente usuários para teste:

| Usuário | Senha | Permissões |
|---------|-------|------------|
| `admin` | `admin123` | Superusuário - Acesso total |
| `manager` | `manager123` | Gerente - Vê todas as ordens |
| `testuser` | `test123` | Usuário comum - Vê apenas suas ordens |

### 🌐 Acessando a API

- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **API Root**: `http://127.0.0.1:8000/api/`
- **Token JWT**: `http://127.0.0.1:8000/api/token/`

### 🔐 Autenticação

O sistema utiliza **JWT (JSON Web Tokens)** para autenticação. Para acessar endpoints protegidos:

#### 1. **Obter token**:
```bash
POST /api/token/
Content-Type: application/json

{
    "username": "admin",
    "password": "admin123"
}
```

#### 2. **Resposta**:
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### 3. **Usar token** nas requisições:
```bash
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## 🔌 API Endpoints

### 🔐 **Autenticação**
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/token/` | Obter token de acesso JWT |
| `POST` | `/api/token/refresh/` | Renovar token JWT |

### 👥 **Usuários** `/api/users/`
| Método | Endpoint | Permissão | Descrição |
|--------|----------|-----------|-----------|
| `GET` | `/api/users/` | Autenticado | Lista usuários (admin: todos / user: próprio) |
| `GET` | `/api/users/{id}/` | Autenticado | Usuário específico |
| `POST` | `/api/users/` | Autenticado | Criar novo usuário |
| `PUT` | `/api/users/{id}/` | Autenticado | Atualizar usuário completo |
| `PATCH` | `/api/users/{id}/` | Autenticado | Atualizar usuário parcial |
| `DELETE` | `/api/users/{id}/` | Autenticado | Deletar usuário |

### 📋 **Ordens de Produção** `/api/ordens-producao/`
| Método | Endpoint | Permissão | Descrição |
|--------|----------|-----------|-----------|
| `GET` | `/api/ordens-producao/` | Autenticado | Lista ordens (gerente/admin: todas / user: próprias) |
| `GET` | `/api/ordens-producao/{id}/` | Autenticado | Ordem específica |
| `POST` | `/api/ordens-producao/` | Autenticado | Criar nova ordem |
| `PUT` | `/api/ordens-producao/{id}/` | Owner/Admin | Atualizar ordem completa |
| `PATCH` | `/api/ordens-producao/{id}/` | Owner/Admin | Atualizar ordem parcial |
| `DELETE` | `/api/ordens-producao/{id}/` | Owner/Admin | Deletar ordem |

### 🛡️ **Sistema de Permissões**

- **Usuários comuns**: Veem apenas seus próprios dados e ordens
- **Gerentes**: Grupo especial que pode ver todas as ordens de produção
- **Superusuários**: Acesso total ao sistema
- **Proprietários**: Podem editar/excluir apenas suas próprias ordens

## 📁 Estrutura do Projeto

```
petshop-django-backend/
├── 📁 core/                      # Configurações principais do Django
│   ├── settings.py               # Configurações do projeto
│   ├── urls.py                  # URLs principais
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
├── 📁 api/                       # App principal da API
│   ├── models.py                # Modelos: OrdemProducao
│   ├── views.py                 # ViewSets: UserViewSet, OrdemProducaoViewSet
│   ├── serializers.py           # Serializers DRF
│   ├── urls.py                  # URLs da API com routers
│   ├── admin.py                 # Configurações do Django Admin
│   └── migrations/              # Migrações do banco de dados
├── 📁 postman/                   # Collections e documentação Postman
│   ├── Petshop_Django_API.postman_collection.json
│   ├── Petshop_Development.postman_environment.json
│   └── API_Documentation.md
├── 📁 venv/                      # Ambiente virtual Python
├── manage.py                     # Script de gerenciamento Django
├── db.sqlite3                    # Banco de dados SQLite
├── requirements.txt              # Dependências do projeto
├── setup_api_tests.sh           # Script de setup automático
├── .gitignore                    # Arquivos ignorados pelo Git
└── README.md                     # Este arquivo
```

## 📡 Postman Collections

Este projeto inclui **collections Postman completas** para facilitar os testes da API:

### 📥 **Como importar**:

1. **Abra o Postman**
2. **Import** → **Upload Files**
3. **Selecione os arquivos**:
   - `postman/Petshop_Django_API.postman_collection.json`
   - `postman/Petshop_Development.postman_environment.json`

### ✨ **Recursos incluídos**:

- 🔄 **Auto-extração** de tokens JWT
- 🧪 **Testes automáticos** de validação
- 📊 **Variáveis de ambiente** configuradas
- 🎯 **Exemplos prontos** para todos os endpoints
- 🛡️ **Testes de permissões** incluídos

### 📚 **Documentação detalhada**:
Consulte o arquivo `postman/API_Documentation.md` para documentação completa da API.

## ⚙️ Configurações

### 🔧 **Configurações Atuais**

O projeto já está configurado com:

- ✅ **JWT Authentication** configurado
- ✅ **Django Guardian** para permissões por objeto  
- ✅ **CORS Headers** para requisições cross-origin
- ✅ **REST Framework** com paginação e filtros
- ✅ **Autenticação de sessão** como fallback

### 🌍 **Variáveis de Ambiente** *(recomendado para produção)*

Crie um arquivo `.env` na raiz do projeto:

```env
# Configurações de Segurança
DEBUG=False
SECRET_KEY=sua_chave_secreta_muito_segura_aqui

# Banco de Dados
DATABASE_URL=postgresql://user:password@localhost/dbname

# Hosts Permitidos
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com,localhost

# JWT Settings
JWT_SECRET_KEY=sua_chave_jwt_secreta

# CORS Settings
CORS_ALLOWED_ORIGINS=https://seu-frontend.com,http://localhost:3000
```

### 🚀 **Configurações de Produção**

Para deploy em produção, considere:

#### **Banco de Dados**:
- ✅ Migrar de SQLite para **PostgreSQL** ou **MySQL**
- ✅ Configurar backup automático
- ✅ Otimizar queries com índices

#### **Segurança**:
- ✅ Configurar `DEBUG=False`
- ✅ Definir `ALLOWED_HOSTS` apropriadamente
- ✅ Usar `HTTPS` obrigatório
- ✅ Configurar `CSRF` e `CORS` adequadamente

#### **Performance**:
- ✅ Configurar **Redis** para cache
- ✅ Usar **Nginx** + **Gunicorn**
- ✅ Implementar **CDN** para arquivos estáticos
- ✅ Configurar **monitoring** (Sentry, etc.)

#### **Infraestrutura**:
- ✅ **Docker** para containerização
- ✅ **CI/CD** pipeline
- ✅ **Load balancer** se necessário

## 🧪 Testes

### 🚀 **Setup Rápido para Testes**

Execute o script automatizado:
```bash
./setup_api_tests.sh
```

Este script irá:
- ✅ Instalar dependências
- ✅ Executar migrações
- ✅ Criar superusuário e usuários de teste
- ✅ Criar dados de exemplo
- ✅ Configurar grupos de permissões

### 🔬 **Testes Unitários**

```bash
# Executar todos os testes
python manage.py test

# Executar testes de um app específico
python manage.py test api

# Executar com verbosidade
python manage.py test --verbosity=2

# Executar testes específicos
python manage.py test api.tests.TestOrdemProducao
```

### 📊 **Cobertura de Testes**

```bash
# Executar com cobertura
coverage run --source='.' manage.py test

# Gerar relatório
coverage report

# Gerar relatório HTML
coverage html
```

### 🧪 **Testando com Postman**

1. **Importe as collections** (veja seção Postman)
2. **Execute os testes**:
   - Autenticação primeiro
   - CRUD de usuários
   - CRUD de ordens de produção
3. **Verifique permissões** com diferentes usuários

### 🔍 **Dados de Teste Criados**

O script cria automaticamente:
- **5 ordens de produção** de exemplo
- **3 usuários** com diferentes permissões
- **1 grupo** "Gerentes" configurado

## 📝 Desenvolvimento

### 🤝 **Contribuindo**

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. Abra um **Pull Request**

### 📋 **Padrões de Código**

- ✅ Seguir **PEP 8** para estilo de código Python
- ✅ Usar **type hints** quando possível
- ✅ Documentar funções e classes importantes
- ✅ Escrever **testes** para novas funcionalidades
- ✅ Usar **docstrings** em métodos públicos
- ✅ Manter **imports** organizados

### 🏗️ **Arquitetura do Projeto**

#### **Models** (`api/models.py`):
- `OrdemProducao`: Modelo principal com owner, produto, quantidade

#### **Views** (`api/views.py`):
- `UserViewSet`: CRUD para usuários com permissões
- `OrdemProducaoViewSet`: CRUD para ordens com filtro por owner

#### **Serializers** (`api/serializers.py`):
- `UserSerializer`: Serialização de usuários com grupos
- `OrdemProducaoSerializer`: Serialização de ordens com owner readonly

#### **Permissions**:
- `IsOwnerOrAdmin`: Permissão customizada para edição
- Integração com Django Guardian para permissões por objeto

### 🎯 **Roadmap**

Funcionalidades planejadas:
- [ ] **Websockets** para atualizações em tempo real
- [ ] **Filtros avançados** nas listagens
- [ ] **Upload de arquivos** nas ordens
- [ ] **Sistema de notificações**
- [ ] **Relatórios** de produção
- [ ] **API de estatísticas**
- [ ] **Autenticação social** (Google, GitHub)

### 🐛 **Reportar Bugs**

Ao reportar bugs, inclua:
- **Versão** do Python e Django
- **Passos** para reproduzir
- **Comportamento esperado** vs **atual**
- **Screenshots** se relevante
- **Logs** de erro

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **[@metratonpr](https://github.com/metratonpr)** - *Desenvolvedor Principal*

## 🤝 Contribuidores

Agradecimentos a todos que contribuíram para este projeto:

<!-- Adicione contribuidores aqui -->
- Você pode ser o próximo! 🚀

## 🆘 Suporte

Encontrou um problema? Tem uma sugestão? Precisa de ajuda?

### 📞 **Canais de Suporte**:
- 🐛 [**Reportar Bug**](https://github.com/metratonpr/petshop-django-backend/issues/new?labels=bug&template=bug_report.md)
- 💡 [**Sugerir Feature**](https://github.com/metratonpr/petshop-django-backend/issues/new?labels=enhancement&template=feature_request.md)
- 💬 [**Discussões**](https://github.com/metratonpr/petshop-django-backend/discussions)
- 📧 [**Email**](mailto:contato@exemplo.com)

### 📋 **Antes de Reportar**:
1. ✅ Verifique se já existe um issue similar
2. ✅ Use o template apropriado
3. ✅ Inclua informações detalhadas
4. ✅ Adicione logs de erro se houver

## 🙏 Agradecimentos

Especial agradecimento às seguintes tecnologias e projetos:

- **[Django](https://djangoproject.com/)** - Framework web robusto
- **[Django REST Framework](https://www.django-rest-framework.org/)** - Toolkit para APIs REST
- **[SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)** - Autenticação JWT
- **[Django Guardian](https://django-guardian.readthedocs.io/)** - Permissões por objeto
- **[Postman](https://www.postman.com/)** - Testes de API

## 📊 Estatísticas

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/metratonpr/petshop-django-backend)
![GitHub language count](https://img.shields.io/github/languages/count/metratonpr/petshop-django-backend)
![GitHub top language](https://img.shields.io/github/languages/top/metratonpr/petshop-django-backend)
![GitHub last commit](https://img.shields.io/github/last-commit/metratonpr/petshop-django-backend)

</div>

---

<div align="center">
  <p>⭐ **Se este projeto foi útil, considere dar uma estrela!** ⭐</p>
  <p>Feito com ❤️ e ☕ usando 🐍 **Python** + 🎸 **Django**</p>
  <p>
    <a href="#-sistema-de-ordens-de-produção---django-backend">⬆️ Voltar ao topo</a>
  </p>
</div>