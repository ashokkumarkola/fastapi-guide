# 🌐 CORS (Cross-Origin Resource Sharing)

---

## 📌 What is CORS?

**CORS** is a **browser security mechanism** that controls whether a web page can make requests to a **different origin (domain)**.

⚠️ **Important:**  
CORS is enforced by the **browser**, **NOT by the server**.  
Servers only return **headers telling the browser what is allowed**.

---

## 🌍 What is an Origin?

**Origin = (scheme + domain + port)**

Example:

```
[http://localhost:3000](http://localhost:3000)
│     │           │
│     │           └── Port
│     └──────────── Domain
└────────────────── Scheme

```

### Example Comparisons

| Request From          | Request To             | Result              |
| --------------------- | ---------------------- | ------------------- |
| http://localhost:3000 | http://localhost:3000  | ✔ Same Origin       |
| http://localhost:3000 | http://localhost:8000  | ❌ Different Port   |
| http://localhost:3000 | https://localhost:3000 | ❌ Different Scheme |
| http://localhost:3000 | http://example.com     | ❌ Different Domain |

👉 **Any difference = Cross-Origin**

---

## 🔐 Why CORS Exists

Without CORS, a **malicious website** could make requests to another website using your browser and **steal sensitive data**.

### Example Attack Scenario

You are logged into:

```

[https://bank.com](https://bank.com)

```

You open a malicious site:

```

[https://evil.com](https://evil.com)

```

Without CORS restrictions, **evil.com** could send requests to **bank.com** using your **session cookies**.

🛡️ **CORS prevents this by requiring explicit permission.**

---

## 🔄 Simple Request vs Preflight Request

### 1️⃣ Simple Request

The **browser directly sends the request**.

#### Conditions

**Allowed Methods**

- `GET`
- `POST`
- `HEAD`

**Allowed Content-Type**

- `application/x-www-form-urlencoded`
- `multipart/form-data`
- `text/plain`

Example:

```

GET /users

```

---

### 2️⃣ Preflight Request

The browser first sends a **test request**.

Method:

```

OPTIONS

```

Purpose:

> "Am I allowed to send this request?"

#### Triggered When

- Method is `PUT`, `PATCH`, or `DELETE`
- `Authorization` header is present
- Custom headers are used
- `Content-Type = application/json`

---

### Example Preflight Request

```

OPTIONS /api/users

```

Headers:

```

Origin: [http://localhost:3000](http://localhost:3000)
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization

```

### Server Response

```

Access-Control-Allow-Origin: [http://localhost:3000](http://localhost:3000)
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Authorization

```

If the browser **approves**, the **actual request is sent**.

---

## 📦 Important CORS Headers

| Header                             | Purpose                                 |
| ---------------------------------- | --------------------------------------- |
| `Access-Control-Allow-Origin`      | Allowed domains                         |
| `Access-Control-Allow-Methods`     | Allowed HTTP methods                    |
| `Access-Control-Allow-Headers`     | Allowed request headers                 |
| `Access-Control-Allow-Credentials` | Allows cookies / authentication         |
| `Access-Control-Expose-Headers`    | Allows frontend to read certain headers |
| `Access-Control-Max-Age`           | Cache duration for preflight response   |

---

## ⚠️ Security Notes

🚫 **NEVER use**

```python
allow_origins=["*"]
allow_credentials=True
```

Reason:

Browsers **block this combination**.

### ❌ Bad Practice

```python
allow_origins=["*"]
allow_credentials=True # Credential is not supported if origin is *
```

### ✅ Correct Practice

Explicitly define **trusted origins**.

---

## 🧪 Development vs 🚀 Production

### Development

```
allow_origins = ["*"]
```

or

```
allow_origins = ["http://localhost:3000"]
```

---

### Production

Only allow **trusted frontend domains**.

Example:

```
https://myapp.com
https://admin.myapp.com
https://api.myapp.com

allow_origin_regex="https://.*\.myapp\.com"
```

🔒 This ensures **secure cross-origin communication**.

```

```
