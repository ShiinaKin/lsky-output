from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from entity import *


def get_engine(db_url: str) -> Engine:
    return create_engine(db_url)

def get_session(engine: Engine) -> sessionmaker:
    return sessionmaker(bind=engine)

def output_schema(sql_session: Session) -> dict:
    config_schema = sql_session.query(Config).all()
    group_schema = sql_session.query(Group).all()
    group_strategy_schema = sql_session.query(GroupStrategy).all()
    user_schema = sql_session.query(User).all()
    personal_access_token_schema = sql_session.query(PersonalAccessToken).all()
    migration_schema = sql_session.query(Migration).all()
    failed_job_schema = sql_session.query(FailedJob).all()
    password_reset_schema = sql_session.query(PasswordReset).all()
    strategy_schema = sql_session.query(Strategy).all()
    album_schema = sql_session.query(Album).all()
    image_schema = sql_session.query(Image).all()
    output = {
        "config": [row.to_dict() for row in config_schema],
        "group": [row.to_dict() for row in group_schema],
        "group_strategy": [row.to_dict() for row in group_strategy_schema],
        "user": [row.to_dict() for row in user_schema],
        "personal_access_token": [row.to_dict() for row in personal_access_token_schema],
        "migration": [row.to_dict() for row in migration_schema],
        "failed_job": [row.to_dict() for row in failed_job_schema],
        "password_reset": [row.to_dict() for row in password_reset_schema],
        "strategy": [row.to_dict() for row in strategy_schema],
        "album": [row.to_dict() for row in album_schema],
        "image": [row.to_dict() for row in image_schema],
    }
    sql_session.close()
    return output