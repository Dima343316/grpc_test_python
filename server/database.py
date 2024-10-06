from sqlalchemy import create_engine, Column, Integer, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()
Base = declarative_base()


class GRPCData(Base):
    __tablename__ = 'grpc_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    PacketSeqNum = Column(BigInteger)
    RecordSeqNum = Column(BigInteger)
    PacketTimestamp = Column(BigInteger)
    Decimal1 = Column(Float)
    Decimal2 = Column(Float)
    Decimal3 = Column(Float)
    Decimal4 = Column(Float)
    RecordTimestamp = Column(BigInteger)

def get_session():
    db_username = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('POSTGRES_NAME')

    # Формируем строку подключения
    database_url = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

    # Устанавливаем соединение с базой данных
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()