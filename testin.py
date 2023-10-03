import pygame

# Configuración del tablero (ancho y alto de la ventana, tamaño de cada celda)
ANCHO = 600
ALTO = 600
TAMANO_CELDA = 60
CANTIDAD_CELDAS = 10

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

# Función para dibujar el tablero con las naves y la cuadrícula
def dibujar_tablero(tablero, pantalla, celda_clicada=None):
    for fila in range(CANTIDAD_CELDAS):
        for columna in range(CANTIDAD_CELDAS):
            pygame.draw.rect(pantalla, (0,0,0), (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA), 1)  # Dibujar cuadrícula
            if tablero[fila][columna] == '■':
                pygame.draw.rect(pantalla, AZUL, (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))  # Dibujar nave
            if celda_clicada and fila == celda_clicada[0] and columna == celda_clicada[1]:
                pygame.draw.rect(pantalla, ROJO, (columna * TAMANO_CELDA, fila * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))  # Dibujar celda clicada en rojo

# Función principal
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Batalla Naval')

    # Tu matriz de tablero con las naves
    tablero = [['⬞' for _ in range(10)] for _ in range(10)]


    reloj = pygame.time.Clock()
    ejecutando = True

    celda_clicada = None  # Almacena la fila y columna de la celda clicada

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Detecta clic izquierdo del mouse
                x, y = pygame.mouse.get_pos()
                fila_clicada = y // TAMANO_CELDA
                columna_clicada = x // TAMANO_CELDA
                if fila_clicada < CANTIDAD_CELDAS and columna_clicada < CANTIDAD_CELDAS:
                    celda_clicada = (fila_clicada, columna_clicada)  # Almacena la celda clicada

        pantalla.fill(BLANCO)  # Limpiar la pantalla
        dibujar_tablero(tablero, pantalla, celda_clicada)  # Dibujar el tablero con las naves y la cuadrícula
        pygame.display.flip()  # Actualizar la pantalla

        reloj.tick(60)  # Limitar la velocidad de fotogramas

    pygame.quit()

if __name__ == "__main__":
    main()