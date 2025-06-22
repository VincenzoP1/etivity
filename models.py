from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, CheckConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Utente(Base):
    __tablename__ = 'utenti'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    data_registrazione = Column(Date)
    profili = relationship("Profilo", back_populates="utente")

class Profilo(Base):
    __tablename__ = 'profili'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    eta = Column(Integer)
    utente_id = Column(Integer, ForeignKey('utenti.id'))
    utente = relationship("Utente", back_populates="profili")
    visualizzazioni = relationship("Visualizzazione", back_populates="profilo")
    valutazioni = relationship("Valutazione", back_populates="profilo")
    preferiti = relationship("Preferito", back_populates="profilo")

class Contenuto(Base):
    __tablename__ = 'contenuti'
    id = Column(Integer, primary_key=True)
    titolo = Column(String)
    anno = Column(Integer)
    lingua = Column(String)
    descrizione = Column(Text)
    durata = Column(Integer)
    tipo = Column(String)
    visualizzazioni = relationship("Visualizzazione", back_populates="contenuto")
    valutazioni = relationship("Valutazione", back_populates="contenuto")
    preferiti = relationship("Preferito", back_populates="contenuto")

class Visualizzazione(Base):
    __tablename__ = 'visualizzazioni'
    id = Column(Integer, primary_key=True)
    profilo_id = Column(Integer, ForeignKey('profili.id'))
    contenuto_id = Column(Integer, ForeignKey('contenuti.id'))
    data = Column(Date)
    tempo_visualizzato = Column(Integer)
    profilo = relationship("Profilo", back_populates="visualizzazioni")
    contenuto = relationship("Contenuto", back_populates="visualizzazioni")

class Valutazione(Base):
    __tablename__ = 'valutazioni'
    id = Column(Integer, primary_key=True)
    profilo_id = Column(Integer, ForeignKey('profili.id'))
    contenuto_id = Column(Integer, ForeignKey('contenuti.id'))
    stelle = Column(Integer)
    __table_args__ = (CheckConstraint('stelle >= 1 AND stelle <= 5'),)
    profilo = relationship("Profilo", back_populates="valutazioni")
    contenuto = relationship("Contenuto", back_populates="valutazioni")

class Preferito(Base):
    __tablename__ = 'preferiti'
    id = Column(Integer, primary_key=True)
    profilo_id = Column(Integer, ForeignKey('profili.id'))
    contenuto_id = Column(Integer, ForeignKey('contenuti.id'))
    profilo = relationship("Profilo", back_populates="preferiti")
    contenuto = relationship("Contenuto", back_populates="preferiti")