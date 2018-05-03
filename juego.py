from gato import Gato
from escenario import Escenario
from objetos import Objetos
from controles import Controles
from interfaz import Interfaz
from sistema_particulas import SistemaParticulas

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

    '''Dibuja todos los elementos
        pantalla: superficie donde se dibujaran'''
    def dibujar(self, pantalla):
		self.escenario.dibujar(pantalla)
		self.gato.dibujar(pantalla)
		self.objectos.dibujar(pantalla)
		self.sistemaParticulas.dibujar(pantalla)
		self.interfaz.dibujar(pantalla)
		
    '''Actualiza todos los elementos
        delta: tiempo externo, necesario para algunas acciones'''
    def actualizar(self, delta):
		self.interfaz.actualizar(delta)
		self.controles.actualizar(delta)
		self.interfaz.actualizar(delta)
		self.escenario.actualizar(delta, self.controles)
		self.gato.actualizar(delta, self.controles, self.objectos, self.sistemaParticulas)
		self.objectos.actualizar(delta, self.controles)
		self.sistemaParticulas.actualizar(delta)