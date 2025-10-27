# 🐾 Petshop Django Backend

<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/REST-API-02569B?style=for-the-badge&logo=django&logoColor=white" alt="REST API">
</div>

<div align="center">
  <h3>🚀 Backend moderno para sistema de petshop com Django REST Framework</h3>
  <p>
    <a href="#-características">Características</a> •
    <a href="#-instalação">Instalação</a> •
    <a href="#-uso">Uso</a> •
    <a href="#-api-endpoints">API</a> •
    <a href="#-contribuição">Contribuição</a>
  </p>
</div>

---

## 📋 Sobre o Projeto

Este é um backend robusto desenvolvido com **Django REST Framework** para gerenciamento de petshops. O sistema oferece uma API RESTful completa para controle de animais, clientes, serviços e agendamentos.

### 🎯 Objetivo

Fornecer uma solução backend escalável e segura para sistemas de petshop, com autenticação JWT e controle de permissões granular.

## ✨ Características

- 🔐 **Autenticação JWT** com `djangorestframework-simplejwt`
- 🛡️ **Sistema de permissões** com `django-guardian`
- 📊 **API RESTful** completa com Django REST Framework
- 🗄️ **Banco de dados** SQLite (facilmente migrável para PostgreSQL/MySQL)
- 🔒 **Segurança** implementada com melhores práticas
- 📝 **Documentação** automática da API
- 🚀 **Pronto para produção** com configurações otimizadas

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.11+ | Linguagem principal |
| **Django** | 5.2.7 | Framework web |
| **Django REST Framework** | Latest | API REST |
| **SimpleJWT** | Latest | Autenticação JWT |
| **Django Guardian** | Latest | Permissões por objeto |
| **SQLite** | 3.x | Banco de dados (desenvolvimento) |

## 📦 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/metratonpr/petshop-django-backend.git
cd petshop-django-backend
```

### 2. Crie um ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-guardian
```

### 4. Configure o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 6. Execute o servidor

```bash
python manage.py runserver
```

O servidor estará rodando em `http://127.0.0.1:8000/`

## 🚀 Uso

### Acessando a API

- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **API Root**: `http://127.0.0.1:8000/api/`
- **Documentação**: `http://127.0.0.1:8000/api/docs/` *(em desenvolvimento)*

### Autenticação

O sistema utiliza JWT (JSON Web Tokens) para autenticação. Para acessar endpoints protegidos:

1. **Obter token**:
```bash
POST /api/token/
{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```

2. **Usar token** nas requisições:
```bash
Authorization: Bearer seu_jwt_token_aqui
```

## 🔌 API Endpoints

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/token/` | Obter token de acesso |
| `POST` | `/api/token/refresh/` | Renovar token |

### Principais Recursos *(em desenvolvimento)*
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/pets/` | Listar animais |
| `POST` | `/api/pets/` | Criar animal |
| `GET` | `/api/customers/` | Listar clientes |
| `POST` | `/api/customers/` | Criar cliente |
| `GET` | `/api/services/` | Listar serviços |
| `POST` | `/api/appointments/` | Agendar serviço |

## 📁 Estrutura do Projeto

```
petshop-django-backend/
├── 📁 core/                 # Configurações principais do Django
│   ├── settings.py          # Configurações do projeto
│   ├── urls.py             # URLs principais
│   └── wsgi.py             # WSGI configuration
├── 📁 api/                  # App principal da API
│   ├── models.py           # Modelos de dados
│   ├── views.py            # Views da API
│   ├── serializers.py      # Serializers (em desenvolvimento)
│   └── urls.py             # URLs da API
├── 📁 migrations/           # Migrações do banco
├── manage.py               # Script de gerenciamento Django
├── db.sqlite3              # Banco de dados
├── requirements.txt        # Dependências (a criar)
└── README.md              # Este arquivo
```

## ⚙️ Configurações

### Variáveis de Ambiente *(recomendado para produção)*

Crie um arquivo `.env` na raiz do projeto:

```env
DEBUG=False
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=seu-dominio.com,localhost
```

### Configurações de Produção

Para deploy em produção, considere:

- ✅ Usar PostgreSQL/MySQL ao invés do SQLite
- ✅ Configurar `DEBUG=False`
- ✅ Definir `ALLOWED_HOSTS` apropriadamente
- ✅ Usar variáveis de ambiente para dados sensíveis
- ✅ Configurar servidor web (Nginx + Gunicorn)
- ✅ Implementar HTTPS

## 🧪 Testes

```bash
# Executar todos os testes
python manage.py test

# Executar testes de um app específico
python manage.py test api

# Executar com cobertura
coverage run --source='.' manage.py test
coverage report
```

## 📝 Desenvolvimento

### Contribuindo

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

### Padrões de Código

- Seguir **PEP 8** para estilo de código Python
- Usar **type hints** quando possível
- Documentar funções e classes importantes
- Escrever testes para novas funcionalidades

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **metratonpr** - *Desenvolvedor Principal* - [@metratonpr](https://github.com/metratonpr)

## 🆘 Suporte

Encontrou um problema? Tem uma sugestão?

- 🐛 [Reporte um bug](https://github.com/metratonpr/petshop-django-backend/issues)
- 💡 [Sugira uma feature](https://github.com/metratonpr/petshop-django-backend/issues)
- 📧 [Entre em contato](mailto:seu-email@exemplo.com)

---

<div align="center">
  <p>Feito com ❤️ e 🐍 Python</p>
  <p>
    <a href="#-petshop-django-backend">⬆️ Voltar ao topo</a>
  </p>
</div>