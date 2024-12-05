import pygame

class Nave():

    def __init__(self, pantalla):

        self.pantalla = pantalla

        #Carga la imagen de la nave y obtiene su rectangulo
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        self.rect.centerx = self.pantalla_rect.centerx

