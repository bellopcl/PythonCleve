from bottle import Bottle, route, run

#app = Bottle()

#@app.route('/')
@route('/')
def index():
	return '<h1>Hello Word<h1>'

@route('/python')
def python():
	return return '<h1>Curso de python<h1>'

if __name__ == '__main__':
	
	run(host='localhost', port=8080, debug=True)
