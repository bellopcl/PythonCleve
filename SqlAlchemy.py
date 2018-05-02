from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pessoa(Base):
	__tablename__ = 'pessoa'
	id = Column(Integer, primary_key=True)
	nome = Column(String(200), nullable=False)

	def __repr__(self):
		return 'ID: %d, nome: %s ' %(self.id, self.nome)

class Endereco(Base):
	__tablename__ =  'endereco'
	id = Column(Integer, primary_key=True)
	nome_rua = Column(String(100))
	bairro = Column(String(100))
	cep = Column(String(20))
	id_pessoa = Column(Integer, ForeignKey('pessoa.id'))
	pessoa = relationship(Pessoa)

engine = create_engine('sqlite://banco.db')

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	pessoa = Pessoa(id=1234, nome='Marcos Castro')
	pessoa2 = Pessoa(id=1111, nome='Cleverson')
	print(pessoa)

	Session = sessionmaker(bind=engine)
	session = Session()
	session.add(pessoa)
	session.add(pessoa2)
	session.commit()

		
		