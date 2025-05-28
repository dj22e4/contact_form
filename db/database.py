from db.models import Base, Contact, Purpose
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class Database:
    _instance = None

    def __new__(cls, filepath):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, filepath):
        if self._initialized:
            return
        if not (filepath or filepath.endswith('.db')):
            raise ValueError('Invalid database path provided!')
        self._filepath = filepath
        self._engine = None
        self._Session = None
        self._session = None
        self._initialized = True

    def create(self):
        self._engine = create_engine(f'sqlite:///{self._filepath}')
        Base.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine)
        self._session = self._Session()
        return self

    def open(self):
        if self._session or self._engine:
            raise RuntimeError('You must close the open database before performing this action!')
        self._engine = create_engine(f'sqlite:///{self._filepath}')
        self._Session = sessionmaker(bind=self._engine)
        self._session = self._Session()
        return self

    def query(self, model, **filters):
        if not self._session:
            raise RuntimeError('You must create or open a database before performing this action!')
        query = self._session.query(model)
        for key, value in filters.items():
            query = query.filter(getattr(model, key) == value)
        return query.all()

    def add(self, item):
        if not self._session:
            raise RuntimeError('You must create or open a database before performing this action!')
        if not isinstance(item, (Contact, Purpose)):
            raise ValueError('Item must be an instance of type Contact or Purpose!')
        self._session.add(item)
        return self

    def remove(self, item):
        if not self._session:
            raise RuntimeError('You must create or open a database before performing this action!')
        if not isinstance(item, (Contact, Purpose)):
            raise ValueError('Item must be an instance of type Contact or Purpose!')
        self._session.delete(item)
        return self

    def save(self):
        if not self._session:
            raise RuntimeError('You must create or open a database before performing this action!')
        self._session.commit()
        return self

    def close(self):
        if not self._session:
            raise RuntimeError('You must create or open a database before performing this action!')
        self._session.commit()
        self._session.close()
        self._session = None
        self._Session = None
        self._engine = None
        return self