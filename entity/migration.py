from sqlalchemy import Column, Integer, String
from entity.base import Base


class Migration(Base):
    __tablename__ = 'migrations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    migration = Column(String(255), nullable=False)
    batch = Column(Integer, nullable=False)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'migration': self.migration,
            'batch': self.batch
        }

    def __repr__(self):
        return f"<Migration(id={self.id}, migration={self.migration}, batch={self.batch})>"
