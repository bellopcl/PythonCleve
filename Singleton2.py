class Singleton:
	__instance = None
	def __init__(self):
		if not Singleton.__instance:
			print('__init__ foi chamado')
		else:
			print('instancia ja criada: ')

	@classmethod
	def obter_instancia(cls):
		if not cls.__instance:
			cls.__instance = Singleton()
		return cls.__instance

s = Singleton()
print('Objeto Criado: ', Singleton.obter_instancia())
s2 = Singleton()