import pygame
import time
from sudoku import Sudoku

pygame.init()

ANCHO, ALTO = 540, 640
TAM_CELDA = ANCHO // 9
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sudoku TDD")

fuente = pygame.font.SysFont("comicsans", 40)
fuente_tiempo = pygame.font.SysFont("comicsans", 30)

def guardar_puntaje(nombre, tiempo, nivel, clasificacion):
    # Punto 5 TDD - Guardado de datos
    with open("puntajes.txt", "a") as f:
        f.write(f"{nombre},{tiempo},{nivel},{clasificacion}\n")

def clasificar_tiempo(segundos):
    if segundos < 600:
        return "Oro"
    elif segundos <= 900:
        return "Plata"
    else:
        return "Bronce"

# PANTALLA DE MENÚ (cumple parte del punto 5)
def mostrar_menu_dificultad():
    seleccion = None
    while seleccion is None:
        pantalla.fill(BLANCO)
        texto = fuente.render("Seleccione dificultad:", True, NEGRO)
        pantalla.blit(texto, (100, 200))

        facil = fuente.render("1 - Fácil", True, AZUL)
        medio = fuente.render("2 - Medio", True, AZUL)
        dificil = fuente.render("3 - Difícil", True, AZUL)

        pantalla.blit(facil, (150, 260))
        pantalla.blit(medio, (150, 320))
        pantalla.blit(dificil, (150, 380))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    seleccion = "facil"
                elif evento.key == pygame.K_2:
                    seleccion = "medio"
                elif evento.key == pygame.K_3:
                    seleccion = "dificil"
    return seleccion

nivel = mostrar_menu_dificultad()

sudoku = Sudoku()
tablero_inicial = sudoku.generar_tablero_dificultad(nivel)
sudoku.cargar_tablero(tablero_inicial)

seleccion = None
inicio = time.time()
juego_completado = False
mensaje_clasificacion = ""
error = ""

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

    tiempo = int(time.time() - inicio)
    minutos = tiempo // 60
    segundos = tiempo % 60
    tiempo_texto = fuente_tiempo.render(f"Tiempo: {minutos:02}:{segundos:02}", True, NEGRO)
    pantalla.blit(tiempo_texto, (10, 560))

    if error:
        error_text = fuente_tiempo.render(error, True, ROJO)
        pantalla.blit(error_text, (10, 600))

    if juego_completado:
        texto = fuente.render("¡Sudoku Completado!", True, ROJO)
        pantalla.blit(texto, (50, 550))
        clasif_texto = fuente_tiempo.render(mensaje_clasificacion, True, ROJO)
        pantalla.blit(clasif_texto, (50, 600))

    pygame.display.flip()

ejecutando = True
while ejecutando:
    dibujar_tablero()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        elif evento.type == pygame.KEYDOWN and seleccion and not juego_completado:
            if evento.unicode.isdigit() and int(evento.unicode) != 0:
                fila, col = seleccion
                num = int(evento.unicode)
                if sudoku.insertar_numero(fila, col, num):
                    if not sudoku.validar_casilla(fila, col):
                        error = "Número inválido en fila/columna/bloque."
                        sudoku.grid[fila][col] = 0
                    else:
                        error = ""
                else:
                    error = "No se puede modificar esta casilla."

                if sudoku.validar_tablero():
                    tiempo_final = int(time.time() - inicio)
                    clasificacion = clasificar_tiempo(tiempo_final)
                    mensaje_clasificacion = f"Clasificación: {clasificacion}. Tiempo: {tiempo_final} s. Dificultad: {nivel}"
                    guardar_puntaje("Jugador", tiempo_final, nivel, clasificacion)
                    juego_completado = True

        elif evento.type == pygame.MOUSEBUTTONDOWN and not juego_completado:
            x, y = pygame.mouse.get_pos()
            if y < ANCHO:
                fila = y // TAM_CELDA
                col = x // TAM_CELDA
                seleccion = (fila, col)

pygame.quit()
