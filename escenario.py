from pygame import Rect
from utilidades import cargarImagen
from configuracion import SIZE, ALTITUD_MAXIMA_NUBE
from random import randrange

class Nube(object):
	'''Clase nube, sirve para adornar el escenario
		Fecha: 26/04/2018
		Autor: Alberto Escribano Lorente'''
	
	'''Constructor: Carga la imagen y establece la posicion'''
	def __init__(self):
		self.imagen = cargarImagen("nube", 4)
		self.cuerpo = Rect(0, 0, self.imagen.get_width(), self.imagen.get_height())
		self.cuerpo.x = randrange(0, SIZE[0] - self.cuerpo.width) #Establece una posicion horizontal aleatoria
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
		if self.cuerpo.left > SIZE[0]:
			self.cuerpo.right = 0
			self.cuerpo.y = randrange(0, self.cuerpo.height * ALTITUD_MAXIMA_NUBE)
		

class Escenario(object):
    '''Clase para representar el escenario y todos sus elementos
        Fecha: 25/04/2018
        Autor: Alberto Escribano Lorente'''

    '''Constructor: Inicializa todos los elementos del escenario'''
    def __init__(self):
        self.nube = Nube()

    '''Dibuja todos los elementos del escenario en la pantalla
        pantalla: superficie donde se dibujaran los elementos'''
    def dibujar(self, pantalla):
        self.nube.dibujar(pantalla)

    '''Actualiza todos los elementos del escenario
        delta: tiempo de juego, necesario para algunas acciones. opcional'''
    def actualizar(self, delta = None):
        self.nube.actualizar(delta)
    
