📄 Django DRF Post API

A **simple Django REST Framework project** built to practice creating APIs from scratch.  
This project now includes **ModelSerializer, ModelViewSet, and Router** to provide full CRUD operations automatically.

---

## 🚀 Features

- **Post model** with title, content, and timestamp  
- **ModelSerializer** converts models to JSON automatically  
- **ModelViewSet + Router** provides full CRUD:
  - List all posts  
  - Retrieve a single post  
  - Create new posts  
  - Update posts (full & partial)  
  - Delete posts  
- Minimal setup — perfect for learning DRF basics and extending later

---

## 🛠️ Tech Stack

- **Python 3**  
- **Django 5**  
- **Django REST Framework**  
- SQLite (default development database)

---

## 📦 Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/banumariwan/post_api_project.git
cd post_api_project
2️⃣ Create and activate a virtual environment:

bash
Copy code
python -m venv env
# Linux/Mac
source env/bin/activate
# Windows
env\Scripts\activate
3️⃣ Install dependencies:

bash
Copy code
pip install djangorestframework
pip install -r requirements.txt   # if you have one
4️⃣ Apply migrations:

bash
Copy code
python manage.py migrate
5️⃣ Create superuser (optional, for admin):

bash
Copy code
python manage.py createsuperuser
6️⃣ Run the server:

bash
Copy code
python manage.py runserver
📁 Project Structure
pgsql
Copy code
post_api_project/
│
├── posts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py        # <-- now includes PostViewSet
│   ├── urls.py         # <-- now includes Router
│   ├── admin.py
│   └── apps.py
│
├── post_api_project/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── README.md
📌 API Endpoints
Endpoint	Method	Description
/api/posts/	GET	List all posts
/api/posts/<id>/	GET	Retrieve a single post
/api/posts/	POST	Create a new post
/api/posts/<id>/	PUT	Update a post fully
/api/posts/<id>/	PATCH	Update a post partially
/api/posts/<id>/	DELETE	Delete a post

Accessible via DRF Browsable API at http://127.0.0.1:8000/api/posts/

⭐ Learning Outcomes
DRF setup and configuration

Returning JSON with ModelSerializer

Full CRUD with ModelViewSet and Router

Preparing for nested serializers, relations, and advanced API patterns

🔮 Future Improvements
Add nested serializers (e.g., categories or authors)

Add Postman tests

Extend to full blog API

Implement authentication & permissions

❤️ Author
Banu Mariwan
GitHub: banumariwan
