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

Using `mcp: add server` command, you can add the PostgreSQL server to your MCP configuration.

finally this results in `mcp.json` file in `.vscode` folder

```json
{
 "servers": {
  "postgres": {
   "command": "npx",
   "args": [
    "-y",
    "@model-context-protocol/server-postgres@0.6.2",
    "postgresql://<user>:<password>@localhost:5432/<db>"
   ],
   "env": {},
   "type": "stdio"
  }
 },
 "inputs": []
}
```
