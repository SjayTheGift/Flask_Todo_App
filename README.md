
# Flask Todo App

Flask todo app that runs with docker has a frontend and backend.
The backendis the API'S, then the frontend deals with consumption of api then return the todos or add the todos.


## Run Locally

Clone the project

```bash
  git clone https://github.com/SjayTheGift/Flask_Todo_App
```

Go to the project directory, and run

```bash
  python -m venv venv
```

Activate venv on windows

```bash
  venv\Scripts\activate
```

On Mac or Linux

```bash
  source venv/bin/activate
```

Please make sure you update the docker-compose.yml file to be able to connect to posgreSQL.

```bash
  DB_URL=postgresql://postgres:postgres@flask_db:5432/postgres
```

```bash
  - POSTGRES_PASSWORD=postgres
  - POSTGRES_USER=postgres
  - POSTGRES_DB=postgres
```
Or you can leave them the way they are then try to connect to you database.


Install dependencies and Start the server

```bash
  docker compose up --build
```



## Tech Stack

**Client:** Vannila Js, Bootstarp

**Server:** Flask


## Running Tests

To run tests, run the following command

```bash
  cd backend
```

```bash
  python test_todo.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_URL="postgresql://username:password@host_name:port_no/db_name"`


