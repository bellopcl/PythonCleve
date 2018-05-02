class MetaClasse(type):
	def __call__(cls, *args, **kargs):
		print('Minha MetaClasse ', args)
		return type.__call__(cls, *args, **kargs)

class int(metaclass=MetaClasse):
	def __init__(self, x, y):
		self.x = x
		self.y = y

obj = int(4, 5)