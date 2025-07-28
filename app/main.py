from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# App & templates
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Redirect root to /register
@app.get("/", response_class=HTMLResponse)
def home():
    return RedirectResponse("/register")

@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(request: Request, email: str = Form(...), db: Session = Depends(get_db)):
    existing = crud.get_user(db, email)
    if existing:
        return RedirectResponse("/login?msg=already_registered", status_code=302)
    user = crud.create_user(db, email)
    return templates.TemplateResponse("set_password.html", {
        "request": request, "email": user.email, "code": user.temp_code
    })

@app.post("/set-password")
def set_password(request: Request,
                 email: str = Form(...),
                 code: str = Form(...),
                 password: str = Form(...),
                 confirm_password: str = Form(...),
                 db: Session = Depends(get_db)):
    user = crud.get_user(db, email)
    if not user or user.temp_code != code:
        return HTMLResponse("Invalid code or email", status_code=400)
    if password != confirm_password:
        return HTMLResponse("Passwords do not match", status_code=400)
    crud.set_new_password(db, user, password)
    return RedirectResponse("/login?msg=now_login", status_code=302)

@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request, msg: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "msg": msg})

@app.post("/login")
def login(request: Request,
          email: str = Form(...),
          password: str = Form(...),
          db: Session = Depends(get_db)):
    user = crud.get_user(db, email)
    if not user or user.is_temp:
        return RedirectResponse("/login?msg=need_set_password", status_code=302)
    if not crud.verify_password(password, user.password):
        return HTMLResponse("Wrong password", status_code=400)
    return HTMLResponse(f"Welcome, {user.email}!")

@app.get("/change-password", response_class=HTMLResponse)
def cp_form(request: Request):
    return templates.TemplateResponse("change_password.html", {"request": request})

@app.post("/change-password")
def change_password(request: Request,
                    email: str = Form(...),
                    password: str = Form(...),
                    new_password: str = Form(...),
                    confirm_new: str = Form(...),
                    db: Session = Depends(get_db)):
    user = crud.get_user(db, email)
    if not user or not crud.verify_password(password, user.password):
        return HTMLResponse("Invalid credentials", status_code=400)
    if new_password != confirm_new:
        return HTMLResponse("New passwords do not match", status_code=400)
    crud.set_new_password(db, user, new_password)
    return HTMLResponse("Password changed! You can now <a href=\"/login\">login</a>.")
