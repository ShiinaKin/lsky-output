from sqlalchemy import Column, Integer, BigInteger, String, Boolean, Numeric, DateTime

from entity.base import Base, TinyInt


class Image(Base):
    __tablename__ = 'images'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=True, comment='用户')
    album_id = Column(BigInteger, nullable=True, comment='相册')
    group_id = Column(BigInteger, nullable=True, comment='角色组')
    strategy_id = Column(BigInteger, nullable=True, comment='策略')
    key = Column(String(255), nullable=False, unique=True, index=True, comment='key')
    path = Column(String(255), nullable=False, comment='保存路径')
    name = Column(String(255), nullable=False, comment='保存名称')
    origin_name = Column(String(255), nullable=False, default='', comment='原始名称')
    alias_name = Column(String(255), nullable=False, default='', comment='别名')
    size = Column(Numeric(8, 2), nullable=False, default=0.00, comment='图片大小(kb)')
    mimetype = Column(String(32), nullable=False, comment='文件类型')
    extension = Column(String(32), nullable=False, comment='文件后缀')
    md5 = Column(String(32), nullable=False, index=True, comment='文件MD5')
    sha1 = Column(String(255), nullable=False, index=True, comment='文件SHA1')
    width = Column(Integer, nullable=False, default=0, comment='宽')
    height = Column(Integer, nullable=False, default=0, comment='高')
    permission = Column(TinyInt(), nullable=False, default=0, comment='访问权限')
    is_unhealthy = Column(Boolean, nullable=False, default=0, comment='是否为不健康的')
    uploaded_ip = Column(String(255), nullable=False, default='', comment='上传IP')
    created_at = Column(DateTime, nullable=True, index=True)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'album_id': self.album_id,
            'group_id': self.group_id,
            'strategy_id': self.strategy_id,
            'key': self.key,
            'path': self.path,
            'name': self.name,
            'origin_name': self.origin_name,
            'alias_name': self.alias_name,
            'size': self.size,
            'mimetype': self.mimetype,
            'extension': self.extension,
            'md5': self.md5,
            'sha1': self.sha1,
            'width': self.width,
            'height': self.height,
            'permission': self.permission,
            'is_unhealthy': self.is_unhealthy,
            'uploaded_ip': self.uploaded_ip,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f"<Image(id={self.id}, user_id={self.user_id}, album_id={self.album_id}, group_id={self.group_id}, strategy_id={self.strategy_id}, key={self.key}, path={self.path}, name={self.name}, origin_name={self.origin_name}, alias_name={self.alias_name}, size={self.size}, mimetype={self.mimetype}, extension={self.extension}, md5={self.md5}, sha1={self.sha1}, width={self.width}, height={self.height}, permission={self.permission}, is_unhealthy={self.is_unhealthy}, uploaded_ip={self.uploaded_ip}, created_at={self.created_at}, updated_at={self.updated_at})>"
