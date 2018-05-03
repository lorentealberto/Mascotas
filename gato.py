from pygame import Rect, transform

from utilidades import cargarImagen
from configuracion import SIZE, VELOCIDAD_GATO

class Gato(object):
	'''Clase que representa la mascota
	Fecha: 25/04/2018
	Autor: Alberto Escribano Lorente'''

	'''Constructor'''
	def __init__(self, suelo):
		self.imagen = cargarImagen("gato", 4)

		#Crea el cuerpo del gato, se usara para gestionar el movimiento y las colisiones
		self.cuerpo = Rect(SIZE[0] / 2 - self.imagen.get_width() / 2, #POSICION X
						suelo - self.imagen.get_height() + 5, #POSICION Y
						self.imagen.get_width(), #ANCHURA
						self.imagen.get_height()) #ALTURA
		self.hambre = 0
		self.maxHambre = 100
		self.objetivo = None
		self.vx = 0
		self.volteado = False

	'''Dibuja el gato en la pantalla
	pantalla: superficie donde se dibujara'''
	def dibujar(self, pantalla):
		pantalla.blit(transform.flip(self.imagen, self.volteado, False), self.cuerpo)

	'''Actualiza todos los elementos
	delta: tiempo de juego, necesario para algunas acciones'''
	def actualizar(self, delta, controles, objetos, sistemaParticulas):
		self.buscarComida(objetos)
		self.irAObjetivo(objetos, sistemaParticulas)
		self.mover()
	
	'''Mueve el gato'''
	def mover(self):
		self.cuerpo.move_ip(self.vx, 0)
	
	'''Busca la pieza de comida mas cercana
		objetos Lista de elementos donde buscara la comida'''
	def buscarComida(self, objetos):
		if self.hambre < self.maxHambre and self.objetivo == None:
			self.objetivo = objetos.obtenerComidaMasCercana(self.cuerpo.x)
	
	'''Va al objetivo seleccionado
		objetos: Se utiliza para borrar el objetivo una vez que haya llegado a el
		sistemaParticulas: Se utiliza para generar una explosion una vez que haya llegado a el'''
	def irAObjetivo(self, objetos, sistemaParticulas):
		if self.objetivo != None:
			if self.cuerpo.right < self.objetivo.cuerpo.left: #Si la comida esta a la derecha del gato
				self.vx = VELOCIDAD_GATO
				self.volteado = False
			elif self.cuerpo.left > self.objetivo.cuerpo.right: #Si la comida esta a la izquierda del gato
				self.vx = -VELOCIDAD_GATO
				self.volteado = True
			else: #Si el gato ha llegado a la comida
				if self.cuerpo.colliderect(self.objetivo.cuerpo): #Comprobar que el gato toque la comida
					self.vx = 0 #Frenar al gato
					#Generar explosion de particulas
					sistemaParticulas.explosionParticulas((255, 0, 0), #Color de la particula
															self.objetivo.cuerpo.x + self.objetivo.cuerpo.width / 2, #Posicion horizontal
															self.objetivo.cuerpo.y + self.objetivo.cuerpo.height / 2) #Posicion vertical
					objetos.elementos.remove(self.objetivo) #Eliminar la comida de la lista de objetos accesibles
					self.objetivo = None #Resetear objetivo
				