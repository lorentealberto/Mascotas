import pygame as py
from utilidades import cargarImagen
from configuracion import SIZE

class Nube(object):
	'''Clase nube, sirve para adornar el escenario'''
	
	'''Constructor'''
	def __init__(self):
		self.imagen = cargarImagen("nube", 4)
		self.cuerpo = py.Rect(0, 0, self.imagen.get_width(), self.imagen.get_height())
	
	'''Dibuja los graficos en la pantalla
		pantalla: superficie donde se dibujara'''
	def dibujar(self, pantalla):
		pantalla.blit(self.imagen, self.cuerpo)
	
	'''Actualiza el elemento'''
	def actualizar(self):
		self.cuerpo.move_ip(1, 0)
		

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
        self.nube.actualizar()
    
