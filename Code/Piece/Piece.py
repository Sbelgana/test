import sys
import os

chemin_dossier_1 = './Code/Couleur'
chemin_dossier_2 = './Code/TypePiece'

if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)
if chemin_dossier_2 not in sys.path:
    sys.path.append(chemin_dossier_2)

from Couleur import*
from TypePiece import*

class Piece:
    def __init__(self, type_piece, couleur):
        pass
