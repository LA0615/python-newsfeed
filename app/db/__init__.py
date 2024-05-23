from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# Debugging: Print the DB_URL to verify it's loaded correctly
db_url = getenv('DB_URL')
if not db_url:
    raise ValueError("DB_URL environment variable is not set")
print(f"DB_URL: {db_url}")

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()