class Estadisticas():
	"""Seguimiento de las estadísticas de Invasión Alienígena"""
	def __init__(self, service_configuraciones):
		"""Inicializa las estadísticas"""
		self.service_configuraciones = service_configuraciones
		self.reset_stats()

		# Inicia Invasión Alienígena en un estado activo
		self.game_active = True

		# La puntuación alta nunca debe restablecerse
		self.alto_puntaje = 0


	def reset_stats(self):
		"""Inicializa estadísticas que pueden cambiar durante el juego"""
		self.naves_restantes = self.service_configuraciones.cantidad_naves
		self.puntaje = 0
		self.nivel = 1
		