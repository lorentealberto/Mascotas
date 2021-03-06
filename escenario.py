from pygame import Rect
from utilidades import cargarImagen
from configuracion import ANCHURA, ALTURA, ALTITUD_MAXIMA_NUBE
from random import randrange

class Suelo(object):
	'''Suelo del escenario'''
	
	'''Constructor
		Carga los graficos y establece la posicion del suelo'''
	def __init__(self):
		self.imagen = cargarImagen("suelo", 4)
		self.posicion = ALTURA - self.imagen.get_height()
	
	'''Dibuja el suelo en la pantalla
		pantalla: Superficie donde se dibujaran los graficos'''
	def dibujar(self, pantalla):
		for i in range(ANCHURA / self.imagen.get_width()):
			pantalla.blit(self.imagen, (self.imagen.get_width() * i, self.posicion))

class Nube(object):
	'''Clase nube, sirve para adornar el escenario
		Fecha: 26/04/2018
		Autor: Alberto Escribano Lorente'''
	
	'''Constructor: Carga la imagen y establece la posicion'''
	def __init__(self):
		self.imagen = cargarImagen("nube", 4)
		self.cuerpo = Rect(0, 0, self.imagen.get_width(), self.imagen.get_height())
		self.cuerpo.x = randrange(0, ANCHURA - self.cuerpo.width) #Establece una posicion horizontal aleatoria
		self.cuerpo.y = randrange(0, self.cuerpo.height * ALTITUD_MAXIMA_NUBE) #Establece una altura aleatoria
	
	'''Dibuja los graficos en la pantalla
		pantalla: superficie donde se dibujara'''
	def dibujar(self, pantalla):
		pantalla.blit(self.imagen, self.cuerpo)
	
	'''Actualiza el elemento'''
	def actualizar(self, delta):
		self.cuerpo.move_ip(1, 0)
		self.comprobarBordes()
	
	'''Comprueba si la nube ha llegado al borde derecho. Si es asi,
		vuelve a aparecer por el borde izquierdo. Cada vez que la
		nube reaparece, lo hara a una altura diferente'''
	def comprobarBordes(self):
		if self.cuerpo.left > ANCHURA:
			self.cuerpo.right = 0
			self.cuerpo.y = randrange(0, self.cuerpo.height * ALTITUD_MAXIMA_NUBE)

class Escenario(object):
    '''Clase para representar el escenario y todos sus elementos
        Fecha: 25/04/2018
        Autor: Alberto Escribano Lorente'''

    '''Constructor: Inicializa todos los elementos del escenario'''
    def __init__(self):
		self.nube = Nube()
		self.suelo = Suelo()

    '''Dibuja todos los elementos del escenario en la pantalla
        pantalla: superficie donde se dibujaran los elementos'''
    def dibujar(self, pantalla):
		self.nube.dibujar(pantalla)
		self.suelo.dibujar(pantalla)

    '''Actualiza todos los elementos del escenario
        delta: tiempo de juego, necesario para algunas acciones. opcional'''
    def actualizar(self, delta, controles):
        self.nube.actualizar(delta)
    
