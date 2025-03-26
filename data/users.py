from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase 


class User(SqlAlchemyBase ):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    modified_date = Column(DateTime, default=datetime.now)

    jobs = relationship("Jobs", back_populates='user')

    def __init__(self, name, password):
        self.set_password(password)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'
