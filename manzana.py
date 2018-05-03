from objeto_escenario import ObjetoEscenario
from configuracion import COMIDA

class Manzana(ObjetoEscenario):
	'''Sera la comida del gato'''
	
	'''Constructor
		imagen: graficos del objeto
		x: posicion horizontal donde aparecera el objeto
		y: posicion vertical donde aparecera el objeto
		suelo: posicion del suelo'''
	def __init__(self, imagen, x, y, suelo):
		ObjetoEscenario.__init__(self, imagen, x, y, suelo, COMIDA)
	
	'''Actualiza la manzana
		delta: Tiempo de juego, usado para algunas funciones'''
	def actualizar(self, delta):
		ObjetoEscenario.actualizar(self, delta)