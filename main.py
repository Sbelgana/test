from Couleur import*
from CasePlateau import*
from Piece import*
from Pos import*
from TypePiece import*
from Plateau import*
from Interface import*
from JeuEchec import*

def jouer_partie(jeu):
    jeu.plateau.init_partie()
    jeu.interface.affiche_liste_piece(jeu.plateau.liste_piece())

    while not jeu.est_echec_et_mat(jeu.joueurCourant):

        jeu.tour_joueur_courant()
        jeu.joueurCourant = Couleur.NOIR if jeu.joueurCourant == Couleur.BLANC else Couleur.BLANC
        print(jeu.joueurCourant)
        if jeu.est_echec(jeu.joueurCourant):
            jeu.interface.place_curseur_roi(jeu.pos_roi_joueur(jeu.joueurCourant).get_emplacement)


if __name__ == '__main__':   
    jeu = JeuEchec()
    jeu.plateau.init_partie()
    jouer_partie(jeu)