class Livro(object):
	def __init__(self, titulo, lancamento, autor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.autor = autor

class Filme(object):
	def __init__(self, titulo, lancamento, diretor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.diretor = diretor

class Pato():
	def quack(self):
		print('Quack, quack')

class Pessoa():
	def quack(self):
		print('Eu faço quack igual a um Pato')

'''def fazer_quack(obj):
	if isinstance(obj, Pato):
		obj.quack()
	else:
		print('isso tem que ser um Pato')
'''
'''
def fazer_quack(obj):
	#LBYL - Não Pythonico
	if hasattr(obj, 'quack'):
		if callable(obj.quack):
			obj.quack()
'''
'''
#EAFP - Easier to ask for forgiveness than permission

'''
def fazer_quack(obj):
	try:
		obj.quack()
	except AttributeError as e:
		print(e)


pato = Pato()
fazer_quack(pato)
'''pato.quack()
'''
Pessoa = Pessoa()
fazer_quack(Pessoa)
'''Pessoa.quack()'''