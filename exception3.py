class TransacaoInvalida(Exception):
	def __init__(self, saldo_atual, quantidade):
		super().__init__('Sua Conta não tem ${}'.format(quantidade))
		self.quantidade = quantidade
		self.saldo_atual = saldo_atual

	def excesso(self):
		return self.quantidade - self.saldo_atual

try:
	raise TransacaoInvalida(10, 20)
except TransacaoInvalida as e:
	print('Você não tem saldo suficiente, ${}'.format(e.excesso()))