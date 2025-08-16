# Django Application Development with SQL and Databases

## This is a code along for the labs in the course. This is a part of the IBM Full Stack Developer Professional Certificate

---

## Building PostgreSQL Docker Container

---

### Docker Compose Configuration

```yaml
version: "3.8"
services:
  db:
    image: postgres:latest
    env_file:
      - postgres.env
    ports:
      - "5432:5432"
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
```

### Running the Container

from root folder

```bash
cd postgres
docker-compose up -d
```

---

## Setting up postgres MCP server

---

Install PostgreSQL extension for Visual Studio Code by microsoft, that provides rich language support for PostgreSQL, including syntax highlighting, code completion, and query execution.
Also it provides mcp support for PostgreSQL.