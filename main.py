from fastapi import FastAPI, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = [
    'http://localhost',
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register", response_model=schemas.User)
async def createUser(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_login(db, user.login)
    if db_user:
        raise HTTPException(status_code=400, detail='Login already in use')
    return crud.create_user(db, user)

@app.post("/login", response_model=schemas.User)
async def login(login: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_login(db, login)
    if db_user == None:
        raise HTTPException(status_code=400, detail='Wrong login')
    if db_user.password == password:
        return crud.get_user_by_login(db, login)
    raise HTTPException(status_code=400, detail='Wrong password')

@app.get("/getRequests/{user_id}", response_model=list[schemas.Request])
async def getRequests(user_id: int, db: Session = Depends(get_db)):
    return crud.get_requests_by_user_id(db, user_id)

@app.get("/getRequest/{id}", response_model=schemas.Request)
async def getRequest(id: int, db: Session = Depends(get_db)):
    db_request = crud.get_request(db, id)
    if db_request == None:
        raise HTTPException(status_code=400, detail='No request with given id')
    return db_request

@app.post("/createRequest", response_model=schemas.Request)
async def createRequest(request: schemas.RequestCreate, user_id: int, db: Session = Depends(get_db)):
    print(request)
    print(user_id)
    return crud.create_request(db, request, user_id)