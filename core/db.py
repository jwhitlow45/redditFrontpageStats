from sqlalchemy import create_engine
import config

engine = create_engine(config.SQLEngine.CONNECTION_STR, echo=True)
