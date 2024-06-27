### Proyecto Atari Pong

## Descripción del Proyecto
Este proyecto es una implementación de un juego inspirado en el clásico Atari Pong utilizando la librería de `pygame`. 
El juego permite a dos jugadores controlar paletas en la pantalla para golpear una pelota y anotar puntos al pasarla por el oponente. 
El juego incluye un menú inicial con opciones para iniciar el juego o salir, así como un menú de pausa para reanudar el juego o salir.

## Funcionalidades Principales
- **Menú Inicial**: Al iniciar el programa, se muestra un menú con dos opciones: "Iniciar juego" y "Salir". Si una opción está seleccionada, su texto cambia a color blanco.
- **Control de Paletas**: Los jugadores pueden mover las paletas usando las teclas `W` y `S` para el Jugador 1, y las flechas `Arriba` y `Abajo` para el Jugador 2.
- **Movimiento de la Pelota**: La pelota rebota en las paredes y en las paletas. Si la pelota pasa una paleta, el jugador contrario anota un punto.
- **Menú de Pausa**: Durante el juego, al presionar `ENTER` se muestra un menú de pausa con opciones para "Reanudar" o "Salir". Las opciones seleccionadas también cambian de color.
- **Efectos de Sonido**: Los sonidos de colisión se reproducen cuando la pelota rebota en las paredes o las paletas.

## Objetivo del Programa
El objetivo de este proyecto es recrear el clásico juego de Atari Pong para dos jugadores de una manera básica e intuitiva para los usuarios que deseen probarlo. 

## Datos del Grupo
- **Integrante 1**: Jimmy Brito
- **Integrante 2**: Luis Lutuala

## Fecha
18 de Junio de 2024

## Instrucciones para Ejecutar el Juego
1. Asegúrate de tener `pygame` instalado. Si no lo tienes, puedes instalarlo usando:
_pip install pygame_
2. Clona este repositorio o descarga el archivo ZIP y descomprímelo.
3. Coloca la imagen `fondo_menu_resized.jpg` y el archivo de sonido `efecto_bola.wav` en el mismo directorio que el código principal.
4. Ejecuta el archivo principal del juego:
