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

---

## Way to download zip file, extract it and delete the zip in Powershell

---

```powershell
Invoke-WebRequest -Uri "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3_django_orm/lab2_template.zip" -OutFile "lab2_template.zip"
Expand-Archive -Path "lab2_template.zip" -DestinationPath "lab2_template"
Remove-Item -Path "lab2_template.zip"
```
