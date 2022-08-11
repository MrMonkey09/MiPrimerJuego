import pygame
import os

# Dibujar texto en pantalla
pygame.font.init()
# Modulo mixer para el sonido
pygame.mixer.init()
class Configs:
    
    # Resolucion de pantalla
    Ancho = 1280
    Alto = 680   
    Pantalla = pygame.display.set_mode((Ancho, Alto))

    #Paleta de colores
    Blanco = (255, 255 , 255)
    Negro = (0, 0, 0)
    Rojo = (255, 0, 0)
    Amarillo = (255, 255, 0)

    #Fotogramas por segundo
    FPS = 60
    # Velocidad del jugador
    VEL = 5
    # Maximo de balas en pantalla
    Max_Balas = 3
    # Velocidad de las balas
    Vel_Bala = 7

    # Barra de vida
    Letra_Vida = pygame.font.SysFont('comicsans', 40)

    # Titulo de ganador
    Letra_Ganador = pygame.font.SysFont('comicsans', 100)

    # Definir los sonidos del juego
    Sonido_Impacto_Bala = pygame.mixer.Sound('assets/Grenade+1.wav')
    Sonido_Disparo_Bala = pygame.mixer.Sound('assets/Shot.wav')

    # Impacto de bala en el jugador
    J1_Impacto = pygame.USEREVENT + 1
    J2_Impacto = pygame.USEREVENT + 2

    # Importar fondo de pantalla
    Fondo_Pantalla = pygame.transform.scale(
        pygame.image.load(
            os.path.join('assets', 'space.png')),
            (Ancho, Alto))
    
    # Importar jugadores
    Jugador_Ancho, Jugador_Alto = 55,40

    J1_Modelo = pygame.image.load(
        os.path.join('assets', 'spaceship_yellow.png'))
    J1 = pygame.transform.rotate(pygame.transform.scale(
        J1_Modelo, (Jugador_Ancho, Jugador_Alto)), 90)

    J2_Modelo = pygame.image.load(
        os.path.join('assets', 'spaceship_red.png'))
    J2 = pygame.transform.rotate(pygame.transform.scale(
        J2_Modelo, (Jugador_Ancho, Jugador_Alto)), 270)

    # Imagen de la bala
    Bala_Modelo = pygame.image.load(
        os.path.join('assets', 'bullet.png'))
    Bala = pygame.transform.rotate(pygame.transform.scale(
        Bala_Modelo, (Jugador_Ancho, Jugador_Alto)), 270)

    # Rectangulos de posicionamento del jugador
    J2_Pos = pygame.Rect(750,200, Jugador_Ancho, Jugador_Alto)
    J1_Pos = pygame.Rect(100,200, Jugador_Ancho, Jugador_Alto)

    # Balas de los jugadores
    J2_Balas = []
    J1_Balas = []

    # Vida de los jugadores
    J2_Vida = 10
    J1_Vida = 10

    def __init__(self):
        pass