from database import BancoDeDados

if __name__=="__main__":
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_cliente('Cleverson', '04208857900', 'bellopcl@gmail.com')
	banco.inserir_cliente('Tomas', '12208857900', 'Cleverson@gmail.com')
	banco.buscar_cliente('12208857900')
	banco.buscar_email('Cleverson@gmail.com')
	#banco.apagar_cliente('12208857900')
	#banco.Busca_Cliente_Cpf('12208857900')
	banco.desconecta()