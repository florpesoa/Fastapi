from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:2468@localhost:3306/Application'

engine=create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,  bind=engine) #para poder interactuar con la DB

Base= declarative_base()
