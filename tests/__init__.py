import config
from sqlalchemy import create_engine

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=False)