from random import randrange
from temporizador import Temporizador
from configuracion import TAM_PARTICULA, MIN_VIDA_PARTICULA, MAX_VIDA_PARTICULA
from pygame import draw

class Particula(object):
	'''Representa una particula'''
	
	'''Constructor
		color: Color que tendra la particula
		x: Posicion horizontal donde se generara la particula
		y: Posicion vertical donde se generara la particula
		vx: Velocidad horizontal que tendra la particula
		vy: Velocidad vertical que tendra la particula'''
	def __init__(self, color, x, y, vx, vy):
		self.temporizador = Temporizador(randrange(MIN_VIDA_PARTICULA, MAX_VIDA_PARTICULA)) #Tiempo de vida de la particula
		self.muerta = False #Bandera para saber cuando hay que eliminar la particula del sistema
		self.color = color
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
	
	'''Actualiza la vida de la particula y su posicion
		delta: Tiempo de juego, necesario para gestionar el tiempo de vida'''
	def actualizar(self, delta):
		self.temporizador.actualizar(delta)
		
		if self.temporizador.pulso: #Si se acabo el tiempo de vida
			self.muerta = True	#Marcar la particula para ser eliminada
		
		#Actualizar posicion
		self.x += self.vx
		self.y += self.vy
	
	'''Dibuja la particula en la pantalla
		pantalla: Superficie donde se dibujara'''
	def dibujar(self, pantalla):
		draw.rect(pantalla, self.color, (self.x, self.y, TAM_PARTICULA, TAM_PARTICULA))