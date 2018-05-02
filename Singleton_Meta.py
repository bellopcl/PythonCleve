class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instances(cls)
class Teste(metaclass=MetaSingleton):
	pass

t1 = Teste()
t2 = Teste()
print(t1, t2)
		
