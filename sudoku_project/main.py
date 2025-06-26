import pygame
from sudoku import Sudoku
import time

pygame.init()

ANCHO, ALTO = 540, 600
TAM_CELDA = ANCHO // 9
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sudoku TDD")

fuente = pygame.font.SysFont("comicsans", 40)
fuente_tiempo = pygame.font.SysFont("comicsans", 30)

sudoku = Sudoku()
tablero_inicial = sudoku.obtener_tablero_dificultad('facil')
sudoku.cargar_tablero(tablero_inicial)

seleccion = None
inicio = time.time()

# Función para dibujar el tablero y los números
def dibujar_tablero():
    pantalla.fill(BLANCO)
    for i in range(9):
        for j in range(9):
            num = sudoku.grid[i][j]
            if num != 0:
                color = NEGRO if sudoku.fijas[i][j] else AZUL
                texto = fuente.render(str(num), True, color)
                pantalla.blit(texto, (j * TAM_CELDA + 20, i * TAM_CELDA + 10))

    for i in range(10):
        grosor = 3 if i % 3 == 0 else 1
        pygame.draw.line(pantalla, NEGRO, (0, i * TAM_CELDA), (ANCHO, i * TAM_CELDA), grosor)
        pygame.draw.line(pantalla, NEGRO, (i * TAM_CELDA, 0), (i * TAM_CELDA, ANCHO), grosor)

    if seleccion:
        fila, col = seleccion
        pygame.draw.rect(pantalla, AZUL, (col * TAM_CELDA, fila * TAM_CELDA, TAM_CELDA, TAM_CELDA), 3)

    if sudoku.validar_tablero():
        texto = fuente.render("¡Sudoku Completado!", True, ROJO)
        pantalla.blit(texto, (100, 550))

    tiempo = int(time.time() - inicio)
    minutos = tiempo // 60
    segundos = tiempo % 60
    tiempo_texto = fuente_tiempo.render(f"Tiempo: {minutos:02}:{segundos:02}", True, NEGRO)
    pantalla.blit(tiempo_texto, (10, 560))

    pygame.display.flip()

# Bucle principal
ejecutando = True
while ejecutando:
    dibujar_tablero()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if y < ANCHO:
                fila = y // TAM_CELDA
                col = x // TAM_CELDA
                seleccion = (fila, col)
        elif evento.type == pygame.KEYDOWN and seleccion:
            if evento.unicode.isdigit():
                num = int(evento.unicode)
                fila, col = seleccion
                sudoku.insertar_numero(fila, col, num)

pygame.quit()
