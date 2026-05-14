# PostgreSQL — psql Basics & Database Commands

## What is `psql`?

`psql` = PostgreSQL interactive terminal client.

Used for:

- database management
- SQL execution
- debugging
- user/role management
- administration

!!! note

```
`psql` meta commands start with `\`
SQL commands end with `;`
```

---

## Open PostgreSQL Terminal

```bash
# Default login
psql -U postgres

# Connect using host + port
psql -U postgres -h localhost -p 5432

# Connect directly to database
psql -U postgres -d mydb

# Connection URL format
psql postgresql://postgres:password@localhost:5432/mydb
```

| Option | Meaning  |
| ------ | -------- |
| `-U`   | username |
| `-h`   | host     |
| `-p`   | port     |
| `-d`   | database |

---

## Database Operations

```sql
-- Create database
CREATE DATABASE mydb;

-- List databases
\l
\list

-- Connect database
\c mydb

-- Exit psql
\q
```

---

## Important `psql` Meta Commands

```sql
-- List tables
\dt

-- Describe table
\d table_name

-- List users/roles
\du

-- Current database
SELECT current_database();

-- Current user
SELECT current_user;

-- Connection info
\conninfo

-- Query history
\s

-- Clear terminal
\! clear
```

---

## Basic SQL Commands

```sql
-- Create table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);

-- Insert data
INSERT INTO users (name, email)
VALUES ('Ashok', 'ashok@example.com');

-- Read data
SELECT * FROM users;

-- Update data
UPDATE users
SET name = 'Ashok Kumar'
WHERE id = 1;

-- Delete data
DELETE FROM users
WHERE id = 1;
```

---

## User & Role Commands

```sql
-- Create user
CREATE USER myuser WITH PASSWORD 'mypassword';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

-- Change password
ALTER USER myuser WITH PASSWORD 'newpassword';
```

---

## Useful CLI Commands

```bash
# Run SQL file
psql -U postgres -d mydb -f schema.sql

# Execute single query
psql -U postgres -d mydb -c "SELECT version();"

# Backup database
pg_dump -U postgres mydb > backup.sql

# Restore database
psql -U postgres mydb < backup.sql
```

---

## PostgreSQL Service Commands

### Ubuntu/Linux

```bash
# Start service
sudo systemctl start postgresql

# Stop service
sudo systemctl stop postgresql

# Restart service
sudo systemctl restart postgresql

# Service status
sudo systemctl status postgresql
```

---

## Naming Conventions

| Object      | Convention |
| ----------- | ---------- |
| databases   | snake_case |
| tables      | plural     |
| columns     | snake_case |
| primary key | `id`       |
| foreign key | `user_id`  |

---
