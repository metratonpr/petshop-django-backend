# 📡 Documentação da API - Petshop Django Backend

## 🚀 Importando no Postman

### 1. **Importar Collection**
- Abra o Postman
- Clique em "Import"
- Selecione o arquivo: `postman/Petshop_Django_API.postman_collection.json`

### 2. **Importar Environment**
- Clique em "Import" novamente
- Selecione o arquivo: `postman/Petshop_Development.postman_environment.json`
- Selecione o environment "Petshop Development"

---

## 🔗 Endpoints Disponíveis

### 🔐 **Autenticação**

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/token/` | Obter token JWT |
| `POST` | `/api/token/refresh/` | Renovar token JWT |

**Exemplo de Login:**
```json
POST /api/token/
{
    "username": "admin",
    "password": "admin123"
}
```

**Resposta:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

---

### 👥 **Usuários** `/api/users/`

| Método | Endpoint | Permissão | Descrição |
|--------|----------|-----------|-----------|
| `GET` | `/api/users/` | Autenticado | Lista usuários |
| `GET` | `/api/users/{id}/` | Autenticado | Usuário específico |
| `POST` | `/api/users/` | Autenticado | Criar usuário |
| `PUT` | `/api/users/{id}/` | Autenticado | Atualizar usuário |
| `PATCH` | `/api/users/{id}/` | Autenticado | Atualizar parcial |
| `DELETE` | `/api/users/{id}/` | Autenticado | Deletar usuário |

**Exemplo de Criação:**
```json
POST /api/users/
{
    "username": "novo_usuario",
    "email": "usuario@exemplo.com",
    "password": "senha123"
}
```

**Resposta:**
```json
{
    "id": 2,
    "username": "novo_usuario",
    "email": "usuario@exemplo.com",
    "groups": []
}
```

---

### 📋 **Ordens de Produção** `/api/ordens-producao/`

| Método | Endpoint | Permissão | Descrição |
|--------|----------|-----------|-----------|
| `GET` | `/api/ordens-producao/` | Autenticado | Lista ordens |
| `GET` | `/api/ordens-producao/{id}/` | Autenticado | Ordem específica |
| `POST` | `/api/ordens-producao/` | Autenticado | Criar ordem |
| `PUT` | `/api/ordens-producao/{id}/` | Owner/Admin | Atualizar ordem |
| `PATCH` | `/api/ordens-producao/{id}/` | Owner/Admin | Atualizar parcial |
| `DELETE` | `/api/ordens-producao/{id}/` | Owner/Admin | Deletar ordem |

**Exemplo de Criação:**
```json
POST /api/ordens-producao/
{
    "produto": "Ração Premium para Cães",
    "quantidade": 50
}
```

**Resposta:**
```json
{
    "id": 1,
    "owner": "admin",
    "produto": "Ração Premium para Cães",
    "quantidade": 50,
    "data_criacao": "2025-10-29T14:30:00Z"
}
```

---

## 🛡️ **Sistema de Permissões**

### **Usuários:**
- **Usuários normais**: Veem apenas seus próprios dados
- **Staff/Superuser**: Veem todos os usuários

### **Ordens de Produção:**
- **Usuários normais**: Veem apenas suas próprias ordens
- **Gerentes**: Veem todas as ordens
- **Superuser**: Acesso total
- **Edição/Exclusão**: Apenas owner ou admin

---

## 🚦 **Fluxo de Teste Recomendado**

### 1. **Autenticação**
```
1. POST /api/token/ (obter token)
2. Copiar access_token para variável
```

### 2. **Teste de Usuários**
```
1. GET /api/users/ (listar)
2. POST /api/users/ (criar)
3. GET /api/users/{id}/ (detalhe)
4. PATCH /api/users/{id}/ (atualizar)
```

### 3. **Teste de Ordens**
```
1. GET /api/ordens-producao/ (listar)
2. POST /api/ordens-producao/ (criar)
3. GET /api/ordens-producao/{id}/ (detalhe)
4. PATCH /api/ordens-producao/{id}/ (atualizar)
```

---

## 🔧 **Configuração para Codespaces**

Se estiver usando GitHub Codespaces, altere a variável `base_url` para:
```
https://{{CODESPACE_NAME}}-8000.{{GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}}
```

---

## 📊 **Status Codes Esperados**

| Código | Descrição |
|--------|-----------|
| `200` | Sucesso |
| `201` | Criado com sucesso |
| `400` | Dados inválidos |
| `401` | Não autorizado |
| `403` | Sem permissão |
| `404` | Não encontrado |
| `500` | Erro interno |

---

## 🧪 **Testes Automatizados**

A collection inclui scripts de teste automático que:
- ✅ Extraem tokens automaticamente
- ✅ Validam respostas
- ✅ Configuram variáveis para próximos testes
- ✅ Verificam status codes

Para executar os testes:
1. Importe a collection
2. Clique em "Run Collection"
3. Veja os resultados automáticos

---

## 🚀 **Próximos Passos**

1. **Criar superusuário** no Django
2. **Importar collections** no Postman
3. **Testar autenticação** primeiro
4. **Explorar endpoints** disponíveis
5. **Criar novos dados** para teste