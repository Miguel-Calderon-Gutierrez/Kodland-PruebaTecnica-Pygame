import sys
import pygame
from bala import Bala

def verificar_eventos_keydown(event, service_configuraciones, pantalla, nave, balas):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Se crea una bala y se agrega al grupo
        nueva_bala = Bala(service_configuraciones,pantalla, nave)
        balas.add(nueva_bala)

def verificar_eventos_keyup(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False

def verificar_eventos(service_configuraciones,pantalla,nave,balas):
    # Escuchar eventos de teclado o del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, service_configuraciones, pantalla, nave, balas)
        elif event.type == pygame.KEYUP:
           verificar_eventos_keyup(event,nave)

def actualizar_pantalla(service_configuraciones,pantalla,nave,balas):
    # Actualiza la pantalla cada pasada por el bucle
    pantalla.fill(service_configuraciones.bg_color)
    #vuelve a dibujar todas la balas
    for bala in balas.sprites():
        bala.draw_bala()
    #Se dibuja la nave
    nave.blitme()
    # Hacer visible la pantalla
    pygame.display.flip()