import pygame
from pygame.sprite import Group
from configuraciones import Configuraciones
from nave import Nave
import funciones_juego as fj

def run_game():
    #Inicializar el juego y crear el objeto pantalla
    pygame.init()
    service_configuraciones = Configuraciones()

    pantalla = pygame.display.set_mode((service_configuraciones.screen_width,service_configuraciones.screen_height))
    pygame.display.set_caption(service_configuraciones.name_game)

    #se crea la nave
    nave = Nave(service_configuraciones = service_configuraciones,pantalla = pantalla)
    #crea un grupo para las balas
    balas = Group()

    #Iniciar el bucle principal del juego
    while True:
        #captura y verificacion de eventos
        fj.verificar_eventos(service_configuraciones,pantalla,nave,balas)
        nave.update()
        balas.update()
        fj.actualizar_pantalla(service_configuraciones,pantalla,nave,balas)

run_game()