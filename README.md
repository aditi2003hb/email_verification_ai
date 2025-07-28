 🤖 email_verification_ai: AI-Themed Secure Email Verification System

A secure, AI-styled backend web application built with **FastAPI**, **SQLite**, **SQLAlchemy ORM**, and **Jinja2 templates**. This project enables users to register using email, receive a temporary verification code, set their password, log in securely, and change their password — **all without using external email APIs**.

> 🧠 Developed by [aditi2003hb](https://github.com/aditi2003hb)

---

## 🚀 Features

- 📧 Email-based registration with a custom temporary code system
- 🔒 Secure password hashing using `passlib` and bcrypt
- ✅ Login functionality with proper user verification
- 🔁 Password change feature with validation
- 💾 Data stored locally using SQLite and SQLAlchemy ORM
- 🧠 Clean and robotic-themed HTML forms using Jinja2
- ⚡ Runs on Hypercorn ASGI server (not Uvicorn)

---

## 🗂️ Folder Structure

email_verification_ai/
│
├── app/
│ ├── main.py # Main FastAPI app and all routes
│ ├── database.py # SQLite database config and session setup
│ ├── models.py # SQLAlchemy user model
│ ├── crud.py # Database logic: create, check, verify, update
│ ├── schemas.py # (Optional) Pydantic schemas for type safety
│ │
│ ├── templates/ # Jinja2 HTML form templates
│ │ ├── register.html
│ │ ├── set_password.html
│ │ ├── login.html
│ │ └── change_password.html
│ │
│ └── static/ # (Optional) for CSS/images
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation (this file)

yaml
Copy code

---

## 🛠️ Tech Stack

| Component        | Tool Used               |
|------------------|-------------------------|
| Backend API      | FastAPI                 |
| Database         | SQLite                  |
| ORM              | SQLAlchemy              |
| Password Hashing | Passlib (bcrypt)        |
| Templates        | Jinja2 (HTML rendering) |
| ASGI Server      | Hypercorn               |
| Forms            | `python-multipart`      |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/aditi2003hb/email_verification_ai.git
cd email_verification_ai
2. Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
If you don’t have the requirements.txt file yet, create one and paste:

css
Copy code
fastapi
sqlalchemy
jinja2
passlib[bcrypt]
hypercorn
python-multipart
▶️ Run the App
Start the FastAPI application using Hypercorn:

bash
Copy code
hypercorn app.main:app --reload
Visit the app at: http://127.0.0.1:8000/

📌 Endpoint Summary
Method	Route	Description
GET	/register	Show email input form
POST	/register	Store email and generate code
POST	/set-password	Set password using temp code
GET/POST	/login	Login form + logic
GET/POST	/change-password	Change password after login

🔐 How It Works
User registers with an email → backend generates a temporary code

User uses that code to set a password

Password is hashed and securely saved

User logs in using email + password

User can change password securely

All passwords are hashed using bcrypt via passlib. Temporary codes ensure only verified users can proceed.

📸 UI Screenshot Placeholder

(Replace with real screenshot or remove this section if not needed)

📜 License
Licensed under the MIT License.
Use freely for learning, experimentation, or enhancement.

👩‍💻 Author
Created by aditi2003hb
