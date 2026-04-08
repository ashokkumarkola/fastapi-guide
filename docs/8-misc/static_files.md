# 📁 Static Files (FastAPI)

## 🔹 What are Static Files?

Files served **as-is** (no processing)

**Examples**

- Images → `.png`, `.jpg`
- Styles → `.css`
- Scripts → `.js`
- Docs → `.pdf`
- Assets → fonts, icons, `favicon.ico`

---

## 🔹 Why "Static"?

- No change per request
- No backend logic
- No DB calls
- Direct file response

👉 Server just **reads → returns**

---

## 🔹 FastAPI Support

Use `StaticFiles`:

```python
from fastapi.staticfiles import StaticFiles
# or
from starlette.staticfiles import StaticFiles
```

---

## 🔹 Mounting Static Files

Mount = attach a **sub-application**

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```

---

## 🔹 Parameters

- `/static` → URL path (access path)
- `directory="static"` → folder location
- `name="static"` → internal reference

---

## 🔹 Accessing Files

```
http://localhost:8000/static/image.png
http://localhost:8000/static/style.css
```

---

## 🔹 Key Concepts

- 📦 Static vs Dynamic
- ⚡ Zero processing
- 🧩 Mounted app
- 📂 File-based serving
- 🚀 Fast delivery

---

## 🔹 Typical Project Structure

```
project/
│
├── main.py
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
```

---

## 🔹 Pro Tips

- Keep static separate from backend logic
- Use CDN for production
- Enable caching for performance
- Compress images & assets

```
User uploads image
        ↓
Backend API (FastAPI / Django etc.)
        ↓
Stored in Object Storage (S3 / GCS)
        ↓
Served via CDN (Cloudflare / Akamai)
        ↓
User loads image from CDN URL
```

---
