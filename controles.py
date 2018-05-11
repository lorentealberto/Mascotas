import pygame as py
from configuracion import BTNIZQ, BTNDER, BTNMED

class Controles(object):
	def __init__(self):
		self.msx = 0
		self.msy = 0
		self.raton = [False, #Boton izquierdo
					False, #Boton derecho
					False] #Boton del medio (Rueda)
	
	#Actualiza los controles
	def actualizar(self, delta):
		self.actualizarPosicionRaton()
	
	#Actualiza la posicion del raton
	def actualizarPosicionRaton(self):
		self.msx = py.mouse.get_pos()[0] #Posicion X del raton
		self.msy = py.mouse.get_pos()[1] #Posicion Y del raton
	
	#Establece el estado del boton izquierdo del raton
	def setBtnIzq(self, estado):
		self.raton[BTNIZQ] = estado
	
	#Establece el estado del boton derecho del raton
	def setBtnDer(self, estado):
		self.raton[BTNDER] = estado
	
	#Establece el estado del boton medio del raton	
	def setBtnMed(self, estado):
		self.raton[BTNMED] = estado
		
	#Devuelve el estado del boton izquierdo del raton
	def btnizq(self):
		return self.raton[BTNIZQ]
	
	#Devuelve el estado del boton derecho del raton
	def btnder(self):
		return self.raton[BTNDER]
	
	#Devuelve el estado del boton medio del raton
	def btnmed(self):
		return self.raton[BTNMED]
