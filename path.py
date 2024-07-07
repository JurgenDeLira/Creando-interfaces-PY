from pygameDemo import *
from pathlib import Path
# Pon esto en la sección #2, defininiendo una consante
BASE_PATH = Path(__file__).resolve().parent
 
# Construye una ruta absoluta para el archivo ball.png
pathToBall = str(BASE_PATH) + 'images / ball.png'

# 3 - Iniciamos el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 4 - Cargamos asssets: imagenes(s), sonido(s), etc.
ballImage = pygame.image.load(str(pathToBall))
# 5 - Inicializamos variables
# --- recorte ---
    # 10 - Dibujar todos los elementos de la ventana
window.blit(ballImage, (100, 200))
    # 11 - Actualizar la ventana
pygame.display.update()
    # 12 - Ralentizar un poco las cosas
clock.tick(FRAMES_PER_SECOND)