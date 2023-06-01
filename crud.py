from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, type=user.type, password=user.password, login=user.login)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
def get_request(db: Session, id: int):
    return db.query(models.Request).filter(models.Request.id == id).first()

def get_requests_by_user_id(db: Session, user_id: int):
    return db.query(models.Request).filter(models.Request.userId == user_id).all()

def create_request(db: Session, request: schemas.Request, user_id: int):
    db_request = models.Request(name=request.name, userDescription=request.userDescription, status=request.status, userId=user_id)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    
     