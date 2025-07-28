import random
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_temp_code():
    return "".join(str(random.randint(0, 9)) for _ in range(5))

def create_user(db: Session, email: str):
    code = generate_temp_code()
    user = models.RegUser(email=email, temp_code=code)
    db.add(user); db.commit(); db.refresh(user)
    return user

def get_user(db: Session, email: str):
    return db.query(models.RegUser).filter(models.RegUser.email == email).first()

def set_new_password(db: Session, user: models.RegUser, raw_password: str):
    hashed = pwd_context.hash(raw_password)
    user.password = hashed
    user.is_temp = False
    db.commit(); db.refresh(user)
    return user

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)
