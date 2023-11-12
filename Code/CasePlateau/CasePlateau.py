import sys
import os


chemin_dossier_1 = './Code/Piece'



if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)

from Piece import*


class CasePlateau:
    def __init__(self, piece=None):
        pass

    def est_occupe(self):
        pass