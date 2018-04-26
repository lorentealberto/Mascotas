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
