from sqlalchemy import Column, Integer, String

from database import Base


class MathExpression(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String)


