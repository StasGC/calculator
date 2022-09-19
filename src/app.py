from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from dependencies import push_expression_to_db
from models import MathExpression

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class QueryExpression(BaseModel):
    expression: str


@app.get("/")
def main():
    return JSONResponse(content="Hello world!")


@app.post("/solver/")
def solve(query: QueryExpression, db: Session = Depends(get_db)):
    try:
        answer = eval(str(query.expression))
    except Exception as ex:
        message = f"{query.expression}: Invalid expression"

        expression = MathExpression(expression=message)
        push_expression_to_db(db, expression)

        return JSONResponse(
            status_code=400,
            content={"message": f"{message}. Error: {ex}"},
        )

    expression = MathExpression(expression=f"{query.expression}={answer}")
    push_expression_to_db(db, expression)
    return expression


@app.get("/history/")
def read_expressions(db: Session = Depends(get_db)):
    return db.query(MathExpression).all()

