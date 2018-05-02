import sqlite3

class BancoDeDados:
	def __init__(self, nome='banco.db'):
		self.nome, self.conexao = nome, None

	def conecta(self):
		self.conexao = sqlite3.connect(self.nome)

	def desconecta(self):
		try:
			self.conexao.close()
		except AttributeError:
			pass

	def criar_tabelas(self):
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NO NULL, 
                   senha VARCHAR(20) NOT NULL,
                   cpf VARCHAR(11) UNIQUE NOT NULL, 
                   email TEXT NOT NULL
                   );
				""")
		except AttributeError:
			print('Faça a conexao do banco de dados')

	def inserir_cliente(self, nome, cpf, email):
		try:
			cursor = self.conexao.cursor()
			try:
				cursor.execute("""
                INSERT INTO clientes(nome, cpf, email) VALUES (?,?,?)
				""", (nome, cpf, email))
			except sqlite3.IntegrityError:
				print('O cpd %s já existe! ' % cpf)

			self.conexao.commit()
			
		except AttributeError:
			print('Faça a conexao do banco antes de inserir clientes')

	def buscar_cliente(self, cpf):
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""SELECT *FROM clientes;""")
			for linha in cursor.fetchall():
				if linha[2] == cpf:
					print('Cliente %s encontrado.' % linha[1])
					break
		except AttributeError:
			print('Faça a conexao do banco antes de buscar cliente. ')

	def buscar_email(self, email):
		try:
			cursor = self.conexao.cursor()

			cursor.execute(""" SELECT *FROM clientes;""")
			for linha in cursor.fetchall():
				if linha[3] == email:
					print(' Cliente %s encontrado! ' %linha[1])
					break
		except AttributeError:
			print('Faça a conexao do banco antes de buscar cliente.')

	def apagar_cliente(self, cpf):
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""DELETE FROM clientes WHERE cpf = ?""", (cpf,))
			self.conexao.commit()

			print('Cliente cpf %s apagado com sucesso! ' % cpf)
			
		except AttributeError:
			print('Cliente não encontrado:')

	def Busca_Cliente_Cpf(self, cpf):
		try:
			cursor = self.conexao.cursor()

			cursor.execute("SELECT *FROM clientes WHERE cpf=?", [(cpf)])

			cliente = cursor.fetchone()

			if cliente:
				print('Cliente %s encontrado. ' % cliente[1])
			else:
				print('cliente não encontrado.')

		except AttributeError:
			print('Faça a conexao do banco antes de buscar clientes')

	def login(username, senha):
		try:
			cursor = self.conexao.cursor()
			sql = 'SELECT *FROM clientes WHERE nome=? and senha=?'
			cliente = cursor.execute(sql, [username, senha]).fetchone()
			if cliente:
				return True
			return False
		except AttributeError:
			print('Faça a conexao do banco.')