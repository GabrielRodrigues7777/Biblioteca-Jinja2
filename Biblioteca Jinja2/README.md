# Biblioteca Flask

Sistema de gerenciamento de biblioteca usando Flask e JSON.

## Como rodar

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Rode o servidor:
```
python app.py
```

3. Acesse no navegador:
```
http://localhost:5000
```

## Rotas disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Página inicial com tabela de livros |
| GET | `/biblioteca` | Lista todos os livros em JSON |
| POST | `/biblioteca/insert` | Cadastra um novo livro |
| GET | `/biblioteca/<isbn>` | Busca livro pelo ISBN |
| DELETE | `/biblioteca/delete/<isbn>` | Deleta um livro pelo ISBN |
