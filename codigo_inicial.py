import pygame
import sys
pygame.init()

# Aquí definimos los colores que se utilizarán en el juego
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Las dimensiones y el nombre de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Atari Pong')

# Se define el reloj y los FPS de nuestro juego
reloj = pygame.time.Clock()
FPS = 60

# Definir las dimensiones y posiciones iniciales de las paletas y la pelota
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10

pos_jugador1 = [50, HEIGHT // 2 - PADDLE_HEIGHT // 2]
pos_jugador2 = [WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2]
pos_bola = [WIDTH // 2, HEIGHT // 2]
vel_pel = [5, 5]

# Velocidad de las paletas
vel_paletas = 7

# Dibujamos las paletas y la pelota que aparecerán en el juego
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (pos_jugador1[0], pos_jugador1[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (pos_jugador2[0], pos_jugador2[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (pos_bola[0], pos_bola[1], BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pygame.display.flip()

# Aquí definimos las teclas de movimiento
def move_paddles(keys):
    if keys[pygame.K_w] and pos_jugador1[1] > 0:
        pos_jugador1[1] -= vel_paletas
    if keys[pygame.K_s] and pos_jugador1[1] < HEIGHT - PADDLE_HEIGHT:
        pos_jugador1[1] += vel_paletas
    if keys[pygame.K_UP] and pos_jugador2[1] > 0:
        pos_jugador2[1] -= vel_paletas
    if keys[pygame.K_DOWN] and pos_jugador2[1] < HEIGHT - PADDLE_HEIGHT:
        pos_jugador2[1] += vel_paletas

# Aquí nosotros definimos cómo se va a comportar la pelota
def move_ball():
    global vel_pel
    pos_bola[0] += vel_pel[0]
    pos_bola[1] += vel_pel[1]

    if pos_bola[1] <= 0 or pos_bola[1] >= HEIGHT - BALL_SIZE:
        vel_pel[1] = -vel_pel[1]

    if (pos_bola[0] <= pos_jugador1[0] + PADDLE_WIDTH and pos_jugador1[1] < pos_bola[1] < pos_jugador1[1] + PADDLE_HEIGHT) or \
       (pos_bola[0] >= pos_jugador2[0] - BALL_SIZE and pos_jugador2[1] < pos_bola[1] < pos_jugador2[1] + PADDLE_HEIGHT):
        pos_bola[0] = -vel_pel[0]

    if pos_bola[0] <= 0 or pos_bola[0] >= WIDTH - BALL_SIZE:
        pos_bola[0], pos_bola[1] = WIDTH // 2, HEIGHT // 2
        vel_pel[0] = -vel_pel[0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    move_paddles(keys)
    move_ball()
    draw_objects()
    reloj.tick(FPS)
