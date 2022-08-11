import pygame
import os
from source.Configs import Configs
from source.Map import Map

# Clase quien mantiene y modifica la Pantalla
class Screen:
    def __init__(self):
        pass

    # Funcion del ganador
    def enunciado_ganador(texto_ganador):
        dibujar_texto = Configs.Letra_Ganador.render(texto_ganador, 1, Configs.Blanco)
        Configs.Pantalla.blit(dibujar_texto, (Configs.Ancho/2 - dibujar_texto.get_width() / 2, Configs.Alto/2 - dibujar_texto.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)
    
    # Funcion para dibujar en Pantalla
    def dibujar_Pantalla(J1, J2, J2_balas, J1_balas, J2_vida, J1_vida):
        Configs.Pantalla.blit(Configs.Fondo_Pantalla, (0,0))
        pygame.draw.rect(Configs.Pantalla,Configs.Negro,Map.Borde)
        Configs.Pantalla.blit(Configs.J1, (J1.x, J1.y))
        Configs.Pantalla.blit(Configs.J2, (J2.x,J2.y))

        # Dibujado de la vida de los jugadores
        J2_vida_text = Configs.Letra_Vida.render("Vida: " + str(J2_vida), 1, Configs.Blanco)
        J1_vida_text = Configs.Letra_Vida.render("Vida: " + str(J1_vida), 1, Configs.Blanco)
        Configs.Pantalla.blit(J2_vida_text,(Configs.Ancho - J2_vida_text.get_width() - 10, 10))
        Configs.Pantalla.blit(J1_vida_text, (10,10))

        for bullet in J2_balas:
            pygame.draw.rect(Configs.Pantalla, Configs.Rojo, bullet)
            Configs.Pantalla.blit(Configs.Bala, (bullet.x,bullet.y))
        
        for bullet in J1_balas:
            pygame.draw.rect(Configs.Pantalla, Configs.Amarillo, bullet)

        pygame.display.update()