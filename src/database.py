from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mssql+pyodbc://:Nayan2000#!!@localhost,14330\SQLEXPRESS02,14330/pizza_delivery?driver=ODBC+Driver+17+for+SQL+Server"
server = 'icubesqlserver.database.windows.net'
database = 'aact_db'


username = 'icubesqlserver'
password = 'Icube%40345678'
driver = 'ODBC+Driver+17+for+SQL+Server'  # Adjust the driver based on your setup

# Create a connection string
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
