from configuracion import PARTICULAS_EN_EXPLOSION, VELOCIDAD_PARTICULA
from particula import Particula
from random import randrange

class SistemaParticulas(object):
	'''Gestor de particulas'''
	
	'''Constructor'''
	def __init__(self):
		self.particulas = []
	
	'''Dibuja las particulas en la pantalla
		pantalla: Superficie donde se dibujaran las particulas'''
	def dibujar(self, pantalla):
		for particula in self.particulas:
			particula.dibujar(pantalla)
	
	'''Actualiza las particulas
		delta: Tiempo de juego, necesario para gestionar el tiempo de vida de las particulas'''
	def actualizar(self, delta):
		for particula in self.particulas:
			particula.actualizar(delta)
			if particula.muerta:
				self.particulas.remove(particula)
	
	'''Anade una serie de particulas con una direccion aleatoria con un color y una posicion determinado
		color: Color de la particula
		x: Posicion horizontal
		y: Posicion vertical'''
	def explosionParticulas(self, color, x, y):
		for i in range(PARTICULAS_EN_EXPLOSION):
			self.particulas.append(Particula(color, x, y, randrange(-VELOCIDAD_PARTICULA, VELOCIDAD_PARTICULA), randrange(-VELOCIDAD_PARTICULA, VELOCIDAD_PARTICULA)))
