from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, JSON

from entity.base import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, comment='角色组名称')
    is_default = Column(Boolean, nullable=False, default=False, comment='是否默认')
    is_guest = Column(Boolean, nullable=False, default=False, comment='是否为游客组')
    configs = Column(JSON, nullable=False, comment='组配置')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'is_default': self.is_default,
            'is_guest': self.is_guest,
            'configs': self.configs,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __repr__(self):
        return f"<Group(id={self.id}, name={self.name}, is_default={self.is_default}, is_guest={self.is_guest}, " \
               f"configs={self.configs}, created_at={self.created_at}, updated_at={self.updated_at})>"
