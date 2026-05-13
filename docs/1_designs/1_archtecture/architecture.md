# Ecommerce Architecture — Production-Friendly Learning Design

Goal:

```text id="h70z7r"
simple enough to learn
strong enough for production thinking
```

We build:

```text id="8psx8k"
Modular Monolith
```

NOT microservices.

---

# 1. Core Modules

```text id="buhrrn"
Auth
Users
Catalog
Inventory
Cart
Orders
Payments
Reviews
Coupons
Notifications
Admin
```

Each module owns:

- models
- schemas
- services
- repositories
- APIs

---

# 2. Exact Ecommerce DB Schema

---

# USERS

## users

```text id="cbk3w2"
id
email
phone
password_hash
full_name
is_active
is_verified
role_id
created_at
updated_at
```

---

## roles

```text id="rf8tbg"
id
name
```

Examples:

```text id="4hyxj5"
admin
customer
seller
```

---

## addresses

```text id="m1u0y5"
id
user_id
full_name
phone
address_line_1
address_line_2
city
state
country
postal_code
is_default
```

---

# CATALOG

## categories

```text id="6n41om"
id
name
slug
parent_id
```

Self relation:

```text id="dj0y14"
electronics
  → mobiles
  → laptops
```

---

## products

```text id="n8qq5n"
id
category_id
name
slug
description
brand
price
status
created_at
updated_at
```

---

## product_images

```text id="d0mlmk"
id
product_id
image_url
is_primary
```

---

# INVENTORY

## inventory

```text id="35l8vy"
id
product_id
stock_quantity
reserved_quantity
sku
warehouse_location
updated_at
```

Important:

```text id="7o2k5g"
available_stock
=
stock_quantity - reserved_quantity
```

---

# CART

## carts

```text id="n0oc7n"
id
user_id
created_at
```

---

## cart_items

```text id="b6e2ut"
id
cart_id
product_id
quantity
price_at_time
```

Why save price?

```text id="fdjczr"
product price may change later
```

---

# ORDERS

## orders

```text id="m9olz5"
id
user_id
address_id
status
subtotal
tax_amount
discount_amount
total_amount
payment_status
created_at
```

---

## order_items

```text id="njlwmz"
id
order_id
product_id
product_name
product_price
quantity
subtotal
```

Why duplicate product data?

```text id="h7c6dn"
historical accuracy
```

---

# PAYMENTS

## payments

```text id="38tgrl"
id
order_id
provider
transaction_id
amount
currency
status
paid_at
```

Providers:

```text id="9hx5j5"
stripe
razorpay
paypal
```

---

# REVIEWS

## reviews

```text id="0u4xwb"
id
user_id
product_id
rating
comment
created_at
```

Constraint:

```text id="zsqn9o"
one review per user per product
```

---

# COUPONS

## coupons

```text id="x5brvq"
id
code
discount_type
discount_value
min_order_amount
expires_at
usage_limit
```

---

## coupon_usages

```text id="14ybyd"
id
coupon_id
user_id
order_id
used_at
```

---

# NOTIFICATIONS

## notifications

```text id="k2rjlwm"
id
user_id
title
message
type
is_read
created_at
```

---

# 3. Relations Overview

---

# Main Relations

```text id="z9ib2v"
User
 ├── Addresses
 ├── Cart
 ├── Orders
 ├── Reviews
 └── Notifications
```

---

```text id="ot5r52"
Category
 └── Products
```

---

```text id="x9uq5r"
Product
 ├── Images
 ├── Inventory
 ├── Reviews
 ├── CartItems
 └── OrderItems
```

---

```text id="zn7pnl"
Order
 ├── OrderItems
 └── Payment
```

---

# 4. ER Diagram (Simplified)

```text id="jlwmq8"
users
 ├── addresses
 ├── carts
 │    └── cart_items
 ├── orders
 │    ├── order_items
 │    └── payments
 ├── reviews
 └── notifications

categories
 └── products
      ├── product_images
      ├── inventory
      ├── reviews
      ├── cart_items
      └── order_items

coupons
 └── coupon_usages
```

---

# 5. User Flow

---

# Customer Journey

```text id="hsgv1h"
Register
→ Login
→ Browse Products
→ Add to Cart
→ Checkout
→ Create Order
→ Payment
→ Order Confirmation
→ Delivery
→ Review Product
```

---

# Admin Journey

```text id="qq5v3d"
Login
→ Manage Categories
→ Manage Products
→ Manage Inventory
→ Manage Orders
→ Manage Coupons
→ View Analytics
```

---

# 6. Order Flow

Very important backend concept.

```text id="g74kse"
Add items to cart
→ Checkout
→ Validate stock
→ Reserve inventory
→ Create order
→ Create payment record
→ Payment success
→ Confirm order
→ Reduce inventory
→ Send notification
```

---

# 7. Payment Flow

Professional payment lifecycle:

```text id="i6q0pi"
Pending
→ Processing
→ Paid
→ Failed
→ Refunded
```

---

# Payment Architecture

```text id="mdy7eq"
Frontend
→ Backend
→ Payment Gateway
→ Webhook
→ Update Payment Status
→ Update Order Status
```

Never trust frontend payment success directly.

---

# 8. Inventory Flow

Critical production concept.

---

# Stock Lifecycle

```text id="0hshlb"
Available Stock
→ Reserved During Checkout
→ Paid
→ Deduct Final Quantity
```

If payment fails:

```text id="xgd4zc"
release reserved stock
```

---

# Why reserve inventory?

Prevents:

```text id="m1zq5p"
overselling
```

---

# 9. API List

---

# AUTH APIs

```text id="vyqklm"
POST /auth/register
POST /auth/login
POST /auth/refresh
POST /auth/logout
GET  /auth/me
```

---

# PRODUCT APIs

```text id="ysn3lm"
GET    /products
GET    /products/{id}
POST   /products
PATCH  /products/{id}
DELETE /products/{id}
```

---

# CATEGORY APIs

```text id="s07x2j"
GET /categories
POST /categories
```

---

# CART APIs

```text id="c6zj78"
GET    /cart
POST   /cart/items
PATCH  /cart/items/{id}
DELETE /cart/items/{id}
```

---

# ORDER APIs

```text id="n4dkxq"
POST /orders
GET  /orders
GET  /orders/{id}
```

---

# PAYMENT APIs

```text id="m1s4m6"
POST /payments/initiate
POST /payments/webhook
```

---

# REVIEW APIs

```text id="4v50mc"
POST /reviews
GET  /products/{id}/reviews
```

---

# ADMIN APIs

```text id="fdbms7"
GET /admin/orders
GET /admin/users
GET /admin/analytics
```

---

# 10. Recommended Folder Structure

```text id="28b2nq"
app/
├── api/
│   └── v1/
│       ├── auth.py
│       ├── products.py
│       ├── categories.py
│       ├── carts.py
│       ├── orders.py
│       ├── payments.py
│       └── reviews.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   ├── database.py
│   ├── logging.py
│   └── exceptions.py
│
├── models/
├── schemas/
├── repositories/
├── services/
├── dependencies/
├── middleware/
├── workers/
├── utils/
├── tests/
├── alembic/
└── main.py
```

```
- Better production version
app/
├── api/
│   └── v1/
│       ├── endpoints/
│       └── router.py
```

---

# 11. Most Important Architecture Decision

Your architecture should optimize for:

```text id="q0htw0"
clarity
maintainability
safe growth
developer speed
```

NOT:

```text id="cvq04w"
premature complexity
```

This architecture is exactly what many strong startups begin with before scaling further.
