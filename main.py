import sys
import pygame
from configuraciones import Configuraciones
def run_game():
    #Inicializar el juego y crear el objeto pantalla
    pygame.init()
    service_configuraciones = Configuraciones()

    pantalla = pygame.display.set_mode((service_configuraciones.screen_width,service_configuraciones.screen_height))
    pygame.display.set_caption(service_configuraciones.name_game)

    #Iniciar el bucle principal del juego
    while True:

        #Escuchar eventos de teclado o del mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pantalla.fill(service_configuraciones.bg_color)
        #Hacer visible la pantalla
        pygame.display.flip()


run_game()