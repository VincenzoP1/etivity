from sqlalchemy import create_engine
from models import Base

def init_db():
    engine = create_engine('sqlite:///streaming.db')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()