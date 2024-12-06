import sys
import pygame

def verificar_eventos_keydown(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True

def verificar_eventos_keyup(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False

def verificar_eventos(nave):
    # Escuchar eventos de teclado o del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event,nave)
        elif event.type == pygame.KEYUP:
           verificar_eventos_keyup(event,nave)

def actualizar_pantalla(service_configuraciones, pantalla, nave):
    # Actualiza la pantalla cada pasada por el bucle
    pantalla.fill(service_configuraciones.bg_color)
    nave.blitme()

    # Vuelve a dibujar la pantalla cada pasada por el bucle
    pantalla.fill(service_configuraciones.bg_color)
    nave.blitme()

    # Hacer visible la pantalla
    pygame.display.flip()