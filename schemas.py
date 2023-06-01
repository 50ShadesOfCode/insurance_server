from pydantic import BaseModel

class UserBase(BaseModel):
    login: str
    name: str
    type: str
    password: str
    
class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class RequestBase(BaseModel):
    name: str
    userDescription: str
    status: str
    
class RequestCreate(RequestBase):
    pass

class Request(RequestBase):
    id: int
    userId: int
    class Config:
        orm_mode = True
