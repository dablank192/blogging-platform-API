# 📝 Blogging Platform API

A RESTful API for a blogging platform, built with **FastAPI** and **PostgreSQL**.

Project Link: https://roadmap.sh/projects/blogging-platform-api

## 🚀 Tech Stack

* **Language:** Python 3.12+
* **Framework:** FastAPI
* **Database:** PostgreSQL (with SQLAlchemy ORM)
* **Validation:** Pydantic
* **Authentication:** JWT (JSON Web Tokens) & OAuth2

## ✨ Key Features

* **Blog Operations:** Full CRUD support (Create, Read, Update, Delete) for blog posts.
* **Advanced Search:** Wildcard search functionality across titles, content, and categories.
* **Documentation:** Automatic interactive API documentation via Swagger UI.

## 🛠️ Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/dablank192/blogging-platform-API.git
    cd blogging-platform-AP
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv .venv
    
    # Windows:
    .venv\Scripts\activate
    
    # macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Database**
    Make sure your PostgreSQL server is running and update the connection string in your `database.py` file.

5.  **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation at:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

---
