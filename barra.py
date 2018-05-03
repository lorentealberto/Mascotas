import pygame as py
from configuracion import TAMANIO_BARRA, ANCHURA_BARRA

class Barra(object):
	#Barra
	
	#Constructor
	#max: Valor maximo que se representara
	#x: Posicion horizontal de la barra
	#y: Posicion vertical de la barra
	#color: Color de la barra, si no se indica ninguno se utilizara el color rojo por defecto
	def __init__(self, icono, max, x, y, color = (255, 0, 0)):
		self.icono = icono
		self.actual = 100
		self.valorMax = max
		self.x, self.y = x, y
		self.color = color
	
	#Dibuja la barra en la pantalla
	#pantalla: Superficie donde se dibujara
	def dibujar(self, pantalla):
		#Icono
		pantalla.blit(self.icono, (self.x, self.y))
		
		#Interior de la barra
		py.draw.rect(pantalla, self.color, (self.x + self.icono.get_width() + 5, #Posicion horizontal
											self.y + self.icono.get_height() / 2 - ANCHURA_BARRA / 2, #Posicion vertical 
											self.actual * TAMANIO_BARRA / self.valorMax, #Anchura de la barra (Dinamico)
											ANCHURA_BARRA)) #Grosor de la barra
		
		#Borde de la barra
		py.draw.rect(pantalla, (75, 75, 75), (self.x + self.icono.get_width() + 5 - 1, #Posicion horizontal
												self.y + self.icono.get_height() / 2 - ANCHURA_BARRA / 2- 1, #Posicion vertical
												TAMANIO_BARRA + 2, #Anchura del borde (Estatico)
												ANCHURA_BARRA + 2), #Grosor del borde
											2)
	
	#Actualiza la barra
	#actual: Valor actual que se representara
	def actualizar(self, actual):
		self.actual = actual
		
		self.comprobarLimite()
	
	#Comprueba el limite inferior de la barra para evitar que tome valores negativos
	def comprobarLimite(self):
		if self.actual <= 0:
			self.actual = 0