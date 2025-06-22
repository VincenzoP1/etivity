from sqlalchemy.orm import Session
from models import Utente, Contenuto

def crea_utente(session: Session, email: str, password: str):
    utente = Utente(email=email, password=password)
    session.add(utente)
    session.commit()
    return utente

def crea_contenuto(session: Session, titolo: str, anno: int, lingua: str, descrizione: str, durata: int, tipo: str):
    contenuto = Contenuto(
        titolo=titolo, anno=anno, lingua=lingua,
        descrizione=descrizione, durata=durata, tipo=tipo
    )
    session.add(contenuto)
    session.commit()
    return contenuto

def lista_contenuti(session: Session):
    return session.query(Contenuto).all()