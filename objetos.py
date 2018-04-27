from controles import Controles
from manzana import Manzana
from utilidades import cargarImagen

class Objetos:
	'''Gestiona los objetos que pueden anadirse al escenario'''
	def __init__(self):
		self.imagenes = {}
		self.cargarImagenes()
		
		#Lista de elementos que hay actualmente en el escenario
		self.elementos = []
		self.controles = Controles()
	
	'''Dibuja los objetos en la pantalla
		pantalla: superficie donde se dibujara'''
	def dibujar(self, pantalla):
		for elemento in self.elementos:
			elemento.dibujar(pantalla)
	
	'''Actualiza todos los elementos contenidos en la lista
		delta: tiempo del juego, utilizado para algunas funciones'''	
	def actualizar(self, delta):
		self.controles.actualizar(delta)
		if self.controles.pulsado:
			self.elementos.append(Manzana(self.imagenes["manzana"], self.controles.x, self.controles.y))
			
		for elemento in self.elementos:
			elemento.actualizar(delta)
			
	
	'''Carga los graficos de los elementos'''
	def cargarImagenes(self):
		self.imagenes["manzana"] = cargarImagen("manzana", 1)