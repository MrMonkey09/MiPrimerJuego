import pygame
import os

# Dibujar texto en pantalla
pygame.font.init()

# Modulo mixer para el sonido
pygame.mixer.init()

# Resolucion de pantalla
WIDTH, HEIGHT = 900, 500   
PANTALLA = pygame.display.set_mode((WIDTH, HEIGHT))

# Titulo del juego
pygame.display.set_caption("Mi primer juego!")

#Paleta de colores
WHITE = (255, 255 , 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#Fotogramas por segundo
FPS = 60
# Velocidad del jugador
VEL = 5
# Maximo de balas en pantalla
MAX_BULLETS = 3
# Velocidad de las balas
BULLET_VEL = 7

# Barra de vida
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)

# Titulo de ganador
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Definir los sonidos del juego
BULLET_HIT_SOUND = pygame.mixer.Sound('assets/Grenade+1.wav')
BULLET_FIRE_SOUND = pygame.mixer.Sound('assets/Shot.wav')

# Importar fondo de pantalla
SPACE = pygame.transform.scale(
    pygame.image.load(
        os.path.join('assets', 'space.png')),
        (WIDTH, HEIGHT))

# Importar jugadores
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Impacto de bala en el jugador
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Borde del mapa
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

# Movimiento del jugador 1
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # Izquierda
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # Derecha
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # Arriba
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # Abajo
        yellow.y += VEL

# Movimiento del jugador 2
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_j] and red.x - VEL > BORDER.x + BORDER.width: # Izquierda
        red.x -= VEL
    if keys_pressed[pygame.K_l] and red.x + VEL + red.width < WIDTH: # Derecha
        red.x += VEL
    if keys_pressed[pygame.K_i] and red.y - VEL > 0: # Arriba
        red.y -= VEL
    if keys_pressed[pygame.K_k] and red.y + VEL + red.height < HEIGHT - 15: # Abajo
        red.y += VEL

# Movimiento de las balas
def handled_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            yellow_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(RED_HIT))
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
        elif bullet.x < 0:
            red_bullets.remove(bullet)

# Funcion del ganador
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    PANTALLA.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# Funcion para dibujar en pantalla
def draw_windows(yellow, red, red_bullets, yellow_bullets, red_health, yellow_health):
    PANTALLA.blit(SPACE, (0,0))
    pygame.draw.rect(PANTALLA,BLACK,BORDER)
    PANTALLA.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    PANTALLA.blit(RED_SPACESHIP, (red.x,red.y))

    # Dibujado de la vida de los jugadores
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    PANTALLA.blit(red_health_text,(WIDTH - red_health_text.get_width() - 10, 10))
    PANTALLA.blit(yellow_health_text, (10,10))

    for bullet in red_bullets:
        pygame.draw.rect(PANTALLA, RED, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(PANTALLA, YELLOW, bullet)

    pygame.display.update()

#Función principal
def main():
    # Rectangulos de posicionamento del jugador
    red = pygame.Rect(750,200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Balas de los jugadores
    red_bullets = []
    yellow_bullets = []

    # Vida de los jugadores
    red_health = 10
    yellow_health = 10

    # Reloj para regular la velocidad del juego
    clock = pygame.time.Clock()
    
    # Mantener encendido el juego
    run = True

    while run:
        #Se encarga de que este bucle se repita 60 veces por segundo
        clock.tick(FPS)

        """ Pygame.event.get() es una lista con todos los eventos
        de pygame. Con el bucle for la recorremos """
        for event in pygame.event.get():
            # Evento detector de botones 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 5, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 + 5, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # Evento impacto al jugador 2
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            # Evento impacto al jugador 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

            # Evento salir del juego
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        # Secuencia del ganador
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break

        # Detector de botones presionados
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handled_bullets(red_bullets, yellow_bullets, red, yellow)

        # Renderizado de la pantalla
        draw_windows(yellow,red, red_bullets, yellow_bullets, red_health, yellow_health)

    main()

#Este if comprueba si el fichero se llama main
if __name__ == "__main__":
    main()
