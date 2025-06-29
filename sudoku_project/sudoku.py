import random
import copy

class Sudoku:
    def __init__(self):
        # Punto 1 TDD - Reglas del juego:
        # Creamos un tablero 9x9 inicializado en ceros
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        # Matriz para marcar qué casillas son fijas (pistas)
        self.fijas = [[False for _ in range(9)] for _ in range(9)]

    def cargar_tablero(self, tablero):
        # Punto 3 TDD - Inicializa datos para probar reglas
        self.grid = copy.deepcopy(tablero)
        self.fijas = [[cell != 0 for cell in row] for row in tablero]

    def insertar_numero(self, fila, col, numero):
        # Punto 4 TDD - validación de entrada y reglas
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
        return (
                self.validar_fila(fila) and
                self.validar_columna(col) and
                self.validar_bloque(fila, col)
        )

    def validar_tablero(self):
        # Punto 4 TDD - validación de tablero completo
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

    def generar_tablero_completo(self):
        """
        Genera un tablero completo de sudoku (solución válida)
        Punto 5 TDD - Generación dinámica y aleatoria
        """
        def resolver():
            for i in range(9):
                for j in range(9):
                    if self.grid[i][j] == 0:
                        numeros = list(range(1, 10))
                        random.shuffle(numeros)
                        for num in numeros:
                            self.grid[i][j] = num
                            if self.validar_casilla(i, j) and resolver():
                                return True
                            self.grid[i][j] = 0
                        return False
            return True

        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        resolver()
        return copy.deepcopy(self.grid)

    def generar_tablero_dificultad(self, nivel="facil"):
        """
        Genera tablero aleatorio con pistas según dificultad.
        Cumple punto 5 TDD - niveles de dificultad.
        """
        tablero_completo = self.generar_tablero_completo()

        if nivel == "facil":
            vacias = random.randint(35, 45)
        elif nivel == "medio":
            vacias = random.randint(46, 55)
        else:
            vacias = random.randint(56, 60)

        tablero = copy.deepcopy(tablero_completo)
        celdas = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(celdas)
        for i, j in celdas[:vacias]:
            tablero[i][j] = 0

        return tablero
