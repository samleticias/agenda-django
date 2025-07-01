# 📅 Agenda Django

Este projeto é uma agenda de contatos desenvolvida com Django. Ele permite que usuários se cadastrem, façam login e gerenciem seus próprios contatos de forma segura. O sistema inclui autenticação, controle de acesso, categorias, mensagens, e mais.

## Funcionalidades

- Cadastro e login de usuários com validações
- Sistema de autenticação (login/logout)
- Restrições: cada usuário só pode visualizar e editar seus próprios contatos
- CRUD de contatos com:
  - Nome, e-mail, telefone, descrição, imagem e categoria
-  Validações com `clean`, `clean_field`, `add_error`
-  Campo de pesquisa com `Q` e OR
-  Interface de administração com Django Admin
-  HTML e CSS básico com interface funcional
-  Suporte a imagens com `ImageField`
-  Mensagens amigáveis com `django.contrib.messages`
-  URLs protegidas com `login_required` e `user.is_authenticated`

## Estrutura

```
agenda-django/
│
├── agendadb/ # Configurações do projeto
├── contact/ # App principal (models, views, forms, templates)
│ ├── models.py
│ ├── forms.py
│ ├── views/
│ └── templates/
│
├── db.sqlite3 # Banco de dados local
├── manage.py
└── requirements.txt # (opcional) Dependências
```

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/samleticias/agenda-django.git
cd agenda-django
```
2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

3. Instale as dependências:

```bash
pip install django
```

4. Rode as migrações:

```bash
python manage.py migrate
```

5. Crie um superusuário:

```bash
python manage.py createsuperuser
```

6. Inicie o servidor:

```bash
python manage.py runserver
```

7. Acesse:

- Aplicação: http://localhost:8000

- Admin: http://localhost:8000/admin

---

## Controle de Acesso

- O sistema utiliza login_required nas views.
- Apenas usuários autenticados podem criar, editar ou excluir contatos.
- Apenas o owner do contato pode ver os botões de editar/excluir.
- Usuários anônimos são redirecionados ao login ao tentar acessar rotas privadas.

---

## Commits Importantes

-  Criação do modelo de **Contato** e **Categoria**
-  Relação entre `Contact` e `owner` (`request.user`)
-  Proteção com `login_required` nas views
-  Uso de `user.is_authenticated` nos templates
-  Sistema de **login**, **logout** e **registro de usuários**
-  Formulários personalizados com `UserCreationForm` e `AuthenticationForm`
-  Validações com `clean`, `clean_field`, `add_error` e `ValidationError`
-  Suporte a imagens com `ImageField`
-  Integração com `django.contrib.messages` para feedback ao usuário
-  Views de exclusão e atualização de contatos com proteção por dono
-  Oculta botões de editar/excluir para usuários não donos
-  Implementação de **campo de pesquisa** com `Q` (filtros com OR)
-  Organização de views em pacotes Python
-  Formulários com `ModelForm` e instância para edição

---

## Melhorias Futuras

-  Paginação e ordenação da lista de contatos
-  Filtro por **categoria** ou outros campos
-  Templates responsivos e modernos com **Bootstrap**
-  Painel administrativo com **estatísticas**
-  Upload de imagem com **pré-visualização**
-  Troca de senha e recuperação de conta
-  Suporte a internacionalização (i18n)
-  Testes automatizados (unitários e de integração)
-  Migração para banco de dados PostgreSQL ou MySQL
