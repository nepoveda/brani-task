from pydantic import BaseModel, EmailStr


class OrderBase(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class TagBase(BaseModel):
    name: str

    class Config:
        orm_mode = True
