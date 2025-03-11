from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.types import JSON

from entity.base import Base, TinyInt


class Strategy(Base):
    __tablename__ = 'strategies'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    key = Column(TinyInt(unsigned=True), nullable=False)
    name = Column(String(64), nullable=False, comment='策略名称')
    intro = Column(String(255), nullable=False, default='', comment='简介')
    configs = Column(JSON, nullable=False, comment='策略配置')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'key': self.key,
            'name': self.name,
            'intro': self.intro,
            'configs': self.configs,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f"<Strategy(id={self.id}, key={self.key}, name={self.name}, intro={self.intro}, configs={self.configs}, created_at={self.created_at}, updated_at={self.updated_at})>"
