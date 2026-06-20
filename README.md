# 🍔 Eato - Online Food Ordering System

## Overview
Eato is a Django + MySQL based Online Food Ordering System with separate **Admin** and **User** panels.

## Features
- User Registration & Login
- Admin Login
- Dashboard
- Category Management
- Product Management
- Banner Management
- Shopping Cart
- Payment (Demo)
- Order Management
- Incoming Orders
- My Orders
- Responsive Bootstrap UI

---

# 🛠 Requirements

- Python 3.11+
- MySQL Server 8+
- Git (Optional)
- VS Code
- pip

---

# 1. Clone / Download

```bash
git clone <repository-url>
cd eato_project
```

Or extract the ZIP.

---

# 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

# 3. Install Django

```bash
pip install django
```

Install MySQL driver

```bash
pip install mysqlclient
```

If mysqlclient fails:

```bash
pip install pymysql
```

---

# 4. Install Requirements

```bash
pip install -r requirements.txt
```

or

```bash
pip install django mysqlclient pillow
```

---

# 5. Create MySQL Database

```sql
CREATE DATABASE eato_db;
```

Create user (optional)

```sql
CREATE USER 'eato'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON eato_db.* TO 'eato'@'localhost';
FLUSH PRIVILEGES;
```

---

# 6. Configure settings.py

```python
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'eato_db',
        'USER':'root',
        'PASSWORD':'your_password',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```

Media

```python
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/'media'
```

urls.py

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

# 7. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 8. Create Superuser

```bash
python manage.py createsuperuser
```

Example

Username

```
admin
```

Email

```
admin@eato.com
```

Password

```
admin123
```

---

# 9. Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# Images

# Images

| Screen | Image |
|---------|-------|
| Index | ![](images/index.png) |
| Login | ![](images/login.png) |
| Signup | ![](images/signin.png) |
| Admin Dashboard | ![](images/admindashboad.png) |
| Add Product | ![](images/addproduct.png) |
| Add Product Form 1 | ![](images/addproductform1.png) |
| Add Product Form 2 | ![](images/addproductform.png) |
| User Dashboard | ![](images/userdashboard.png) |
| User Dashboard Foods | ![](images/userdashboard2.png) |
| Cart | ![](images/cart.png) |
| Payment | ![](images/payment.png) |
| Order Success | ![](images/ordersucces.png) |
| My Orders | ![](images/myorders.png) |
| Incoming Orders | ![](images/incoming.png) |
---

# Project Flow

```text
Landing Page
      |
 Login / Signup
      |
 User Dashboard
      |
 Categories
      |
 Products
      |
 Add To Cart
      |
 Payment
      |
 Order Success
      |
 My Orders

                 Admin
                    |
             Admin Dashboard
                    |
   Category -> Product -> Banner
                    |
          Incoming Orders
```

---

# Project Structure (archive)

- eato_project/accounts/
- eato_project/accounts/__init__.py
- eato_project/accounts/__pycache__/
- eato_project/accounts/__pycache__/__init__.cpython-311.pyc
- eato_project/accounts/__pycache__/admin.cpython-311.pyc
- eato_project/accounts/__pycache__/apps.cpython-311.pyc
- eato_project/accounts/__pycache__/context_processors.cpython-311.pyc
- eato_project/accounts/__pycache__/forms.cpython-311.pyc
- eato_project/accounts/__pycache__/models.cpython-311.pyc
- eato_project/accounts/__pycache__/urls.cpython-311.pyc
- eato_project/accounts/__pycache__/views.cpython-311.pyc
- eato_project/accounts/admin.py
- eato_project/accounts/apps.py
- eato_project/accounts/forms.py
- eato_project/accounts/migrations/
- eato_project/accounts/migrations/0001_initial.py
- eato_project/accounts/migrations/0002_profile_delete_customer.py
- eato_project/accounts/migrations/0003_category.py
- eato_project/accounts/migrations/0004_banner.py
- eato_project/accounts/migrations/0005_product.py
- eato_project/accounts/migrations/0006_product_discount_price_product_unit_and_more.py
- eato_project/accounts/migrations/__init__.py
- eato_project/accounts/migrations/__pycache__/
- eato_project/accounts/migrations/__pycache__/0001_initial.cpython-311.pyc
- eato_project/accounts/migrations/__pycache__/0002_profile_delete_customer.cpython-311.pyc
- eato_project/accounts/migrations/__pycache__/0003_category.cpython-311.pyc
- eato_project/accounts/migrations/__pycache__/0004_banner.cpython-311.pyc
- eato_project/accounts/migrations/__pycache__/0005_product.cpython-311.pyc
- eato_project/accounts/migrations/__pycache__/0006_product_discount_price_product_unit_and_more.cpython-311.pyc
- eato_project/accounts/migrations/__pycache__/__init__.cpython-311.pyc
- eato_project/accounts/models.py
- eato_project/accounts/tests.py
- eato_project/accounts/urls.py
- eato_project/accounts/views.py
- eato_project/eato_project/
- eato_project/eato_project/__init__.py
- eato_project/eato_project/__pycache__/
- eato_project/eato_project/__pycache__/__init__.cpython-311.pyc
- eato_project/eato_project/__pycache__/settings.cpython-311.pyc
- eato_project/eato_project/__pycache__/urls.cpython-311.pyc
- eato_project/eato_project/__pycache__/wsgi.cpython-311.pyc
- eato_project/eato_project/asgi.py
- eato_project/eato_project/settings.py
- eato_project/eato_project/urls.py
- eato_project/eato_project/wsgi.py
- eato_project/manage.py
- eato_project/media/
- eato_project/media/banner_images/
- eato_project/media/banner_images/Banner1_oywMMRN.png
- eato_project/media/banner_images/Banner2.png
- eato_project/media/banner_images/Banner2_0ToLhOa.png
- eato_project/media/banner_images/Banner3.png
- eato_project/media/banner_images/ChatGPT_Image_Jun_20_2026_11_28_41_AM.png
- eato_project/media/banner_images/banner1.png
- eato_project/media/category/
- eato_project/media/category/OIP.png
- eato_project/media/category/photo-1513104890138-7c749659a591.png
- eato_project/media/category/photo-1544025162-d76694265947.png
- eato_project/media/category/photo-1547592180-85f173990554.png
- eato_project/media/category/photo-1568901346375-23c9450c58cd.png
- eato_project/media/category/photo-1578985545062-69928b1d9587.png
- eato_project/media/category/photo-1612929633738-8fe44f7ec841.png
- eato_project/media/product_images/
- eato_project/media/product_images/Pizza_Margherita_stu_spivack.jpg
- eato_project/media/products/
- eato_project/media/products/Dosa_at_Sri_Ganesha_Restauran_Bangkok_44570742744.jpg
- eato_project/media/profile_images/
- eato_project/media/profile_images/6f6cafaffc78e29ee03b3680f47d3351.jpg
- eato_project/profile_images/
- eato_project/profile_images/6f6cafaffc78e29ee03b3680f47d3351.jpg
- eato_project/profile_images/6f6cafaffc78e29ee03b3680f47d3351_FWXbns2.jpg
- eato_project/profile_images/6f6cafaffc78e29ee03b3680f47d3351_dpI2rYG.jpg
- eato_project/static/
- eato_project/static/images/
- eato_project/static/images/1000343641.jpg
- eato_project/static/images/1000343642.jpg
- eato_project/static/images/Banner1.png
- eato_project/static/images/Banner2.png
- eato_project/static/images/Banner3.png
- eato_project/static/images/Dominos.png
- eato_project/static/images/a2b.png
- eato_project/static/images/burgerking.png
- eato_project/static/images/haldirams.png
- eato_project/static/images/kfc.png
- eato_project/static/images/pizzahunt.png
- eato_project/templates/
- eato_project/templates/addcategory.html
- eato_project/templates/addcategoryform.html
- eato_project/templates/addnewbannerform.html
- eato_project/templates/addproduct.html
- eato_project/templates/addproductform.html
- eato_project/templates/addrestaurant.html
- eato_project/templates/admindashboard.html
- eato_project/templates/adminnavbar.html
- eato_project/templates/adminsidebar.html
- eato_project/templates/banner.html
- eato_project/templates/cart.html
- eato_project/templates/category.html
- eato_project/templates/coupon.html
- eato_project/templates/edit_admin_profile.html
- eato_project/templates/editbannerform.html
- eato_project/templates/editcategory.html
- eato_project/templates/incomeorder.html
- eato_project/templates/index.html
- eato_project/templates/login.html
- eato_project/templates/myorders.html
- eato_project/templates/navbar.html
- eato_project/templates/ordersuccess.html
- eato_project/templates/payment.html
- eato_project/templates/settings.html
- eato_project/templates/sidebar.html
- eato_project/templates/signup.html
- eato_project/templates/userdashboard.html
- eato_project/templates/users.html


---

# Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

# Tech Stack

- Django
- Python
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- MySQL
- Pillow

---

# Author

**Harish Raj S**

