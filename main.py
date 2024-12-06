import pygame
from pygame.sprite import Group
from configuraciones import Configuraciones
from nave import Nave
import funciones_juego as fj


def run_game():
    # Inicializar el juego y crear el objeto pantalla
    pygame.init()
    service_configuraciones = Configuraciones()

    pantalla = pygame.display.set_mode((service_configuraciones.screen_width, service_configuraciones.screen_height))
    pygame.display.set_caption(service_configuraciones.name_game)

    # se crea la nave, el grupo de balas y los aliens
    nave = Nave(service_configuraciones=service_configuraciones, pantalla=pantalla)
    balas = Group()
    aliens = Group()

    # crea una flota de aliens
    fj.crear_flota(service_configuraciones, pantalla, nave, aliens)

    # Iniciar el bucle principal del juego
    while True:
        # captura y verificacion de eventos
        fj.verificar_eventos(service_configuraciones, pantalla, nave, balas)
        nave.update()
        fj.updata_balas(aliens, balas)
        fj.update_aliens(service_configuraciones, aliens)
        fj.actualizar_pantalla(service_configuraciones, pantalla, nave, aliens, balas)


run_game()
