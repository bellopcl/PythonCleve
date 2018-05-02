'''def algo():
	raise Exception('excecao')
try:
	algo()
except:
	print('Eu peguei uma excecao')
	print('excecutado apos a excecao')'''

def divisao(divisor):
	try:
		if divisor == 13:
			raise ValueError('13 não é legal')

		return 10 / divisor
	except ZeroDivisionError:
		return 'Divisao por zero'
	except TypeError:
		return 'Entre com um valor numerico'
	except ValueError:
		print('Não utilize o numero 13')
		raise

print(divisao(13))
