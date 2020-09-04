from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from dotenv import dotenv_values

Base = automap_base()

engine = create_engine(URL('postgres', **dotenv_values()))
Base.prepare(engine, reflect=True)
session = Session(engine)
