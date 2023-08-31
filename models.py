from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, DECIMAL, BigInteger, DATE, FLOAT
from database import Base

class User(Base):
    __tablename__ = 'monk_table'

    id = Column(BigInteger, primary_key=True, index=True)
    project_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    type_id = Column(BigInteger, nullable=False)
    source_type_id = Column(BigInteger, nullable=False)
    status_code = Column(Integer)
    name = Column(String(255), nullable=False)
    lat = Column(DECIMAL(10, 7), nullable=False)
    lon = Column(DECIMAL(10, 7), nullable=False)
    coord_x = Column(DECIMAL(9, 2))
    coord_y = Column(DECIMAL(9, 2))
    utm_zone = Column(String(3))
    ground_level = Column(DECIMAL(15, 7))
    datum = Column(String(10))
    creation_date = Column(DATE)
    survey_company = Column(String(255))
    process_id = Column(BigInteger)
    version = Column(FLOAT, default=1.10)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP, onupdate=True)
    creation_date = Column(DATE)
    survey_company = Column(String(255))
    process_id = Column(BigInteger)
    version = Column(FLOAT, default=1.10)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP, onupdate=True)

