from sqlalchemy import Integer, Column
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)

