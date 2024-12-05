import pygame

class Nave():

    def __init__(self, pantalla):

        self.pantalla = pantalla

        #Carga la imagen de la nave y obtiene su rectangulo
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        #Centra la imagen de la nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom


    def blitme(self):
        """Dibuja la imagen en su ubicación actual"""
        self.pantalla.blit(self.imagen,self.rect)
