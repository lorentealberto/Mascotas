import pygame as py
from pygame.locals import QUIT

#Tamanio de la pantalla
SIZE = (640, 480)

#METODOS GLOBALES

'''CARGA UNA IMAGEN CON UNA DETERMINADA ESCALA
    escala: escala a la que se reescalara la imagen'''
def cargarImagen(ruta, escala = 1):
    imagen = py.image.load("recursos/imagenes/"+ruta+".png").convert_alpha()
    return py.transform.scale(imagen, (imagen.get_width() * escala, imagen.get_height() * escala))

#CLASES
class Temporizador(object):
    '''Clase que activa un pulso cada cierto tiempo
        Autor: Alberto E. Lorente
        Fecha: 25/04/2018'''

    '''Constructor
        intervalo: Tiempo que tardara en activarse el pulso'''
    def __init__(self, intervalo):
        self.intervalo = intervalo
        self.tiempo = 0
        self.pulso = False

    '''Actualiza el tiempo interno en base al tiempo del programa para activar o desactivar el pulso
        delta: tiempo del programa'''
    def actualizar(self, delta):
        self.tiempo += delta
        if self.tiempo > self.intervalo:
            self.tiempo = 0
            self.pulso = True
        else:
            self.pulso = False


class Escenario(object):
    '''Clase para representar el escenario y todos sus elementos
        Fecha: 25/04/2018
        Autor: Alberto Escribano Lorente'''

    '''Constructor: Inicializa todos los elementos del escenario'''
    def __init__(self):
        pass

    '''Dibuja todos los elementos del escenario en la pantalla
        pantalla: superficie donde se dibujaran los elementos'''
    def dibujar(self, pantalla):
        pass

    '''Actualiza todos los elementos del escenario
        delta: tiempo de juego, necesario para algunas acciones'''
    def actualizar(self, delta):
        pass
    

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
        


def main():
    #Inicializa el juego
    py.init()
    screen = py.display.set_mode((SIZE))
    py.display.set_caption("Mascotas")

    clear = (64, 196, 255) #Color con el que se limpiara la pantalla
    exit = False #Bandera para salir
    fps = py.time.Clock() #Reloj del juego
    delta = 0 #Tiempo que dura una iteracion del bucle de juego

    juego = Juego()
    
    while not exit: #Bucle de juego
        for event in py.event.get(): #Si el jugador cierra la ventana, finalizar el juego
            if event.type == QUIT:
                exit = True

        screen.fill(clear) #Limpiar pantalla

        juego.actualizar(delta)
        juego.dibujar(screen)

        py.display.update() #Actualizar pantalla
        delta = fps.tick(60)#Actualizar FPS y tiempo de iteracion
    py.quit()
    return 0
if __name__ == "__main__":
    main()
