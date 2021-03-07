from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import pyodbc

from shared.core import config

# Set pooling to false to allow pyodbc to properly resolve connections
pyodbc.pooling = False
engine=create_engine(config.SQLEngine.CONNECTION_STR,)
Base = declarative_base()
Session = sessionmaker(bind=engine)

@contextmanager
def session_manager():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()