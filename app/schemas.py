from pydantic import BaseModel, EmailStr, constr

class EmailSchema(BaseModel):
    email: EmailStr

class TempCodeSchema(BaseModel):
    email: EmailStr
    code: constr(min_length=5, max_length=5)

class PasswordCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=6)
    confirm_password: constr(min_length=6)
