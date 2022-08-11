import pygame
import os
from source.Configs import Configs

class Bullet:

    def __init__(self):
        pass

    # Movimiento de las balas
    def Balas_Control(J2_Balas, J1_Balas, J2_Pos, J1_Pos):
        for bullet in J1_Balas:
            bullet.x += Configs.Vel_Bala
            if J2_Pos.colliderect(bullet):
                J1_Balas.remove(bullet)
                pygame.event.post(pygame.event.Event(Configs.J2_Impacto))
            elif bullet.x > Configs.Ancho:
                J1_Balas.remove(bullet)
        
        for bullet in J2_Balas:
            bullet.x -= Configs.Vel_Bala
            if J1_Pos.colliderect(bullet):
                J2_Balas.remove(bullet)
                pygame.event.post(pygame.event.Event(Configs.J1_Impacto))
            elif bullet.x < 0:
                J2_Balas.remove(bullet)