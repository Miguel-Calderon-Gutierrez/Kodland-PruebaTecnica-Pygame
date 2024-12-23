import sys
import pygame
from bala import Bala
from alien import Alien
from time import sleep


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


def verificar_eventos(service_configuraciones, pantalla, estadisticas, marcador, play_button, nave, aliens, balas):
    # Escuchar eventos de teclado o del mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, service_configuraciones, pantalla, nave, balas)
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(service_configuraciones, pantalla, estadisticas, marcador, play_button, nave, aliens,
                              balas,
                              mouse_x, mouse_y)


def check_play_button(service_configuraciones, pantalla, estadisticas, marcador, play_button, nave, aliens, balas,
                      mouse_x,
                      mouse_y):
    """Comienza un nuevo juego cuando el jugador hace clic en Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not estadisticas.game_active:
        # Restablece la configuración del juego
        service_configuraciones.inicializa_configuraciones_dinamicas()

        # Ocultar el cursor del ratón
        pygame.mouse.set_visible(False)

        # Restablece las estadísticas del juego
        estadisticas.reset_stats()
        estadisticas.game_active = True

        # Restablece las imágenes de marcador
        marcador.prep_puntaje()
        marcador.prep_alto_puntaje()
        marcador.prep_nivel()
        marcador.prep_naves()

        # Vacía la lista de aliens y balas
        aliens.empty()
        balas.empty()

        # Crea una nueva flota y centra la nave
        crear_flota(service_configuraciones, pantalla, nave, aliens)
        nave.centrar_nave()


def actualizar_pantalla(service_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas, play_button):
    # Actualiza la pantalla cada pasada por el bucle
    pantalla.fill(service_configuraciones.bg_color)
    # vuelve a dibujar todas la balas
    for bala in balas.sprites():
        bala.draw_bala()
    # Se dibuja la nave
    nave.blitme()
    # Se dibuja el alien
    aliens.draw(pantalla)

    # se dibuja el marcador
    marcador.muestra_puntaje()

    if not estadisticas.game_active:
        play_button.draw_button()

    # Hacer visible la pantalla
    pygame.display.flip()


def updata_balas(service_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas):
    # actualiza las balas y elimina las antiguas
    balas.update()
    # Eliminar balas que salen de rango
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    check_bala_alien_collisions(service_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas)


def check_bala_alien_collisions(service_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas):
    """Elimina las balas y los aliensque choquen"""
    collisions = pygame.sprite.groupcollide(balas, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            estadisticas.puntaje += service_configuraciones.puntos_alien * len(aliens)
            marcador.prep_puntaje()
        verifica_alto_puntaje(estadisticas, marcador)

    if len(aliens) == 0:
        # Si se destruye toda la flota, comienza un nuevo nivel
        balas.empty()
        service_configuraciones.aumentar_velocidad()

        # Incrementa el nivel
        estadisticas.nivel += 1
        marcador.prep_nivel()

        crear_flota(service_configuraciones, pantalla, nave, aliens)


def verifica_alto_puntaje(estadisticas, marcador):
    """Verifica si existe un puntaje más alto"""
    if estadisticas.puntaje > estadisticas.alto_puntaje:
        estadisticas.alto_puntaje = estadisticas.puntaje
        marcador.prep_alto_puntaje()


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


def check_aliens_bottom(service_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas):
    """Comprueba si algún alien ha llegado al final de la pantalla"""
    pantalla_rect = pantalla.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= pantalla_rect.bottom:
            # Trata esto de la misma forma que si la nave fuera golpeada
            nave_golpeada(service_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas)
            break


def update_aliens(service_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas):
    """Comprueba si la flota está al borde y luego actualiza las posiciones de todos los aliens de la flota"""
    check_fleet_edges(service_configuraciones, aliens)
    aliens.update()

    # Busca colisiones de alien-nave
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_golpeada(service_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas)

    # Busca aliens que golpean la parte inferior de la pantalla
    check_aliens_bottom(service_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas)


def nave_golpeada(service_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas):
    """Responde a una nave siendo golpeada por un alien"""

    if estadisticas.naves_restantes > 0:
        # Disminuye naves_restantes
        estadisticas.naves_restantes -= 1

        # Actualiza el marcador
        marcador.prep_naves()

        # Vacía la lista de aliens y balas
        aliens.empty()
        balas.empty()

        # Crea una nueva flota y centra la nave
        crear_flota(service_configuraciones, pantalla, nave, aliens)
        nave.centrar_nave()

        # Pausa
        sleep(0.5)

    else:
        estadisticas.game_active = False
        pygame.mouse.set_visible(True)
