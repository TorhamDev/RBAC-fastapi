from fastapi import FastAPI
from src.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


@app.get("/")
def test():
    return {"message": "Hello World!"}
