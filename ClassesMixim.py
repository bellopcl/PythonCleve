class livro(object):
	"""dnome, conteudotring for livro"""
	def __init__(self, nome, conteudo):
		self.nome = nome
		self.conteudo = conteudo

class LivroHTMLMixin(object):
	def rendenizar(self):
		return ('<html><title>%s</title><body>%s</body></html') % (self.nome, self.conteudo)

class LivroHTML(livro, LivroHTMLMixin):
	pass

livro_html = LivroHTML('algum livro', 'blalalal')
print(livro_html.rendenizar())
		
		
