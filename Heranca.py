class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

class PessoaFisica(Pessoa):
	def __init__(self, CPF, nome, idade):
		Pessoa.__init__(self, nome, idade)
		self.CPF = CPF

p1 = Pessoa('Marcos', 28)
p1.nome
