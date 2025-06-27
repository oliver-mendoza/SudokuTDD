import unittest
from sudoku import Sudoku
class TestSudoku(unittest.TestCase):
    def test_validar_fila_valida(self):
        # → Parte 3: Test que falla (Rojo) → luego Green → Refactor
        s = Sudoku()
        s.grid[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(s.validar_fila(0))
    def test_validar_fila_con_repetidos(self):
        # → Parte 3: Test para validar filas incorrectas
        s = Sudoku()
        s.grid[0] = [1, 2, 3, 4, 5, 5, 7, 8, 9]
        self.assertFalse(s.validar_fila(0))
    def test_validar_columna_con_repetidos(self):
        # → Parte 3: Test para validar columnas incorrectas
        s = Sudoku()
        s.grid[0][0] = 1
        s.grid[5][0] = 1
        self.assertFalse(s.validar_columna(0))
    def test_validar_bloque_con_repetidos(self):
        # → Parte 3: Test para validar bloques incorrectos
        s = Sudoku()
        s.grid[0][0] = 9
        s.grid[1][1] = 9
        self.assertFalse(s.validar_bloque(0, 0))
    def test_insertar_numero_en_fija(self):
        # → Parte 3 y Parte 4: Test para asegurar que las celdas fijas no se pueden modificar
        s = Sudoku()
        tablero = s.obtener_tablero_dificultad()
        s.cargar_tablero(tablero)
        self.assertFalse(s.insertar_numero(0, 0, 3))
    def test_insertar_numero_valido(self):
        # → Parte 3 y Parte 4: Test para insertar un número en celda vacía
        s = Sudoku()
        self.assertTrue(s.insertar_numero(0, 0, 5))
        self.assertEqual(s.grid[0][0], 5)
    def test_validar_tablero_incompleto(self):
        # → Parte 3 y Parte 4: Test para verificar que el tablero incompleto no es válido
        s = Sudoku()
        tablero = s.obtener_tablero_dificultad()
        s.cargar_tablero(tablero)
        self.assertFalse(s.validar_tablero())
if __name__ == "__main__":
    unittest.main()