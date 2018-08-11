from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class CommonColumns(Base):

    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now(), onupdate=func.now())
    _etag = Column(String(40))

class Pacientes(CommonColumns):
    __tablename__ = 'pacientes'
    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(11), nullable=False)
    nome = Column(String(120), nullable=False)
    dt_nasc = Column(DateTime, nullable=True)

