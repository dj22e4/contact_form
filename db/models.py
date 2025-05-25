from sqlalchemy import Column, Integer, String, Date, Text, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import date

Base = declarative_base()

contact_purposes = Table(
    'contact_purposes',
    Base.metadata,
    Column('contact_id', Integer, ForeignKey('contacts.id'), primary_key=True),
    Column('purpose_id', Integer, ForeignKey('purposes.id'), primary_key=True)
)

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, default=lambda: date.today(), index=True)
    last_name = Column(String, nullable=False, index=True)
    first_name = Column(String, nullable=False, index=True)
    middle_initial = Column(String, nullable=True)
    street_address = Column(String, nullable=False)
    apartment = Column(String, nullable=True)
    city = Column(String, nullable=False, index=True)
    state = Column(String, nullable=False, index=True)
    zip_code = Column(String, nullable=False, index=True)
    phone = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    purposes = relationship('Purpose', secondary=contact_purposes, backref='contacts')
    follow_up_date = Column(Date, nullable=True)
    comments = Column(Text, nullable=True)

class Purpose(Base):
    __tablename__ = 'purposes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)