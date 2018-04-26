import pygame as py
from pygame.locals import QUIT
from configuracion import SIZE
from juego import Juego

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
