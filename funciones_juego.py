import sys
import pygame
from bala import Bala
from alien import Alien
from nave import Nave


def verificar_eventos_keydown(event, service_configuraciones, pantalla, nave, balas):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Se crea una bala y se agrega al grupo
        fuego_bala(service_configuraciones, pantalla, nave, balas)
    elif event.key == pygame.K_q:
        sys.exit()


def verificar_eventos_keyup(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False


def verificar_eventos(service_configuraciones, pantalla, nave, balas):
    # Escuchar eventos de teclado o del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, service_configuraciones, pantalla, nave, balas)
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)


def actualizar_pantalla(service_configuraciones, pantalla, nave, aliens, balas):
    # Actualiza la pantalla cada pasada por el bucle
    pantalla.fill(service_configuraciones.bg_color)
    # vuelve a dibujar todas la balas
    for bala in balas.sprites():
        bala.draw_bala()
    # Se dibuja la nave
    nave.blitme()
    # Se dibuja el alien
    aliens.draw(pantalla)
    # Hacer visible la pantalla
    pygame.display.flip()


def updata_balas(service_configuraciones, pantalla, nave, aliens, balas):
    # actualiza las balas y elimina las antiguas
    balas.update()
    # Eliminar balas que salen de rango
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    check_bala_alien_collisions(service_configuraciones, pantalla, nave, aliens, balas)


def check_bala_alien_collisions(service_configuraciones, pantalla, nave, aliens, balas):
    """Elimina las balas y los aliensque choquen"""
    collisions = pygame.sprite.groupcollide(balas, aliens, True, True)

    if len(aliens) == 0:
        # Si se destruye toda la flota, comienza un nuevo nivel
        balas.empty()
        crear_flota(service_configuraciones, pantalla, nave, aliens)


def fuego_bala(service_configuraciones, pantalla, nave, balas):
    # Se crea una bala y se agrega al grupo
    if len(balas) < service_configuraciones.balas_allowed:
        nueva_bala = Bala(service_configuraciones, pantalla, nave)
        balas.add(nueva_bala)


def get_number_aliens_x(service_configuraciones, alien_width):
    available_space_x = service_configuraciones.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def get_number_rows(service_configuraciones, nave_height, alien_height):
    """Determina el numero de aliens que se ajustan en la pantalla"""
    available_space_y = (service_configuraciones.screen_width - (3 * alien_height) - nave_height)
    number_rows = int((available_space_y / (2 * alien_height)) - 1)
    return number_rows


def crear_alien(service_configuraciones, pantalla, aliens, alien_number, row_number):
    # crea un alien y lo coloca en la fila
    alien = Alien(service_configuraciones, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * (alien.rect.height * row_number)
    aliens.add(alien)


def crear_flota(service_configuraciones, pantalla, nave, aliens):
    """Se crean la flota de aliens y se ajusta el espacio entre ellos"""
    alien = Alien(service_configuraciones, pantalla)

    number_aliens_x = get_number_aliens_x(service_configuraciones, alien.rect.width)
    number_rows = get_number_rows(service_configuraciones, nave.rect.height, alien.rect.height)

    # crea la flota de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            crear_alien(service_configuraciones, pantalla, aliens, alien_number, row_number)


def change_fleet_direction(service_configuraciones, aliens):
    """Desciende toda la flota y cambia la dirección de la flota"""
    for alien in aliens.sprites():
        alien.rect.y += service_configuraciones.fleet_drop_speed
    service_configuraciones.fleet_direction *= -1


def check_fleet_edges(service_configuraciones, aliens):
    """Responde de forma apropiada si algún alien ha llegado a un borde"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(service_configuraciones, aliens)
            break


def update_aliens(service_configuraciones,nave,aliens):
    # actualiza las posiciones de los aliens
    check_fleet_edges(service_configuraciones, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(nave, aliens):
        pass