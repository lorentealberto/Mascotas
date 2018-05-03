from barra import Barra
from utilidades import cargarImagen
class Interfaz(object):
	#Interfaz de usuario
	
	#Constructor
	#Necesita obtener como parametro todos los objetos que tengan valores que se representaran
	def __init__(self, gato):
		self.gato = gato
		self.barra = Barra(cargarImagen("manzana"), 100, 20, 20)
	
	#Dibuja la interfaz en la pantalla
	#pantalla: Superficie donde se dibujara
	def dibujar(self, pantalla):
		self.barra.dibujar(pantalla)
	
	#Actualiza la interfaz
	#delta: Tiempo de juego, necesario para realizar algunas acciones
	def actualizar(self, delta):
		self.barra.actualizar(self.gato.hambre)