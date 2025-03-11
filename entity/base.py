from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TypeDecorator

Base = declarative_base()

class TinyInt(TypeDecorator):
    impl = Integer

    def __init__(self, unsigned=False, **kw):
        self.unsigned = unsigned
        TypeDecorator.__init__(self, **kw)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            from sqlalchemy.dialects.mysql import TINYINT
            return dialect.type_descriptor(TINYINT(unsigned=self.unsigned))
        elif dialect.name == 'postgresql':
            from sqlalchemy.dialects.postgresql import SMALLINT
            return dialect.type_descriptor(SMALLINT())
        else:
            return dialect.type_descriptor(self.impl)
