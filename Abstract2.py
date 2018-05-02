from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

	@abstractmethod
	def dizer_algo(self):
		return 'Eu sou um Animal '

class Cachorro(Animal):
	def dezer_algo(self):
		s = super(Cachorro, self).dizer_algo()
		return '%s - %s' % (s, 'AU AU')

c = Cachorro()
print(c.dizer_algo())
		
	