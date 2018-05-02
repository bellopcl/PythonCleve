from abc import ABCMeta, abstractmethod

class MinhaClasseAbstrata(metaclass=ABCMeta):
	@abstractmethod
	def fazer_algo(self):
		pass
