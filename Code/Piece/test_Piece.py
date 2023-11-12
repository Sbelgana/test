import unittest
import os
import sys
import tempfile

from Piece import*

class TestPiece(unittest.TestCase):

    def test_initialisation_piece(self):
        piece = Piece(TypePiece.ROI, Couleur.BLANC)
        self.assertEqual(piece.type, TypePiece.ROI)
        self.assertEqual(piece.couleur, Couleur.BLANC)

        piece = Piece(TypePiece.DAME, Couleur.NOIR)
        self.assertEqual(piece.type, TypePiece.DAME)
        self.assertEqual(piece.couleur, Couleur.NOIR)

    def test_attributs_piece(self):
        piece = Piece(TypePiece.FOU, Couleur.BLANC)
        self.assertTrue(hasattr(piece, 'type'))
        self.assertTrue(hasattr(piece, 'couleur'))

if __name__ == '__main__':
    if not os.path.exists('Code/Piece/logs'):
        os.mkdir('Code/Piece/logs')
    with open('Code/Piece/logs/tests_results_Piece.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)


