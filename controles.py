import pygame as py

class Controles(object):
	def __init__(self):
		self.pulsado = False
		
	def actualizar(self, delta):
		self.x = py.mouse.get_pos()[0]
		self.y = py.mouse.get_pos()[1]
		
		if py.mouse.get_pressed()[0] and not self.pulsado:
			self.pulsado = True
		
	
			