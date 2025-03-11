from sqlalchemy import Column, BigInteger

from entity.base import Base

class GroupStrategy(Base):
    __tablename__ = 'group_strategy'

    group_id = Column(BigInteger, primary_key=True, nullable=False, comment='角色组')
    strategy_id = Column(BigInteger, primary_key=True, nullable=False, comment='策略')

    def to_dict(self) -> dict:
        return {
            'group_id': self.group_id,
            'strategy_id': self.strategy_id,
        }

    def __repr__(self):
        return f"<GroupStrategy(group_id={self.group_id}, strategy_id={self.strategy_id})>"
