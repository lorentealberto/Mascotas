from gato import Gato
from escenario import Escenario
from objetos import Objetos

class Juego(object):
    '''Clase que gestiona todos los recursos del juego
        Fecha: 25/04/2018
        Autor: Alberto Escribano Lorente'''

    '''Constructor, inicializa todos los elementos'''
    def __init__(self):
		self.elementos = [Escenario(), Gato(), GestorElementos()]

    '''Dibuja todos los elementos
        pantalla: superficie donde se dibujaran'''
    def dibujar(self, pantalla):
        for elemento in self.elementos:
			elemento.dibujar(pantalla)

    '''Actualiza todos los elementos
        delta: tiempo externo, necesario para algunas acciones'''
    def actualizar(self, delta):
        for elemento in self.elementos:
			elemento.actualizar(delta)
        
