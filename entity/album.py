from sqlalchemy import Column, BigInteger, String, DateTime

from entity.base import Base


class Album(Base):
    __tablename__ = 'albums'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, comment='用户')
    name = Column(String(64), nullable=False, comment='名称')
    intro = Column(String(255), nullable=False, default='', comment='简介')
    image_num = Column(BigInteger, nullable=False, default=0, comment='图片数量')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'intro': self.intro,
            'image_num': self.image_num,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f"<Album(id={self.id}, user_id={self.user_id}, name={self.name}, intro={self.intro}, image_num={self.image_num}, created_at={self.created_at}, updated_at={self.updated_at})>"
