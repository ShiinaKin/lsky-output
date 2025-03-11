from sqlalchemy import Column, String, DateTime

from entity.base import Base


class PasswordReset(Base):
    __tablename__ = 'password_resets'

    email = Column(String(255), primary_key=True, index=True)
    token = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'token': self.token,
            'created_at': self.created_at
        }

    def __repr__(self):
        return f"<PasswordReset(email={self.email}, token={self.token}, created_at={self.created_at})>"
