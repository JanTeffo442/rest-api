import sys, os
import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://myuser:pass@localhost/pure_sql')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Computers(Base):
    __tablename__ = 'computers'
    id = Column(Integer, primary_key=True)
    hard_drive_type = Column(String)
    processor = Column(String)
    amount_ram = Column(String)
    max_ram = Column(String)
    hard_drive_size = Column(String)
    form_factor = Column(String)

    def __init__(self, id, hard_drive_type, processor, amount_ram, max_ram,hard_drive_size, form_factor):
        self.id = id
        self.hard_drive_type = hard_drive_type
        self.processor = processor
        self.amount_ram = amount_ram
        self.max_ram = max_ram
        self.hard_drive_size = hard_drive_size
        self.form_factor = form_factor
    
    def save_computer(self):
        session.add(self)
        session.commit()

    def __repr__(self):
        return f'Computer: {self.id}'

Base.metadata.create_all(engine)
#add_computer = Computers(1,"ssd","intel dual core", "5GB", '64 GB','1TB', "mini")
#add_computer2 = Computers(2,"hdd","amd", "8GB","16GB", "500GB","medium")
add_computer3 = Computers(3,"ssd","intel atom", "2GB","16GB", "256GB","medium")
#add_computer.save_computer()
#add_computer2.save_computer()
add_computer3.save_computer()
session.commit()


#print(add_computer.save_computer())