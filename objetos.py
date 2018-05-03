from math import sqrt

from utilidades import cargarImagen
from configuracion import COMIDA

from manzana import Manzana
from excremento import Excremento

class Objetos:
	'''Gestiona los objetos que pueden anadirse al escenario'''
	def __init__(self, suelo):
		self.imagenes = {}
		self.cargarImagenes()
		self.suelo = suelo
		self.manzanas = 5
		
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
		if controles.btnizq() and self.manzanas > 0:
			self.elementos.append(Manzana(self.imagenes["manzana"], controles.msx, controles.msy, self.suelo))
			controles.setBtnIzq(False)
			self.manzanas -= 1
	
	def addExcremento(self, x, y):
		self.elementos.append(Excremento(self.imagenes["excremento"], x, y, self.suelo))
	
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
	
	'''Devuelve si hay o no comida en el escenario'''
	def hayComida(self):
		for obj in self.elementos:
			if obj.tipo == COMIDA:
				return True
		return False
	
	'''Carga los graficos de los elementos'''
	def cargarImagenes(self):
		self.imagenes["manzana"] = cargarImagen("manzana", 1)
		self.imagenes["excremento"] = cargarImagen("excremento", 1)