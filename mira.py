from pygame import Rect
from utilidades import cargarImagen


class Mira(object):
    '''Mira Aspecto del raton para el minijuego Cazar Pajaros'''
    
    '''Constructor: Inicializa todos los elementos
        controles: Actualiza la posicion del objeto'''
    def __init__(self, controles):
        self.img = cargarImagen("mira", 3)
        self.controles = controles
        self.cuerpo = Rect(self.controles.msx, self.controles.msy, 2, 2)

    '''Actualiza la posicion de la mira'''
    def actualizar(self):
        self.cuerpo.x = self.controles.msx - self.img.get_width() / 2
        self.cuerpo.y = self.controles.msy - self.img.get_height() / 2

    '''Dibuja la mira en la pantalla:
        pantalla: superficie donde se dibujara'''
    def dibujar(self, pantalla):
        pantalla.blit(self.img, self.cuerpo)
