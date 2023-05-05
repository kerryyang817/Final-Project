from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql://username:password@localhost/quality_assurance')

Session = sessionmaker(bind=engine)

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    quantity = Column(Integer)


class Defect(Base):
    __tablename__ = 'defects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


class Inspection(Base):
    __tablename__ = 'inspections'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    defect_id = Column(Integer)

    product = relationship("Product", backref="inspections")
    defect = relationship("Defect", backref="inspections")
