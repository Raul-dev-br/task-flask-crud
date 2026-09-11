<h1 align="center">📝 Task Flask CRUD</h1>

<p align="center">API REST para gerenciamento de tarefas (To-Do), desenvolvida com Flask.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/API-REST-4CAF50?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge" />
</p>

---

## 📌 Sobre o projeto

Este projeto é uma **API REST** construída com **Flask** para praticar as operações básicas de um CRUD (Create, Read, Update, Delete) aplicadas ao gerenciamento de tarefas.

No momento, os dados são armazenados **em memória** durante a execução da aplicação — a integração com um banco de dados (como PostgreSQL) é um dos próximos passos planejados.

---

## 🚀 Endpoints

| Método   | Rota           | Descrição                          |
|----------|----------------|-------------------------------------|
| `GET`    | `/tasks`       | Lista todas as tarefas              |
| `GET`    | `/tasks/<id>`  | Retorna uma tarefa específica       |
| `POST`   | `/tasks`       | Cria uma nova tarefa                |
| `PUT`    | `/tasks/<id>`  | Atualiza uma tarefa existente       |
| `DELETE` | `/tasks/<id>`  | Remove uma tarefa                   |

### Exemplo de tarefa (JSON)

```json
{
  "id": 1,
  "title": "Estudar Flask",
  "description": "Revisar rotas e métodos HTTP",
  "done": false
}
```

---

## 🛠️ Tecnologias

- **Python**
- **Flask**

---

## 🗺️ Próximos passos

- [ ] Persistência de dados com banco de dados (PostgreSQL)
- [ ] Validação de dados de entrada
- [ ] Tratamento de erros e status codes mais detalhados
- [ ] Documentação dos endpoints (ex.: Swagger/OpenAPI)

---

## 👤 Autor

Desenvolvido por **Raul Ferreira**

<p align="left">
  <a href="https://www.linkedin.com/in/raul-dev-br07/">
    <img src="https://img.shields.io/badge/LinkedIn-0082FA?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="mailto:raulferreirapinto41@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
</p>