# CRM-Locadora

## Descrição:
O sistema consiste em um sistema de gerenciamento de relacionamento com o cliente (CRM) e um catálogo virtual para a locadora de jogos. O sistema permite que administradores (proprietários/funcionários) gerenciem o estoque (jogos e DLCs) e registrem pedidos, enquanto usuários autenticados (clientes) podem acessar o catálogo.

## Justificativa:
- Centralização de Gerenciamento: Registar jogos e vendas no mesmo lugar e de maneira fácil
- Divulgação de estoque: Servir como catálogo digital para clientes
- Controle Financeiro: Permitir ao administrador ver o rendimento financeiro da empresa

## Tecnologias Principais:
Backend: Python, Django
API: Django REST Framework (DRF)
Autenticação: Token Authentication (DRF)

## Endpoints da API:
A API principal está disponível sob o prefixo: /api/.



## Executando com Django
O projeto é baseado em Django e pode ser executado localmente.

### Pré-requisitos
- Python 3.8+
- Django (versão utilizada no projeto)
- Django REST Framework (DRF)

### Comandos de Inicialização:

Crie o banco de dados (SQLite) e tabelas:
```
python manage.py makemigrations
python manage.py migrate
```

Crie o Superusuário (Dono da Empresa):
```
python manage.py createsuperuser
```
Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```
A API estará acessível em http://127.0.0.1:8000/api/ e a interface administrativa em http://127.0.0.1:8000/admin/.
