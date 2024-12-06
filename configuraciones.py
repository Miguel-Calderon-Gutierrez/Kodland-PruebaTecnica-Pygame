class Configuraciones():

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 750
        self.bg_color = (9, 0, 38)
        self.name_game = "Juego invasión de aliens - Miguel Calderon"

        # configuraciones de la nave
        self.factor_velocidad_nave = 1
        self.cantidad_naves = 2

        # configuraciones de balas
        self.bala_factor_velocidad = 3
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 252, 163, 45
        self.balas_allowed = 2

        # configuraciones de alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction 1 derecha, -1 izquierda
        self.fleet_direction = 1
