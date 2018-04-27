from pygame import Rect
from configuracion import GRAVEDAD, GRAVEDAD_MAXIMA, ALTURA

class ObjetoEscenario(object):
	'''Todos los objetos que se puedan poner en el escenario deberan heredar de esta clase
		tiene los comportamientos basicos de los objetos'''
	
	'''Constructor
		imagen: graficos del objeto
		x: posicion horizontal donde aparecera el objeto
		y: posicion vertical donde aparecera el objeto'''
	def __init__(self, imagen, x, y):
		self.imagen = imagen
		self.cuerpo = Rect(x, y, imagen.get_width(), imagen.get_height())
		
		self.enSuelo = False
		self.vy = 0
	
	'''Dibuja el objeto en la pantalla
		pantalla: superficie donde se dibujara'''
	def dibujar(self, pantalla):
		pantalla.blit(self.imagen, self.cuerpo)
	
	'''Actualiza el objeto
		delta: Tiempo de juego, usado para algunas funciones'''
	def actualizar(self, delta):
		self.aplicarGravedad()
		self.comprobarSuelo()
		self.mover()
	
	'''Mueve la manzana'''
	def mover(self):
		self.cuerpo.move_ip(0, self.vy)
	
	'''Comprueba si la manzana esta en el suelo'''
	def comprobarSuelo(self):
		if self.cuerpo.bottom + self.vy > ALTURA:
			self.cuerpo.bottom = ALTURA
			self.enSuelo = True
	
	'''Si la manzana no esta en el suelo, aplicar gravedad.
		Comprueba que la manzana no supere un limite de velocidad vertical'''
	def aplicarGravedad(self):
		if not self.enSuelo:
			if self.vy > GRAVEDAD_MAXIMA: #Limite para la gravedad
				self.vy = GRAVEDAD_MAXIMA
			else:
				self.vy += GRAVEDAD #Si no ha llegado al limite aplicar la gravedad normalmente
		else:
			self.vy = 0

class Manzana(ObjetoEscenario):
	'''Sera la comida del gato'''
	
	'''Constructor
		imagen: graficos del objeto
		x: posicion horizontal donde aparecera el objeto
		y: posicion vertical donde aparecera el objeto'''
	def __init__(self, imagen, x, y):
		ObjetoEscenario.__init__(self, imagen, x, y)
	
	'''Actualiza la manzana
		delta: Tiempo de juego, usado para algunas funciones'''
	def actualizar(self, delta):
		ObjetoEscenario.actualizar(self, delta)