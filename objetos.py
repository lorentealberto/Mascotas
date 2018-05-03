from manzana import Manzana
from utilidades import cargarImagen
from math import sqrt
from configuracion import COMIDA

class Objetos:
	'''Gestiona los objetos que pueden anadirse al escenario'''
	def __init__(self, suelo):
		self.imagenes = {}
		self.cargarImagenes()
		self.suelo = suelo
		
		#Lista de elementos que hay actualmente en el escenario
		self.elementos = []
	
	'''Dibuja los objetos en la pantalla
		pantalla: superficie donde se dibujara'''
	def dibujar(self, pantalla):
		for elemento in self.elementos:
			elemento.dibujar(pantalla)
	
	'''Actualiza todos los elementos contenidos en la lista
		delta: tiempo del juego, utilizado para algunas funciones'''	
	def actualizar(self, delta, controles):
		for elemento in self.elementos:
			elemento.actualizar(delta)
			
		self.addObjeto(controles)
	
	'''Anade el objeto seleccionado al escenario
		controles: Gestor de controles'''
	def addObjeto(self, controles):
		if controles.btnizq():
			self.elementos.append(Manzana(self.imagenes["manzana"], controles.msx, controles.msy, self.suelo))
			controles.setBtnIzq(False)
	
	'''Devuelve el objeto del tipo comida mas cercano a la posicion horizontal indicada
		x: Se obtiene el objeto mas cercano a esta posicion'''
	def obtenerComidaMasCercana(self, x):
		self.menor = 500
		self.obj = None
		for obj in self.elementos:
			if obj.tipo == COMIDA:
				self.dist = sqrt((obj.cuerpo.x - x) ** 2)
				if self.dist < self.menor:
					self.menor = self.dist
					self.obj = obj
		return self.obj
	
	'''Carga los graficos de los elementos'''
	def cargarImagenes(self):
		self.imagenes["manzana"] = cargarImagen("manzana", 1)