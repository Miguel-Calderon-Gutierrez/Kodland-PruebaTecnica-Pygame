class Configuraciones():

    def __init__(self):
        self.screen_width = 990
        self.screen_height = 690
        self.bg_color = (9, 0, 38)
        self.name_game = "Juego invasión de aliens - Miguel Calderon"

        # configuraciones de la nave
        self.factor_velocidad_nave = 1.5
        self.cantidad_naves = 2

        # configuraciones de balas
        self.bala_factor_velocidad = 3
        self.bala_width = 3
        self.bala_height = 10
        self.bala_color = 252, 163, 45
        self.balas_allowed = 10

        # configuraciones de alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.escala_aceleracion = 0.5
        self.puntos_alien = 50

        # Qué tan rápido se acelera el juego
        self.escala_aceleracion = 1.1
        # Qué tan rápido aumentan los valores de puntos por aliens
        self.escala_puntaje = 1.5

        self.inicializa_configuraciones_dinamicas()

        # fleet direction 1 derecha, -1 izquierda
        self.fleet_direction = 1

    def inicializa_configuraciones_dinamicas(self):
        """Inicializa la configuración que cambia a lo largo del juego"""
        self.factor_velocidad_nave = 1.5
        self.bala_factor_velocidad = 3
        self.alien_speed_factor = 1
        # fleet_direction, si es 1 representa a la derecha; si es -1 representa a la izquierda
        self.fleet_direction = 1
        # Puntuación
        self.puntos_alien = 50

    def aumentar_velocidad(self):
        """Aumenta la configuración de velocidad y los valores de puntos por aliens"""
        self.factor_velocidad_nave *= self.escala_aceleracion
        self.bala_factor_velocidad *= self.escala_aceleracion
        self.alien_speed_factor *= self.escala_aceleracion

        self.puntos_alien = int(self.puntos_alien * self.escala_puntaje)
