# pyproject.toml

## ✅ Do modern FastAPI projects use `pyproject.toml`?

**Yes. Almost all modern Python projects (including FastAPI) use it.**

It has effectively replaced:

- `requirements.txt` (partially)
- `setup.py`
- `setup.cfg`

This shift comes from official Python standards like:

- PEP 518
- PEP 621

---

## 📦 What is `pyproject.toml`?

It’s a **single configuration file** that defines:

- Project metadata
- Dependencies
- Build system
- Tool configurations

👉 Think of it as:
**“the central control file for your Python project”**

---

## 🔧 What does it actually do?

### 1. Dependency management

Instead of:

```
requirements.txt
```

You write:

```toml
[project]
dependencies = [
  "fastapi",
  "uvicorn",
]
```

---

### 2. Build system definition

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

---

### 3. Tool configuration (very important)

Many tools now use it:

- Black
- Ruff
- Poetry

Example:

```toml
[tool.ruff]
line-length = 100
```

---

## 🚀 Is it production-grade?

✔️ **Yes — fully production-grade.**

In fact:

- It’s part of **official Python packaging standards**
- Used in **serious production systems**
- Supported by modern tools like:
  - pip
  - Poetry
  - Hatch

👉 Companies and open-source projects are actively migrating to it.

---

## 🧠 What do latest best practices say?

### Current official direction (2024–2025+):

- ✅ Use `pyproject.toml` as the **single source of truth**
- ❌ Avoid relying only on `requirements.txt`
- ✅ Use modern dependency tools:
  - Poetry / Hatch / PDM

---

## ⚖️ `pyproject.toml` vs `requirements.txt`

| Feature               | pyproject.toml | requirements.txt |
| --------------------- | -------------- | ---------------- |
| Dependency management | ✅ Modern      | ⚠️ Basic         |
| Version constraints   | ✅ Structured  | ✅ Flat          |
| Tool config           | ✅ Yes         | ❌ No            |
| Build system          | ✅ Yes         | ❌ No            |
| Production ready      | ✅ Yes         | ✅ Yes (legacy)  |

---

## 🧩 FastAPI-specific reality

When you create a modern FastAPI app, you’ll often see:

### Option A (modern)

- `pyproject.toml` ✅

### Option B (older/simple)

- `requirements.txt`

👉 Both work, but:

- **New projects → use `pyproject.toml`**
- **Legacy projects → still use requirements.txt**

---

## 🧪 Example (FastAPI project)

```toml
[project]
name = "my-fastapi-app"
version = "0.1.0"
dependencies = [
    "fastapi",
    "uvicorn[standard]"
]
```

---

## 🧾 Final verdict

✔️ Yes, modern FastAPI projects use `pyproject.toml`
✔️ It is **official, standardized, and production-ready**
✔️ It’s the **future of Python project management**

---

# 🚀 For NEW FastAPI projects (recommended way)

- ✔️ Use tools like Poetry / Hatch / PDM

1. Use Poetry (most popular)

Just run:

```bash
poetry new my-fastapi-app
cd my-fastapi-app
poetry add fastapi uvicorn
```

👉 This will:

✅ Automatically create pyproject.toml
✅ Add dependencies correctly
✅ Handle versions & virtual env

---

# 🔄 For EXISTING projects (very important)

- ✔️ Use tools like Poetry / Hatch / PDM

Let’s say you already have:

requirements.txt
Option 1: Convert using Poetry
poetry init

👉 It will:

Ask you questions
Let you import dependencies
Generate pyproject.toml
