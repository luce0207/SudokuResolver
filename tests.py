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

# Attention: les indices commencent à 0 et non 1, ex: la 3e ligne de la grille correspond au sous-tableau d'indice 2.

def absentSurLigne(chiffre, grille, ligne):
    """
    :param chiffre: chiffre entre 1 et 9 dont on on cherche à vérifier l'absence sur une ligne de la grille
    :param grille: grille que l'on veut résoudre
    :param ligne: ligne sur laquelle on cherche à vérifier l'absence du chiffre
    :return: booléen vérifiant l'absence du chiffre sur la ligne
    """
    for j in grille[ligne]:
        if j == chiffre:
            return False
    return True

assert absentSurLigne(5, grille_test, 0) == True
assert absentSurLigne(1, grille_test, 1) == False



def absentSurColonne(chiffre, grille, colonne):
    """
        :param chiffre: chiffre entre 1 et 9 dont on on cherche à vérifier l'absence sur une colonne de la grille
        :param grille: grille que l'on veut résoudre
        :param colonne: colonne sur laquelle on cherche à vérifier l'absence du chiffre
        :return: booléen vérifiant l'absence du chiffre sur la colonne
    """
    for i in range(9):
        if grille[i][colonne] == chiffre:
            return False
    return True

assert absentSurColonne(2, grille_test, 2) == True
assert absentSurColonne(8, grille_test, 3) == False



def absentSurBloc(chiffre, grille, ligne, colonne):
    """
        :param chiffre: chiffre entre 1 et 9 dont on on cherche à vérifier l'absence sur un bloc de la grille
        :param grille: grille que l'on veut résoudre
        :param ligne: ligne appartenant au bloc
        :param colonne: colonne appartenant au bloc
        :return: booléen vérifiant l'absence du chiffre sur le bloc
    """
    ligneBloc = ligne - (ligne % 3)
    colonneBloc = colonne - (colonne % 3)
    for i in range(ligneBloc, ligneBloc + 3):
        for j in range(colonneBloc, colonneBloc + 3):
            if grille[i][j] == chiffre:
                return False
    return True

assert absentSurBloc(6, grille_test, 4, 3) == True
assert absentSurBloc(9, grille_test, 5, 7) == False



def estValide(grille, position):
    """
    :param grille: grille que l'on veut résoudre
    :param position: numéro de la case (de 0 à 80) à partir duquel on cherche à vérifier si la grille est valide, il sert d'itérateur pour parcourir la grille
    :return: booloéen indiquant si la grille est valide à partir de la position donnée
    """
    if position == 81: # Les indices vont de 0 à 80 mais pour prendre en compte la case 80, il faut aller jusqu'à 81
        return True
    ligne = position // 9
    colonne = position % 9
    if grille[ligne][colonne] != 0:
        return estValide(grille, position+1)
    for chiffre in range(1,10):
        if (absentSurLigne(chiffre, grille, ligne) and absentSurColonne(chiffre, grille, colonne) and absentSurBloc(chiffre, grille, ligne, colonne)):
            grille[ligne][colonne] = chiffre
            if estValide(grille, position+1):
                return True
            grille[ligne][colonne] = 0
    return False

assert estValide(grille_test, 0)



def resoudre_sudoku(grille):
    """
    :param grille: grille que l'on veut résoudre
    :return: grille complétée si une solution valide est trouvée, None sinon
    """
    if estValide(grille, 0):
        return grille
    else:
        return None

assert resoudre_sudoku(grille_test) == grille_solution