# 📄 Django DRF Post API

A **simple Django REST Framework project** built to practice creating APIs from scratch.  
This project is designed for learning DRF fundamentals: **APIView, ModelSerializer, and JSON responses**.

---

## 🚀 Features

- Create a **Post** model with title, content, and timestamp  
- Return JSON response for all posts via **PostSerializer**  
- Use **APIView** to fetch and return posts  
- Easy-to-extend structure for **ViewSets, Routers, and full CRUD**  
- Clean and minimal — perfect for learning DRF basics

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
│   ├── serializers.py       # <-- new
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── post_api_project/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── README.md
📌 API Endpoint
Endpoint	Method	Description
/api/posts/	GET	Returns all posts in JSON using PostSerializer

⭐ Learning Outcomes
DRF setup and configuration

APIView and returning JSON

ModelSerializer usage for clean JSON responses

Preparing for ViewSets and full CRUD APIs

🔮 Future Improvements
Add CRUD endpoints using ViewSet + Router

Implement nested serializers (e.g., categories or authors)

Add POST, PUT, DELETE functionality

Add Postman tests

Expand to a full blog API with advanced features

❤️ Author
Banu Mariwan
GitHub: banumariwan
