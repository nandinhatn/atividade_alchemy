from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

from sqlalchemy.orm  import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine  = create_engine('sqlite:///habilidades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base= declarative_base()
Base.query= db_session.query_property()


class Programador(Base):
    __tablename__ = 'programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    email = Column(String(40))

    def __repr__(self):
        return '<Programador {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()
        pass

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Habilidade(Base):
    __tablename__= 'habilidade'
    id= Column (Integer , primary_key=True)
    nome = Column (String(40))

    def __repr__(self):
        return '<Habilidade {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def deletar(self):
        db_session.delete(self)
        db_session.commit()


class Programador_Habilidade(Base):
    __tablename__= 'programador_habilidade'
    id= Column (Integer, primary_key= True)
    programador_id = Column(Integer, ForeignKey('programador.id'))
    habilidade_id = Column(Integer, ForeignKey('habilidade.id'))
    programador = relationship("Programador")
    habilidade = relationship("Habilidade")


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()