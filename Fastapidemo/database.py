from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://postgres:123@localhost/mydb"  #postgresql://username:password@host:port/database_name
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

