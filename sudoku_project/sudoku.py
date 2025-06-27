class Sudoku:
    def __init__(self):
        # → Parte 4: Agregando funcionalidad básica con código
        # Creamos una matriz vacía (tablero) de 9x9
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        # Guardamos qué celdas son fijas (no modificables)
        self.fijas = [[False for _ in range(9)] for _ in range(9)]
    def cargar_tablero(self, tablero):
        # → Parte 4: Agregando funcionalidad básica
        # Carga un tablero inicial y marca las posiciones fijas
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = tablero[i][j]
                if tablero[i][j] != 0:
                    self.fijas[i][j] = True
    def insertar_numero(self, fila, col, numero):
        # → Parte 4: Evitar modificar celdas fijas (reglas del juego)
        if self.fijas[fila][col]:
            return False
        # → Parte 4: Validar que solo se puedan ingresar números del 1 al 9
        if not (1 <= numero <= 9):
            return False
        self.grid[fila][col] = numero
        return True
    def validar_fila(self, fila):
        # → Parte 4: Validar la regla de no repetir en filas
        numeros = [n for n in self.grid[fila] if n != 0]
        return len(numeros) == len(set(numeros))
    def validar_columna(self, col):
        # → Parte 4: Validar la regla de no repetir en columnas
        numeros = [self.grid[f][col] for f in range(9) if self.grid[f][col] != 0]
        return len(numeros) == len(set(numeros))
    def validar_bloque(self, fila, col):
        # → Parte 4: Validar la regla de no repetir en bloques 3x3
        numeros = []
        start_f, start_c = 3 * (fila // 3), 3 * (col // 3)
        for i in range(start_f, start_f + 3):
            for j in range(start_c, start_c + 3):
                val = self.grid[i][j]
                if val != 0:
                    numeros.append(val)
        return len(numeros) == len(set(numeros))
    def validar_casilla(self, fila, col):
        # → Parte 4: Validar una sola casilla, combinando reglas
        return self.validar_fila(fila) and self.validar_columna(col) and self.validar_bloque(fila, col)
    def validar_tablero(self):
        # → Parte 4: Validar si el tablero completo está correcto
        for i in range(9):
            if not self.validar_fila(i) or not self.validar_columna(i):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not self.validar_bloque(i, j):
                    return False
        for fila in self.grid:
            if 0 in fila:
                return False
        return True
    def obtener_tablero_dificultad(self, nivel='facil'):
        # → Parte 1: Reglas del juego: Tableros iniciales con pistas
        # → Parte 4: Agregando funcionalidad básica
        # Retorna un tablero prediseñado (por ahora solo nivel fácil)
        if nivel == 'facil':
            return [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        # → Parte 4: A futuro se agregarán más niveles
        return [[0]*9 for _ in range(9)]