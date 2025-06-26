class Sudoku:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.fijas = [[False for _ in range(9)] for _ in range(9)]

    def cargar_tablero(self, tablero):
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = tablero[i][j]
                if tablero[i][j] != 0:
                    self.fijas[i][j] = True

    def insertar_numero(self, fila, col, numero):
        if self.fijas[fila][col]:
            return False
        if not (1 <= numero <= 9):
            return False
        self.grid[fila][col] = numero
        return True

    def validar_fila(self, fila):
        numeros = [n for n in self.grid[fila] if n != 0]
        return len(numeros) == len(set(numeros))

    def validar_columna(self, col):
        numeros = [self.grid[f][col] for f in range(9) if self.grid[f][col] != 0]
        return len(numeros) == len(set(numeros))

    def validar_bloque(self, fila, col):
        numeros = []
        start_f, start_c = 3 * (fila // 3), 3 * (col // 3)
        for i in range(start_f, start_f + 3):
            for j in range(start_c, start_c + 3):
                val = self.grid[i][j]
                if val != 0:
                    numeros.append(val)
        return len(numeros) == len(set(numeros))

    def validar_casilla(self, fila, col):
        return self.validar_fila(fila) and self.validar_columna(col) and self.validar_bloque(fila, col)

    def validar_tablero(self):
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
        # Ejemplos básicos de tableros prediseñados
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
        # Se pueden agregar más niveles como 'medio' o 'dificil'
        return [[0]*9 for _ in range(9)]