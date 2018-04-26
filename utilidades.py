import pygame as py
import os
import io
import zipfile

'''Carga el archivo de recursos'''
def cargarDatos():
	archivo = zipfile.ZipFile(os.path.dirname(os.path.realpath(__file__)) + "/recursos.zip", 'r')
	return archivo

'''CARGA UNA IMAGEN CON UNA DETERMINADA ESCALA
    escala: escala a la que se reescalara la imagen'''
def cargarImagen(ruta, escala = 1):
	imgfile = cargarDatos().read("recursos/imagenes/"+ruta+".png")
	bytes_io = io.BytesIO(imgfile)
	imagen = py.image.load(bytes_io).convert_alpha()
	return py.transform.scale(imagen, (imagen.get_width() * escala, imagen.get_height() * escala))
