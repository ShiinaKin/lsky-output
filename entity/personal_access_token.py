from sqlalchemy import Column, BigInteger, String, Text, DateTime

from entity.base import Base


class PersonalAccessToken(Base):
    __tablename__ = 'personal_access_tokens'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tokenable_type = Column(String(255), nullable=False)
    tokenable_id = Column(BigInteger, nullable=False)
    name = Column(String(255), nullable=False)
    token = Column(String(64), nullable=False, unique=True)
    abilities = Column(Text, nullable=True)
    last_used_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'tokenable_type': self.tokenable_type,
            'tokenable_id': self.tokenable_id,
            'name': self.name,
            'token': self.token,
            'abilities': self.abilities,
            'last_used_at': self.last_used_at,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f"<PersonalAccessToken(id={self.id}, tokenable_type={self.tokenable_type}, tokenable_id={self.tokenable_id}, name={self.name}, token={self.token}, abilities={self.abilities}, last_used_at={self.last_used_at}, created_at={self.created_at}, updated_at={self.updated_at})>"
