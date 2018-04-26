import pygame as py
'''CARGA UNA IMAGEN CON UNA DETERMINADA ESCALA
    escala: escala a la que se reescalara la imagen'''
def cargarImagen(ruta, escala = 1):
    imagen = py.image.load("recursos/imagenes/"+ruta+".png").convert_alpha()
    return py.transform.scale(imagen, (imagen.get_width() * escala, imagen.get_height() * escala))
