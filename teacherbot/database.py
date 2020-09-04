from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from dotenv import dotenv_values

Base = automap_base()

engine = create_engine(URL('postgres', **dotenv_values()))
Base.prepare(engine, reflect=True)
session = Session(engine)

for table in dir(Base.classes):
    if not table.startswith('__'):
        exec(f'{table}=Base.classes.{table}')

if __name__ != '__main__':
    # Delete imports to avoid naming conflicts
    # when importing this file
    del automap_base
    del Session
    del URL
    del create_engine
    del dotenv_values
