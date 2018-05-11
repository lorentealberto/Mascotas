from utilidades import cargarImagen
from configuracion import ANCHURA
from temporizador import Temporizador
from pajaro import Pajaro
from mira import Mira

class CazaPajaros(object):
    '''Minijuego: CazarPajaros
        Varios pajaros saldran por los lados de la pantalla
        El jugador tendra un numero limitado de balas y tendra
        que intentar matar la mayor cantidad de pajaros posibles
        con esas balas'''

    '''Constructor: Inicializa todos los elementos necesarios
        controles: Referencia a los controles'''
    def __init__(self, controles, particulas):
        self.img_pajaro = cargarImagen("pajaro", 2)
        self.pajaros = [Pajaro(self.img_pajaro)]
        self.tempAparicion = Temporizador(2000)
        self.mira = Mira(controles)
        self.controles = controles
        self.particulas = particulas

    '''Actualiza todos los elementos del minijuego
        delta: Tiempo externo, necesario para el temporizador de
            aparicion de los pajaros'''
    def actualizar(self, delta):
        self.tempAparicion.actualizar(delta)
        self.mira.actualizar()

        self.disparar()

        if self.tempAparicion.pulso:
            self.pajaros.append(Pajaro(self.img_pajaro))

        for pajaro in self.pajaros:
            pajaro.actualizar(delta)

    '''Dibuja en la pantalla todos los elementos del minijuego
        pantalla: Superficie donde se dibujaran los elementos'''
    def dibujar(self, pantalla):
        self.mira.dibujar(pantalla)
        for pajaro in self.pajaros:
            pajaro.dibujar(pantalla)

    
    def disparar(self):
        if self.controles.btnizq():
            for pajaro in self.pajaros:
                if self.mira.cuerpo.colliderect(pajaro.cuerpo):
                    self.particulas.explosion((255, 0, 0), pajaro.cuerpo.centerx, pajaro.cuerpo.centery)
                    self.pajaros.remove(pajaro)

                    break
        
