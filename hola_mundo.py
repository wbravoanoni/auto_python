from flask import Flask
from flask import request

app = Flask(__name__) #nuevo objeto

@app.route('/') #wrap o un decorador
def index():
	return '<h1>hola mundo 4</h1>' #Regresa un string

#http://localhost:8000/params?param1=Winston&param2=Bravo&param3=26

@app.route('/params') #wrap o un decorador
def params():
	param = request.args.get('param1','no tiene este parametro')
	param2 = request.args.get('param2','no tiene este parametro')
	param3 = request.args.get('param3','no tiene este parametro')
	return 'El parametro es Nombre: {} Apellido: {} Edad: {}'.format(param,param2,param3) #Regresa un string	

if __name__ == '__main__':
		app.run(debug = True, port = 8000) #se encarga de ejecutar el servidor 5000