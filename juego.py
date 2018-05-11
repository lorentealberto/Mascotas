from gato import Gato
from escenario import Escenario
from objetos import Objetos
from controles import Controles
from interfaz import Interfaz
from sistema_particulas import SistemaParticulas
from minijuegos import Minijuegos

from configuracion import CRIADERO, MINIJUEGOS

class Juego(object):
    '''Clase que gestiona todos los recursos del juego
        Fecha: 25/04/2018
        Autor: Alberto Escribano Lorente'''

    '''Constructor, inicializa todos los elementos'''
    def __init__(self):
	self.controles = Controles()
	self.escenario = Escenario()
        self.gato = Gato(self.escenario.suelo.posicion)
        self.objectos = Objetos(self.escenario.suelo.posicion)
        self.interfaz = Interfaz(self.gato)
        self.sistemaParticulas = SistemaParticulas()
        self.minijuegos = Minijuegos(self.sistemaParticulas, self.controles)
        
        self.salaActual = MINIJUEGOS

    '''Dibuja todos los elementos
        pantalla: superficie donde se dibujaran'''
    def dibujar(self, pantalla):
        self.escenario.dibujar(pantalla)
        self.sistemaParticulas.dibujar(pantalla)
        
        if self.salaActual == CRIADERO:
            self.dibujarCriadero(pantalla)
        elif self.salaActual == MINIJUEGOS:
            self.dibujarMinijuegos(pantalla)

    '''Dibuja en la pantalla todos los elementos del criadero
        pantalla: Superficie donde se dibujara'''	
    def dibujarCriadero(self, pantalla):
        self.gato.dibujar(pantalla)
        self.objectos.dibujar(pantalla)
        self.interfaz.dibujar(pantalla)

    '''Dibuja en la pantalla los minijuegos
        pantalla: Superficie donde se dibujaran los minijuegos'''	
    def dibujarMinijuegos(self, pantalla):
        self.minijuegos.dibujar(pantalla)
		
    '''Actualiza todos los elementos
        delta: tiempo externo, necesario para algunas acciones'''
    def actualizar(self, delta):
        self.interfaz.actualizar(delta)
        self.controles.actualizar(delta)
        self.escenario.actualizar(delta, self.controles)
        self.sistemaParticulas.actualizar(delta)
        
        if self.salaActual == CRIADERO:
            self.actualizarCriadero(delta)
        elif self.salaActual == MINIJUEGOS:
            self.actualizarMinijuegos(delta)

    '''Actualiza todos los elementos del criadero
        delta: Tiempo externo, necesario para realizar algunas acciones'''
    def actualizarCriadero(self, delta):
	self.gato.actualizar(delta, self.objectos, self.sistemaParticulas)
	self.objectos.actualizar(delta, self.controles)

    '''Actualiza los minijuegos
        delta: Tiempo externo, necesario para algunas acciones'''
    def actualizarMinijuegos(self, delta):
	self.minijuegos.actualizar(delta)
