from sqlalchemy import Column, BigInteger, String, Text, DateTime, func
from entity.base import Base


class FailedJob(Base):
    __tablename__ = 'failed_jobs'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String(255), nullable=False, unique=True)
    connection = Column(Text, nullable=False)
    queue = Column(Text, nullable=False)
    payload = Column(Text, nullable=False)
    exception = Column(Text, nullable=False)
    failed_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "uuid": self.uuid,
            "connection": self.connection,
            "queue": self.queue,
            "payload": self.payload,
            "exception": self.exception,
            "failed_at": self.failed_at
        }

    def __repr__(self):
        return f"<FailedJob(id={self.id}, uuid={self.uuid}, connection={self.connection}, queue={self.queue}, payload={self.payload}, exception={self.exception}, failed_at={self.failed_at})>"
