from flask import Flask

app = Flask(__name__) #nuevo objeto

@app.route('/') #wrap o un decorador
def index():
	return 'hola mundo 3' #Regresa un string

if __name__ == '__main__':
		app.run(debug = True, port = 8000) #se encarga de ejecutar el servidor 5000