import pygame


class Nave():

    def __init__(self, service_configuraciones, pantalla):

        self.pantalla = pantalla
        self.service_configuraciones = service_configuraciones

        # Carga la imagen de la nave y obtiene su rectangulo
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Centra la imagen de la nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom

        self.center = float(self.rect.centerx)

        # Banderas de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.service_configuraciones.factor_velocidad_nave

        if self.moving_left and self.rect.left > 0:
            self.center -= self.service_configuraciones.factor_velocidad_nave

        self.rect.centerx = self.center

    def blitme(self):
        """Dibuja la imagen en su ubicación actual"""
        self.pantalla.blit(self.imagen, self.rect)
