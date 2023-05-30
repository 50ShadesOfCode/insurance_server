from pydantic import BaseModel

class TypeOfPaymentBase(BaseModel):
    name: str
    description: str

class TypeOfPaymentCreate(TypeOfPaymentBase):
    pass

class TypeOfPayment(TypeOfPaymentBase):
    id: int
    
    class Config:
        orm_mode = True

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
        
class PaymentBase(BaseModel):
    reason: str
    
class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    userId: int
    user: User
    typeId: int
    type: TypeOfPayment
    
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
    user: User
    
