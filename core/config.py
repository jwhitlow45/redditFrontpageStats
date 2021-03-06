import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Client():
    ID = os.getenv('ID')
    SECRET = os.getenv('SECRET')
    AGENT = os.getenv('AGENT')

class SQLEngine():
    CONNECTION_STR = os.getenv('CONNECTION_STR')