from cazapajaros import CazaPajaros
from configuracion import CAZA_PAJAROS


class Minijuegos(object):
    '''Gestiona los minijuegos'''

    '''Constructor; inicializa todos los elementos'''
    def __init__(self, particulas, controles):
         self.minijuegos = [CazaPajaros(controles, particulas)]
         self.actual = CAZA_PAJAROS

    '''Actualiza el minijuego seleccionado
        delta: Tiempo externo, necesario para realizar algunas acciones'''      
    def actualizar(self, delta):
        self.minijuegos[self.actual].actualizar(delta)

    '''Dibuja el minijuego actual en la pantalla
        pantalla: Superficie donde se dibujara'''      
    def dibujar(self, pantalla):
        self.minijuegos[self.actual].dibujar(pantalla)
