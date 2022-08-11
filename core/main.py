import pygame
import os
from source.Configs import Configs
from source.Screen import Screen
from source.Bullet import Bullet
from source.Player import Player

# Titulo del juego
pygame.display.set_caption("Mi primer juego!")

# Dibujar texto en pantalla
pygame.font.init()
# Modulo mixer para el sonido
pygame.mixer.init()

#Función principal
def main():
    
    # Reloj para regular la velocidad del juego
    reloj = pygame.time.Clock()
    
    # Mantener encendido el juego
    energia = True

    while energia:
        #Se encarga de que este bucle se repita 60 veces por segundo
        reloj.tick(Configs.FPS)

        J1 = Player(1, Configs.J1, Configs.J1_Pos)
        J2 = Player(2, Configs.J2, Configs.J2_Pos)

        #Pygame.event.get() es una lista con todos los eventos de pygame. Con el bucle for la recorremos
        for event in pygame.event.get():
            # Evento detector de botones 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(Configs.J1_Balas) < Configs.Max_Balas:
                    bala = pygame.Rect(J1.Pos.x + J1.Pos.width, J1.Pos.y + J1.Pos.height//2 + 5, 10, 5)
                    Configs.J1_Balas.append(bala)
                    Configs.Sonido_Disparo_Bala.play()
                
                if event.key == pygame.K_RCTRL and len(Configs.J2_Balas) < Configs.Max_Balas:
                    bala = pygame.Rect(J2.Pos.x, J2.Pos.y + J2.Pos.height//2 + 5, 10, 5)
                    Configs.J2_Balas.append(bala)
                    Configs.Sonido_Disparo_Bala.play()

            # Evento impacto al jugador 2
            if event.type == Configs.J2_Impacto:
                Configs.J2_Vida -= 1
                Configs.Sonido_Impacto_Bala.play()

            # Evento impacto al jugador 1
            if event.type == Configs.J1_Impacto:
                Configs.J1_Vida -= 1
                Configs.Sonido_Impacto_Bala.play()

            # Evento salir del juego
            if event.type == pygame.QUIT:
                energia = False
                pygame.quit()

        # Secuencia del ganador
        texto_ganador = ""
        if Configs.J2_Vida <= 0:
            texto_ganador = "Jugador 1 Ganador!"
        
        if Configs.J1_Vida <= 0:
            texto_ganador = "Jugador 2 Ganador!"
        
        if texto_ganador != "":
            Screen.enunciado_ganador(texto_ganador)
            break

        # Detector de botones presionados
        botones_presionados = pygame.key.get_pressed()
        
        # Movimientos 
        J1.Control_Cfg(botones_presionados, J1.Pos, J1.Control)
        J2.Control_Cfg(botones_presionados, J2.Pos, J2.Control)
        Bullet.Balas_Control(Configs.J2_Balas, Configs.J1_Balas, J2.Pos, J1.Pos)

        # Renderizado de la pantalla
        Screen.dibujar_Pantalla(J1.Pos,J2.Pos, Configs.J2_Balas, Configs.J1_Balas, Configs.J2_Vida, Configs.J1_Vida)

    main()

#Este if comprueba si el fichero se llama main
if __name__ == "__main__":
    main()
