# Sistema de Gerenciamento de Usuários e Livros com Limitação de Taxa de Requisições e Autenticação com JWT
## Descrição
Este sistema implementa uma aplicação Django com funcionalidades  gerenciamento de usuários e livros com limitação de taxa de requisições baseadas no IP para proteger o sistema. A limitação de taxa é configurada para permitir até 120 requisições por 15 minutos por IP. O sistema inclui autenticação JWT para segurança e usa Django REST Framework para a API.

## Funcionalidades
- Limitação de taxa de requisições por IP.
- CRUD de usuários com autenticação JWT.
- CRUD de livros com upload de imagem.
- Sistema de autenticação e gerenciamento de sessão.
- Middleware para tratamento de CORS.

## Tecnologias Utilizadas no Backend
- HTML5
- CSS3
- JavaScript
- Python
- Django
- Django REST Framework
- JWT para autenticação
- SQLite (pode ser configurado para outros bancos de dados)
- CORS Headers

## Como Usar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-projeto
    ```
3. Crie um ambiente virtual e ative:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Configure as variáveis de ambiente no arquivo `.env`.

6. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

### Serializers
- `CustomUserSerializer`: Serializador para o modelo `CustomUser`.
- `BookSerializer`: Serializador para o modelo `Book`.

### Views
- `CustomUserViewSet`: ViewSet para gerenciar usuários.
- `BookListCreate`: View para listar e criar livros.
- `BookRetrieveUpdateDestroy`: View para recuperar, atualizar e deletar livros.

### URLs
- `/api/users/`: Endpoint para CRUD de usuários.
- `/api/books/`: Endpoint para CRUD de livros.
- `/api/auth/login/`: Endpoint para obtenção do token JWT.
- `/api/auth/login/refreshtoken/`: Endpoint para renovação do token JWT.

### Models
- `CustomUser`: Modelo customizado de usuário.
- `Book`: Modelo para armazenar informações de livros.
- `RateLimit`: Modelo para gerenciar a limitação de taxa de requisições.

### Middleware
- `RateLimitMiddleware`: Middleware para aplicar a limitação de taxa de requisições.
