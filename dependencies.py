from models import MathExpression
from sqlalchemy.orm import Session


def push_expression_to_db(db: Session, expression: MathExpression):
    db.add(expression)
    db.commit()
    db.refresh(expression)
