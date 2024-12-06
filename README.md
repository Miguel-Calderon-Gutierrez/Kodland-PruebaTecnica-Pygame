# 🎮 **Juego Invasión de Aliens** 🎮

¡Bienvenido a **Juego Invasión de Aliens**! Este proyecto es un emocionante juego desarrollado en **Python** utilizando la librería **PyGame**, creado como parte de la **prueba técnica de Kodland** para la vacante de **profesor de Python**. La misión principal del jugador es enfrentarse a una invasión alienígena mientras mejora sus habilidades y supera desafíos.

---

## **🚀 Descripción del Proyecto**

El juego incluye:
- Una nave controlada por el jugador para derrotar flotas de alienígenas.
- Balas disparadas por la nave, que pueden destruir a los alienígenas.
- Incremento gradual en la dificultad a medida que avanzas de nivel.
- Estadísticas como puntaje, niveles y vidas restantes.
- Un sistema de **mejor puntaje** que motiva al jugador a mejorar.

---

## **📂 Estructura del Proyecto**

```
Kodland-PruebaTecnica-Pygame
├── main.py               # Archivo principal que ejecuta el juego
├── configuraciones.py    # Configuración del juego (pantalla, colores, etc.)
├── estadisticas.py       # Gestión de las estadísticas del juego
├── nave.py               # Control de la nave del jugador
├── bala.py               # Control de las balas disparadas
├── alien.py              # Lógica de los alienígenas
├── funciones_juego.py    # Lógica general del juego
├── button.py             # Creación y manejo del botón de inicio
├── marcador.py           # Manejo y visualización de las estadísticas
├── imagenes/             # Carpeta con las imágenes del juego
│   ├── alien.bmp         # Imagen del alienígena
│   └── nave.bmp          # Imagen de la nave
├── README.md             # Documentación del proyecto
```

---

## **🔧 Configuración Inicial**

### **1. Requisitos**
- Python 3.8 o superior
- PyGame 2.0 o superior

### **2. Instalación**
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Miguel-Calderon-Gutierrez/Kodland-PruebaTecnica-Pygame.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Kodland-PruebaTecnica-Pygame
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install pygame
   ```

---

## **▶️ Cómo Ejecutar el Juego**

1. Asegúrate de estar en el directorio raíz del proyecto.
2. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```
3. ¡Enfréntate a la invasión alienígena y alcanza el puntaje más alto!

---

## **🛠️ Configuración Personalizable**

Puedes personalizar diversos aspectos del juego modificando el archivo `configuraciones.py`. Aquí algunos parámetros destacados:

| Parámetro              | Descripción                       | Valor Actual              |
|------------------------|-----------------------------------|---------------------------|
| `screen_width`         | Ancho de la pantalla             | 990 px                    |
| `screen_height`        | Alto de la pantalla              | 690 px                    |
| `bg_color`             | Color de fondo (RGB)             | `(9, 0, 38)`              |
| `name_game`            | Título del juego                 | `Juego invasión de aliens - Miguel Calderon` |
| `bala_factor_velocidad`| Velocidad de las balas           | 3                         |
| `balas_allowed`        | Número máximo de balas en pantalla| 10                        |
| `alien_speed_factor`   | Velocidad inicial de los aliens  | 1                         |
| `fleet_drop_speed`     | Velocidad con la que los aliens descienden | 10            |
| `cantidad_naves`       | Número de vidas iniciales        | 2                         |

---

## **📊 Sistema de Estadísticas**

El juego incluye un sistema de estadísticas para que los jugadores puedan medir su progreso:

1. **Puntaje:** Se incrementa al eliminar alienígenas.
2. **Mejor Puntaje:** Almacena el puntaje más alto alcanzado.
3. **Nivel:** Aumenta a medida que el jugador elimina flotas completas.
4. **Vidas Restantes:** Representa la cantidad de naves disponibles.

Las estadísticas se visualizan dinámicamente durante el juego, gracias a la integración con `marcador.py`.

---

## **📜 Código Principal**

El archivo principal `main.py` inicializa el juego y contiene el bucle principal. También gestiona las interacciones entre los componentes.

**Fragmento del Bucle Principal:**
```python
while True:
    fj.verificar_eventos(service_configuraciones, pantalla, estadisticas, marcador, play_button, nave, aliens, balas)
    if estadisticas.game_active:
        nave.update()
        fj.updata_balas(service_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas)
        fj.update_aliens(service_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas)
    fj.actualizar_pantalla(service_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas, play_button)
```

---

## **🎨 Recursos Visuales**

El juego utiliza las siguientes imágenes, ubicadas en la carpeta `imagenes/`:
- **`alien.bmp`:** Representa a los alienígenas.
- **`nave.bmp`:** Representa la nave del jugador.

---

## **👨‍💻 Acerca del Desarrollador**

Este proyecto fue creado por **Miguel Calderón** como parte de una prueba técnica para **Kodland**. Si tienes alguna duda o sugerencia, ¡no dudes en contactarme! 😊

- 📧 Email: [miguelcalderon.dev@gmail.com](mailto:miguelcalderon.dev@gmail.com)
- 🐙 GitHub: [Miguel-Calderon-Gutierrez](https://github.com/Miguel-Calderon-Gutierrez)

---

¡Gracias por visitar este proyecto! Si te gustó, ⭐️ dale una estrella en GitHub. 