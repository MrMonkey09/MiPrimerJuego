import pygame
import os
from source.Configs import Configs
from source.Map import Map

class Player:
    
    def __init__(self, Control, Avatar, Pos):
        self.Control = Control
        self.Avatar = Avatar
        self.Pos = Pos

    def Control_Cfg(self, botones_presionados, Pos, Control):
        if Control == 1:
            self.J1_Control(botones_presionados, Pos)
            
        elif Control == 2:
            self.J2_Control(botones_presionados, Pos)
        
    # Movimiento del jugador 1
    def J1_Control(self, botones_presionados, J1_Pos):
        if botones_presionados[pygame.K_a] and J1_Pos.x - Configs.VEL > 0: # Izquierda
            J1_Pos.x -= Configs.VEL
        if botones_presionados[pygame.K_d] and J1_Pos.x + Configs.VEL + J1_Pos.width < Map.Borde.x: # Derecha
            J1_Pos.x += Configs.VEL
        if botones_presionados[pygame.K_w] and J1_Pos.y - Configs.VEL > 0: # Arriba
            J1_Pos.y -= Configs.VEL
        if botones_presionados[pygame.K_s] and J1_Pos.y + Configs.VEL + J1_Pos.height < Configs.Ancho - 15: # Abajo
            J1_Pos.y += Configs.VEL

    # Movimiento del jugador 2
    def J2_Control(self, botones_presionados, J2_Pos):
        if botones_presionados[pygame.K_j] and J2_Pos.x - Configs.VEL > Map.Borde.x + Map.Borde.width: # Izquierda
            J2_Pos.x -= Configs.VEL
        if botones_presionados[pygame.K_l] and J2_Pos.x + Configs.VEL + J2_Pos.width < Configs.Ancho: # Derecha
            J2_Pos.x += Configs.VEL
        if botones_presionados[pygame.K_i] and J2_Pos.y - Configs.VEL > 0: # Arriba
            J2_Pos.y -= Configs.VEL
        if botones_presionados[pygame.K_k] and J2_Pos.y + Configs.VEL + J2_Pos.height < Configs.Alto - 15: # Abajo
            J2_Pos.y += Configs.VEL
