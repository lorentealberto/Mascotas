from gato import Gato
class Juego(object):
    '''Clase que gestiona todos los recursos del juego
        Fecha: 25/04/2018
        Autor: Alberto Escribano Lorente'''

    '''Constructor, inicializa todos los elementos'''
    def __init__(self):
        self.gato = Gato()

    '''Dibuja todos los elementos
        pantalla: superficie donde se dibujaran'''
    def dibujar(self, pantalla):
        self.gato.dibujar(pantalla)

    '''Actualiza todos los elementos
        delta: tiempo externo, necesario para algunas acciones'''
    def actualizar(self, delta):
        self.gato.actualizar(delta)
        
