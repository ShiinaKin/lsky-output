from sqlalchemy import Column, String, Text, DateTime

from entity.base import Base


class Config(Base):
    __tablename__ = 'configs'

    name = Column(String(32), primary_key=True, comment='配置名')
    value = Column(Text, nullable=True, comment='配置值')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'value': self.value,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __repr__(self):
        return f"<Config(name={self.name}, value={self.value}, created_at={self.created_at}, updated_at={self.updated_at})>"
