from sqlalchemy import Column, BigInteger, String, Boolean, Numeric, DateTime, JSON

from entity.base import Base, TinyInt


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    group_id = Column(BigInteger, nullable=True, comment='角色组')
    name = Column(String(255), nullable=False, comment='姓名')
    email = Column(String(255), nullable=False, unique=True, comment='邮箱')
    password = Column(String(255), nullable=False, comment='密码')
    remember_token = Column(String(100), nullable=True)
    is_adminer = Column(Boolean, nullable=False, default=False, comment='是否为管理员')
    capacity = Column(Numeric(20, 2), nullable=False, default=0.00, comment='总容量(kb)')
    url = Column(String(255), nullable=False, default='', comment='个人主页')
    configs = Column(JSON, nullable=False, comment='配置')
    image_num = Column(BigInteger, nullable=False, default=0, comment='图片数量')
    album_num = Column(BigInteger, nullable=False, default=0, comment='相册数量')
    registered_ip = Column(String(255), nullable=False, default='', comment='注册IP')
    status = Column(TinyInt(unsigned=True), nullable=False, default=1, comment='状态')
    email_verified_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'group_id': self.group_id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'remember_token': self.remember_token,
            'is_adminer': self.is_adminer,
            'capacity': self.capacity,
            'url': self.url,
            'configs': self.configs,
            'image_num': self.image_num,
            'album_num': self.album_num,
            'registered_ip': self.registered_ip,
            'status': self.status,
            'email_verified_at': self.email_verified_at,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f"<User(id={self.id}, group_id={self.group_id}, name={self.name}, email={self.email}, password={self.password}, remember_token={self.remember_token}, is_adminer={self.is_adminer}, capacity={self.capacity}, url={self.url}, configs={self.configs}, image_num={self.image_num}, album_num={self.album_num}, registered_ip={self.registered_ip}, status={self.status}, email_verified_at={self.email_verified_at}, created_at={self.created_at}, updated_at={self.updated_at})>"
