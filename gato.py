import pygame as py

from utilidades import cargarImagen
from configuracion import SIZE

class Gato(object):
    '''Clase que representa la mascota
        Fecha: 25/04/2018
        Autor: Alberto Escribano Lorente'''

    '''Constructor'''
    def __init__(self):
        self.imagen = cargarImagen("gato", 4)

        #Crea el cuerpo del gato, se usara para gestionar el movimiento y las colisiones
        self.cuerpo = py.Rect(SIZE[0] / 2 - self.imagen.get_width() / 2, #POSICION X
                              SIZE[1] - self.imagen.get_height(), #POSICION Y
                              self.imagen.get_width(), #ANCHURA
                              self.imagen.get_height()) #ALTURA

    '''Dibuja el gato en la pantalla
        pantalla: superficie donde se dibujara'''
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.cuerpo)

    '''Actualiza todos los elementos
        delta: tiempo de juego, necesario para algunas acciones'''
    def actualizar(self, delta):
        pass
