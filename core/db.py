from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, Float, String, Boolean
import config

engine = create_engine(config.SQLEngine.CONNECTION_STR, echo=True)
meta=MetaData()

posts = Table(
    'posts', meta,
    Column('id', String, primary_key=True)
)