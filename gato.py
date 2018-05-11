from pygame import Rect, transform, draw
from random import randrange

from utilidades import cargarImagen
from temporizador import Temporizador
from configuracion import ANCHURA, VELOCIDAD_GATO, HAMBRE_MAXIMA, ESCALA_GATO, PERDIDA_DE_ENERGIA
from configuracion import TIEMPO_CAMBIO_OBJETIVO, TIEMPO_EXCREMENTO, TIEMPO_DESGASTE_ENERGIA

class Gato(object):
	'''Clase que representa la mascota
	Fecha: 25/04/2018
	Autor: Alberto Escribano Lorente'''

	'''Constructor'''
	def __init__(self, suelo):
		self.imagen = cargarImagen("gato", ESCALA_GATO)
		self.volteado = False

		#Crea el cuerpo del gato, se usara para gestionar el movimiento y las colisiones
		self.cuerpo = Rect(ANCHURA / 2 - self.imagen.get_width() / 2, #POSICION X
						suelo - self.imagen.get_height() + 5, #POSICION Y
						self.imagen.get_width(), #ANCHURA
						self.imagen.get_height()) #ALTURA
		self.hambre = 100
		self.maxHambre = HAMBRE_MAXIMA
		
		self.vx = 0
		
		self.objetivo = None
		
		#Temporizadores
		self.tempoObjetivo = Temporizador(TIEMPO_CAMBIO_OBJETIVO)
		self.tempoExcremento = Temporizador(TIEMPO_EXCREMENTO)
		self.tempoDesgasteEnergia = Temporizador(TIEMPO_DESGASTE_ENERGIA)
		
		self.temporizadores = [self.tempoObjetivo, self.tempoExcremento, self.tempoDesgasteEnergia]

	'''Dibuja el gato en la pantalla
		pantalla: superficie donde se dibujara'''
	def dibujar(self, pantalla):
		pantalla.blit(transform.flip(self.imagen, self.volteado, False), self.cuerpo)

	'''Actualiza todos los elementos
		delta: tiempo de juego, necesario para algunas acciones
		objetos: Lista de objetos del escenario
		sistemaParticulas: Sistema de particulas del juego'''
	def actualizar(self, delta, objetos, sistemaParticulas):
		self.actualizarTemporizadores(delta)
		
		self.definirObjetivo(objetos)
		self.irAObjetivo(objetos, sistemaParticulas)	
		self.mover()
		self.excretar(objetos)
		
		if self.tempoDesgasteEnergia.pulso:
			self.hambre -= PERDIDA_DE_ENERGIA
			if self.hambre < 0:
				self.hambre = 0
	
	'''Expulsa un excremento cada cierto tiempo
		objetos: Lista de objetos del escenario, donde se anadira el excremento'''
	def excretar(self, objetos):
		if self.tempoExcremento.pulso:
			objetos.addExcremento(self.cuerpo.x, self.cuerpo.y)
	
	'''Actualiza todos los temporizadores	
		delta: Tiempo de juego, necesario para actualizar los temporizadores'''
	def actualizarTemporizadores(self, delta):
		for temporizador in self.temporizadores:
			temporizador.actualizar(delta)
	
	'''Mueve el gato y lo voltea dependiendo de la velocidad'''
	def mover(self):
		if self.vx < 0:
			self.volteado = True
		elif self.vx > 0:
			self.volteado = False
			
		self.cuerpo.move_ip(self.vx, 0)
	
	'''Si tiene hambre, buscara la pieza de comida mas cercana.
		Si no tiene hambre, generara un punto aleatorio e ira a el.'''
	def definirObjetivo(self, objetos):
		if self.hambre < self.maxHambre and objetos.hayComida(): #Tiene hambre, buscar comida
			self.objetivo = objetos.obtenerComidaMasCercana(self.cuerpo.x)
		if self.tempoObjetivo.pulso and self.objetivo == None:
			self.objetivo = Rect(randrange(0, ANCHURA - self.cuerpo.width), self.cuerpo.y + self.cuerpo.height / 2, 10, 10)
	
	'''Va al objetivo seleccionado
		objetos: Se utiliza para borrar el objetivo si era un objeto del escenario y ha llegado a el
		sistemaParticulas: Se utiliza para generar una explosion si el objetivo era un objeto del escenario y ha llegado a el'''
	def irAObjetivo(self, objetos, sistemaParticulas):
		if self.objetivo != None: #Comprueba que el objetivo no sea nulo
			#Comprueba si el objetivo es un objeto del escenario o una posicion
			if type(self.objetivo) is Rect: #Comprueba si es posicion
				self.cuerpo_objetivo = self.objetivo
			else: #Comprueba si es un objeto del escenario
				self.cuerpo_objetivo = self.objetivo.cuerpo
		
			if self.cuerpo.right < self.cuerpo_objetivo.left: #Si el objetivo esta a la derecha del gato
				self.vx = VELOCIDAD_GATO
			elif self.cuerpo.left > self.cuerpo_objetivo.right: #Si el objetivo esta a la izquierda del gato
				self.vx = -VELOCIDAD_GATO
			else: #Si el gato ha llegado al objetivo
				if self.cuerpo.colliderect(self.cuerpo_objetivo): #Comprobar que el gato toque el objetivo
					self.vx = 0 #Frenar al gato
					if not type(self.objetivo) is Rect: #Si el objeto no era una posicion
						#Generar explosion de particulas
						sistemaParticulas.explosion((255, 0, 0), #Color de la particula
																self.cuerpo_objetivo.x + self.cuerpo_objetivo.width / 2, #Posicion horizontal
																self.cuerpo_objetivo.y + self.cuerpo_objetivo.height / 2) #Posicion vertical
						objetos.elementos.remove(self.objetivo) #Eliminar la comida de la lista de objetos accesibles						
						
						self.hambre += 20
						if self.hambre > HAMBRE_MAXIMA: #Limite del hambre
							self.hambre = HAMBRE_MAXIMA

					self.objetivo = None #Resetear objetivo
