import unittest
from resolver import *

grille_test = [[0, 1, 0, 2, 3, 4, 0, 0, 0],
               [3, 0, 0, 5, 0, 6, 0, 1, 0],
               [7, 0, 0, 8, 0, 0, 6, 0, 2],
               [2, 0, 9, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 0, 0, 0, 0, 4],
               [0, 7, 0, 0, 0, 0, 3, 0, 9],
               [4, 0, 6, 0, 0, 2, 0, 0, 7],
               [0, 5, 0, 1, 0, 8, 0, 0, 3],
               [0, 0, 0, 4, 9, 7, 0, 8, 0]]

grille_solution = [[6, 1, 8, 2, 3, 4, 9, 7, 5],
                   [3, 9, 2, 5, 7, 6, 4, 1, 8],
                   [7, 4, 5, 8, 1, 9, 6, 3, 2],
                   [2, 3, 9, 7, 4, 5, 8, 6, 1],
                   [8, 6, 1, 9, 2, 3, 7, 5, 4],
                   [5, 7, 4, 6, 8, 1, 3, 2, 9],
                   [4, 8, 6, 3, 5, 2, 1, 9, 7],
                   [9, 5, 7, 1, 6, 8, 2, 4, 3],
                   [1, 2, 3, 4, 9, 7, 5, 8, 6]]

class TestSudokuMethods(unittest.TestCase):

    def test_absentSurLigne(self):
        self.assert_absentSurLigne(True, 5, 0)
        self.assert_absentSurLigne(False, 1, 1)

    def test_absentSurColonne(self):
        self.assert_absentSurColonne(True, 2, 2)
        self.assert_absentSurColonne(False, 8, 3)

    def test_absentSurBloc(self):
        self.assert_absentSurBloc(True, 6, 4, 3)
        self.assert_absentSurBloc(False, 9, 5, 7)

    def test_estValide(self):
        #self.assert_estValide(True, 0)
        #self.assert_estValide(True, 0, grille=grille_test)
        self.assert_estValide(False, 0, grille=[
            [6, 6, 6, 2, 3, 4, 9, 7, 5],
            [3, 9, 2, 5, 7, 6, 4, 1, 8],
            [7, 4, 5, 8, 1, 9, 6, 3, 2],
            [2, 3, 9, 7, 4, 5, 8, 6, 1],
            [8, 6, 1, 9, 2, 3, 7, 5, 4],
            [5, 7, 4, 6, 8, 1, 3, 2, 9],
            [4, 8, 6, 3, 5, 2, 1, 9, 7],
            [9, 5, 7, 1, 6, 8, 2, 4, 3],
            [1, 2, 3, 4, 9, 7, 5, 8, 6]])
        self.assert_estValide(False, 0, grille=[
            [0, 0, 0, 2, 3, 4, 9, 7, 5],
            [3, 9, 2, 5, 7, 6, 4, 1, 8],
            [7, 4, 5, 8, 1, 9, 6, 3, 2],
            [9, 9, 9, 7, 4, 5, 8, 6, 1],
            [8, 6, 1, 9, 2, 3, 7, 5, 4],
            [5, 7, 4, 6, 8, 1, 3, 2, 9],
            [4, 8, 6, 3, 5, 2, 1, 9, 7],
            [9, 5, 7, 1, 6, 8, 2, 4, 3],
            [1, 2, 3, 4, 9, 7, 5, 8, 6]])

    # -----------------


    def assert_estValide(self, expected, position, grille=grille_solution):
        self.assertEqual(expected, estValide(copy.deepcopy(grille), position))

    def assert_absentSurLigne(self, expected, chiffre, ligne, grille=grille_test):
        self.assertEqual(expected, absentSurLigne(chiffre, grille, ligne))

    def assert_absentSurColonne(self, expected, chiffre, colonne, grille=grille_test):
        self.assertEqual(expected, absentSurColonne(chiffre, grille, colonne))

    def assert_absentSurBloc(self, expected, chiffre, ligne, colonne, grille=grille_test):
        self.assertEqual(expected, absentSurBloc(chiffre, grille, ligne, colonne))



if __name__ == '__main__':
    unittest.main()
