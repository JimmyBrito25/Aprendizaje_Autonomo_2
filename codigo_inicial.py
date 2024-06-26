import pygame
import sys

pygame.init()

# Aquí definimos los colores que se utilizarán en el juego
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Las dimensiones y el nombre de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Atari Pong')

# Se define el reloj y los FPS de nuestro juego
clock = pygame.time.Clock()
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

# Empiezan las puntuaciones
punt_jugador1 = 0
punt_jugador2 = 0

# Los estados de mi juego
juego_pausa = False

# El 0 es para Reanudar, 1 es para Salir
opcion_seleccionada = 0

# Estado inicial del juego
menu_inicial = True
opcion_menu_inicial = 0

# Imagen de fondo del menú de pausa
fondo_menu_inicial = pygame.image.load('fondo_menu_resized.jpg')

#Efecto de sonido colisión de la pelota
sonido_colision = pygame.mixer.Sound('efecto_bola.wav')

# Dibujamos las paletas y la pelota que aparecerán en el juego
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (pos_jugador1[0], pos_jugador1[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (pos_jugador2[0], pos_jugador2[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (pos_bola[0], pos_bola[1], BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    draw_scores()
    pygame.display.flip()

def draw_scores():
    # Dibujamos las puntuaciones de los jugadores en la pantalla.
    font = pygame.font.Font(None, 74)
    text = font.render(str(punt_jugador1), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(punt_jugador2), 1, WHITE)
    screen.blit(text, (WIDTH - 250, 10))


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
    global vel_pel, punt_jugador1, punt_jugador2
    pos_bola[0] += vel_pel[0]
    pos_bola[1] += vel_pel[1]

    if pos_bola[1] <= 0 or pos_bola[1] >= HEIGHT - BALL_SIZE:
        vel_pel[1] = -vel_pel[1]
        sonido_colision.play()

    if (pos_bola[0] <= pos_jugador1[0] + PADDLE_WIDTH and pos_jugador1[1] < pos_bola[1] < pos_jugador1[1] + PADDLE_HEIGHT) or \
       (pos_bola[0] >= pos_jugador2[0] - BALL_SIZE and pos_jugador2[1] < pos_bola[1] < pos_jugador2[1] + PADDLE_HEIGHT):
        vel_pel[0] = -vel_pel[0]
        sonido_colision.play()

    if pos_bola[0] <= 0:
        punt_jugador2 += 1
        reset_ball()
    if pos_bola[0] >= WIDTH - BALL_SIZE:
        punt_jugador1 += 1
        reset_ball()

# Reinicia la posición y velocidad de la pelota
def reset_ball():
    pos_bola[0], pos_bola[1] = WIDTH // 2, HEIGHT // 2
    vel_pel[0] = -vel_pel[0]

# Esta función dibuja el menú de pausa
def draw_pause_menu():
    font = pygame.font.Font(None, 74)
    texto_reanudar = font.render("Reanudar", True, GRAY if opcion_seleccionada != 0 else WHITE)
    texto_salir = font.render("Salir", True, GRAY if opcion_seleccionada != 1 else WHITE)

    screen.blit(texto_reanudar, (WIDTH // 2 - texto_reanudar.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(texto_salir, (WIDTH // 2 - texto_salir.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

# Esta función dibuja el menú principal del juego
def draw_initial_menu():
    screen.blit(fondo_menu_inicial, (0, 0))
    font = pygame.font.Font(None, 74)
    texto_iniciar = font.render("Iniciar juego", True, GRAY if opcion_menu_inicial != 0 else WHITE)
    texto_salir = font.render("Salir", True, GRAY if opcion_menu_inicial != 1 else WHITE)

    screen.blit(texto_iniciar, (WIDTH // 2 - texto_iniciar.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(texto_salir, (WIDTH // 2 - texto_salir.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

#Aquí se dibuja el mensaje del ganador
def draw_winner_message(winner):
    font = pygame.font.Font(None, 74)
    texto_ganador = font.render(f"{winner} Ganó", True, WHITE)

    screen.fill(BLACK)
    screen.blit(texto_ganador, (WIDTH // 2 - texto_ganador.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

# Esta es la función principal que va a ejecutar el juego
def main():
    global juego_pausa, opcion_seleccionada, menu_inicial, opcion_menu_inicial, punt_jugador1, punt_jugador2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if menu_inicial:
                    if event.key == pygame.K_RETURN:
                        if opcion_menu_inicial == 0:
                            menu_inicial = False
                        elif opcion_menu_inicial == 1:
                            pygame.quit()
                            sys.exit()
                    if event.key == pygame.K_UP:
                        opcion_menu_inicial = (opcion_menu_inicial - 1) % 2
                    if event.key == pygame.K_DOWN:
                        opcion_menu_inicial = (opcion_menu_inicial + 1) % 2
                elif juego_pausa:
                    if event.key == pygame.K_RETURN:
                        if opcion_seleccionada == 0:
                            juego_pausa = False
                        elif opcion_seleccionada == 1:
                            pygame.quit()
                            sys.exit()
                    if event.key == pygame.K_UP:
                        opcion_seleccionada = (opcion_seleccionada - 1) % 2
                    if event.key == pygame.K_DOWN:
                        opcion_seleccionada = (opcion_seleccionada + 1) % 2
                elif punt_jugador1 >= 10 or punt_jugador2 >= 10:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_RETURN:
                        juego_pausa = True

        keys = pygame.key.get_pressed()
        if menu_inicial:
            draw_initial_menu()
        elif juego_pausa:
            draw_pause_menu()
        elif punt_jugador1 >= 10:
            draw_winner_message("Jugador 1")
        elif punt_jugador2 >= 10:
            draw_winner_message("Jugador 2")
        else:
            move_paddles(keys)
            move_ball()
            draw_objects()

        clock.tick(FPS)

# Se ejecuta el juego
if __name__ == "__main__":
    main()
