from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase 


class Jobs(SqlAlchemyBase ):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String, nullable=True)
    work_size = Column(Integer, nullable=True, default=0)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, default=datetime.now)
    is_finished = Column(Boolean, default=True)
    team_leader = Column(Integer, ForeignKey("users.id"))

    user = relationship('User')

    def __repr__(self):
        return f'<Job> {self.job}'
