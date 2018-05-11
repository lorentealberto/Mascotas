from pygame import Rect
from pygame.transform import flip
from random import randrange
from configuracion import ANCHURA, GRAVEDAD, GRAVEDAD_MAXIMA
from configuracion import IMPULSO_PAJARO, VELOCIDAD_PAJARO, MIN_CAMBIO_IMPULSO_PAJARO, MAX_CAMBIO_IMPULSO_PAJARO, SUELO_PAJARO

from temporizador import Temporizador


class Pajaro(object):
    '''Pajaro Elemento del minijuego Cazar Pajaros
        Revolotea por la pantalla'''

    '''Constructor: Inicializa todos los componentes
        img: Imagen que representara al pajaro'''
    def __init__(self, img):
        self.img = img
        self.cuerpo = Rect(randrange(0, ANCHURA, ), 0, self.img.get_width(), self.img.get_height())
        self.temp_impulso = Temporizador(randrange(MIN_CAMBIO_IMPULSO_PAJARO, MAX_CAMBIO_IMPULSO_PAJARO))
        self.vy = 0
        self.girado = False
        
        self.establecerVelocidadHorizontal()

    '''Dibuja la imagen del pajaro en la pantalla
        pantalla: Superficie donde se dibujara'''
    def dibujar(self, pantalla):
        self.comprobarGiro()
        pantalla.blit(flip(self.img, self.girado, False), self.cuerpo)

    '''Actualiza la posicion del pajaro
        delta: Tiempo externo, necesario para realizar algunas acciones'''
    def actualizar(self, delta):
        self.temp_impulso.actualizar(delta)
        self.aplicarGravedad()
        self.aplicarImpulso()
        self.comprobarSuelo()
        self.comprobarBordes()
        self.cuerpo.move_ip(self.vx, self.vy)

    '''Aplica la gravedad al pajaro'''
    def aplicarGravedad(self):
        self.vy += GRAVEDAD
        if self.vy > GRAVEDAD_MAXIMA:
            self.vy = GRAVEDAD_MAXIMA

    '''Aplica un impulso al pajaro para que no caiga en picado'''
    def aplicarImpulso(self):
        if self.cuerpo.y > 50:
            if self.temp_impulso.pulso:
                self.vy = -IMPULSO_PAJARO
                self.temp_impulso.intervalo = randrange(MIN_CAMBIO_IMPULSO_PAJARO, MAX_CAMBIO_IMPULSO_PAJARO)

    '''Comprueba que el pajaro no supere el limite inferior del escenario'''
    def comprobarSuelo(self):
        if self.cuerpo.bottom >= SUELO_PAJARO:
            self.vy = -IMPULSO_PAJARO

    '''Comprueba que el pajaro no se salga de los bordes horizontales del mundo'''
    def comprobarBordes(self):
        if self.cuerpo.left + self.vx < 0 or self.cuerpo.right + self.vx > ANCHURA:
            self.vx *= -1
            
    '''Gira la imagen acorde a la velocidad actual del pajaro'''
    def comprobarGiro(self):
        if self.vx < 0:
            self.girado = True
        elif self.vx > 0:
            self.girado = False

    '''Establece aleatoriamente la velocidad horizontal del pajaro'''
    def establecerVelocidadHorizontal(self):
        self.vx = 0
        while self.vx == 0:
            self.vx = randrange(-VELOCIDAD_PAJARO, VELOCIDAD_PAJARO)
