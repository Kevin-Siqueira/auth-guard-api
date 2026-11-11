# 🛡️ AuthGuard API — Central de Autenticação & Autorização RBAC

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

API RESTful completa de autenticação, autorização baseada em papéis (RBAC) e revogação de tokens JWT com armazenamento em cache de alta velocidade via Redis.

---

### 🚀 Funcionalidades Principais

- **Autenticação JWT Segura:** Emissão de Access Tokens (15 min) e Refresh Tokens (7 dias).
- **Proteção contra Reuso (Token Blacklist):** Endpoint de `/logout` que invalida instantaneamente o Access Token no Redis.
- **Controlo de Acesso Baseado em Papéis (RBAC):** Restrições de endpoints dinâmicas por nível de acesso (`user` vs `admin`).
- **Segurança de Senhas:** Hashing unidirecional com `bcrypt`.
- **Conteinização Total:** Ambiente pronto para produção com Docker e Docker Compose.
- **Testes Automatizados:** Suíte completa cobrindo autenticação e rotas protegidas com `pytest`.

---

### 🛠️ Arquitetura do Projeto

```text
auth-guard-api/
├── app/
│   ├── api/          # Endpoints REST e injeção de dependências (security/deps)
│   ├── core/         # Configurações globais, segurança JWT e conexão PostgreSQL
│   ├── models/       # Entidades da base de dados (SQLAlchemy)
│   ├── schemas/      # Validação e serialização de dados (Pydantic)
│   └── services/     # Gestão da Blacklist de Tokens com Redis
├── tests/            # Testes automatizados com pytest
└── docker-compose.yml