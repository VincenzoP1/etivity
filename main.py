from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from crud import crea_utente, crea_contenuto, lista_contenuti
from db_setup import init_db

def main():
    init_db()
    engine = create_engine('sqlite:///streaming.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("1. Aggiungi utente")
    print("2. Aggiungi contenuto")
    print("3. Lista contenuti")

    scelta = input("Seleziona un'opzione: ")
    if scelta == '1':
        email = input("Email: ")
        password = input("Password: ")
        crea_utente(session, email, password)
        print("Utente creato.")
    elif scelta == '2':
        titolo = input("Titolo: ")
        anno = int(input("Anno: "))
        lingua = input("Lingua: ")
        descrizione = input("Descrizione: ")
        durata = int(input("Durata (min): "))
        tipo = input("Tipo (film/serie): ")
        crea_contenuto(session, titolo, anno, lingua, descrizione, durata, tipo)
        print("Contenuto aggiunto.")
    elif scelta == '3':
        contenuti = lista_contenuti(session)
        for c in contenuti:
            print(f"{c.id} - {c.titolo} ({c.tipo})")

if __name__ == '__main__':
    main()