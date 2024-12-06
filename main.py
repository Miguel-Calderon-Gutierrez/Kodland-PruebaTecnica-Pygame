import pygame
import funciones_juego as fj
from pygame.sprite import Group
from configuraciones import Configuraciones
from estadisticas import Estadisticas
from nave import Nave
from button import Button
from marcador import Marcador

def run_game():
    # Inicializar el juego y crear el objeto pantalla
    pygame.init()
    service_configuraciones = Configuraciones()

    pantalla = pygame.display.set_mode((service_configuraciones.screen_width, service_configuraciones.screen_height))
    pygame.display.set_caption(service_configuraciones.name_game)

    # boton de play
    play_button = Button(service_configuraciones, pantalla, "Iniciar")

    # Estadisticas del juego
    estadisticas = Estadisticas(service_configuraciones)
    marcador = Marcador(service_configuraciones, pantalla, estadisticas)
    # se crea la nave, el grupo de balas y los aliens
    nave = Nave(service_configuraciones=service_configuraciones, pantalla=pantalla)
    balas = Group()
    aliens = Group()

    # crea una flota de aliens
    fj.crear_flota(service_configuraciones, pantalla, nave, aliens)

    # Iniciar el bucle principal del juego
    while True:
        # captura y verificacion de eventos
        fj.verificar_eventos(service_configuraciones, pantalla, estadisticas, play_button, nave, aliens, balas)
        if estadisticas.game_active:
            nave.update()
            fj.updata_balas(service_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas)
            fj.update_aliens(service_configuraciones, estadisticas, pantalla, nave, aliens, balas)

        fj.actualizar_pantalla(service_configuraciones, pantalla, estadisticas, marcador,nave, aliens, balas, play_button)


run_game()
