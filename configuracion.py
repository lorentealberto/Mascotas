#CONFIGURACION DE LA VENTANA
ANCHURA = 640 #Anchura de la pantalla
ALTURA = 480 #Altura de la pantalla
SIZE = (ANCHURA, ALTURA) #Tamanio de la pantalla

#CONFIGURACION DEL ESCENARIO (MUNDO)
ALTITUD_MAXIMA_NUBE = 5 #Escala de altitud maxima para generar la nube
GRAVEDAD = 1 #Gravedad del mundo
GRAVEDAD_MAXIMA = 15 #Limite maximo para la velocidad vertical

#CONFIGURACION DE LA INTERFAZ
TAMANIO_BARRA = 120 #Tamanio de las barras de la interfaz (En pixeles)
ANCHURA_BARRA = 10 #Anchura de la barra de la interfaz (En pixeles)

#CONFIGURACION DEL GATO
VELOCIDAD_GATO = 2 #Velocidad del gato
HAMBRE_MAXIMA = 100 #Valor maximo de hambre que puede tener el gato
ESCALA_GATO = 4 #Escala de los graficos del gato
PERDIDA_DE_ENERGIA = 10 #Cantidad de hambre que se reduce cada vez que se gasta energia

#CONFIGURACION DE LAS PARTICULAS
PARTICULAS_EN_EXPLOSION = 20 #Numero de particulas que se generaran en cada explosion
TAM_PARTICULA = 3 #Tamanio de las particulas
VELOCIDAD_PARTICULA = 4 #Velocidad que tendra la particula
MIN_VIDA_PARTICULA = 100 #Tiempo minimo de vida que tendra una particula
MAX_VIDA_PARTICULA = 250 #Tiempo maximo de vida que tendra una particula

#CONFIGURACION DE LOS TIEMPOS
TIEMPO_CAMBIO_OBJETIVO = 3000 #Milisegundos que tarda el gato en ir a por un nuevo objetivo
TIEMPO_EXCREMENTO = 10000 #Milisegundos que tarda el gato en expulsar un excremento
TIEMPO_DESGASTE_ENERGIA = 5000 #Milisegundos que tarda en vaciarse un poco la barra de hambre

#CONFIGURACION DE LOS CONTROLES
BTNIZQ = 0 #Boton izquierdo raton
BTNDER = 1 #Boton derecho raton
BTNMED = 2 #Rueda raton

#TIPOS DE OBJETOS
COMIDA = 0 #Comida para el gato
EXCREMENTO = 1 #Excremento producido por el gato

#MODOS DE JUEGOS
CRIADERO = 0 #Pantalla de inicio
MINIJUEGOS = 1 #Minijuegos

#MINIJUEGOS
CAZA_PAJAROS = 0 #Minijuego de cazar pajaro

#PAJARO
IMPULSO_PAJARO = 13 #Impulso que tendra el pajaro al aletear
VELOCIDAD_PAJARO = 3 #Velocidad horizontal del pajaro
MIN_CAMBIO_IMPULSO_PAJARO = 375 #Tiempo minimo que tardara el pajaro en aletear
MAX_CAMBIO_IMPULSO_PAJARO = 500 #Tiempo maximo que tardara el pajaro en aletear 
SUELO_PAJARO = ALTURA - 150 #Altura limite inferior que puede alcanzar el pajaro
