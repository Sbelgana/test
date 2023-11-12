import sys
import os

chemin_dossier_1 = os.path.dirname(os.path.realpath(__file__)) + '/../Plateau'
chemin_dossier_2 = os.path.dirname(os.path.realpath(__file__)) + '/../Interface'


if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)
if chemin_dossier_2 not in sys.path:
    sys.path.append(chemin_dossier_2)


from Plateau import*
from Interface import*


class JeuEchec:

    def __init__(self):
        pass

    def est_case_joueur(self, pos, joueur):
        pass

    def est_case_joueur_inverse(self, pos, joueur):
        pass

    def liste_mouvement_cavalier(self, pos):
        pass

    def liste_mouvement_fou(self, pos):
        pass

    def liste_mouvement_tour(self, pos):
        pass

    def liste_mouvement_dame(self, pos):
        pass

    def liste_mouvement_roi(self, pos, juste_mouvement=False):
        pass

    def liste_mouvement_pion(self, pos):
        pass



    def liste_mouvement_valide(self, pos_depart, liste_move):
        pass

    def liste_mouvement_joueur(self, joueur, juste_mouvement=False):
        pass

    def liste_mouvement_pos(self, pos, juste_mouvement=False):
        pass

    def pos_roi_joueur(self, joueur):
        pass

    # Founie 
    def est_echec(self, joueur):
        pos_roi = self.pos_roi_joueur(joueur)
        return Pos.est_dans_liste_pos(pos_roi, self.liste_mouvement_joueur(~(joueur)))


    def est_echec_et_mat(self, joueur):
        position_roi = self.pos_roi_joueur(joueur)
        liste_mouvements_roi = self.liste_mouvement_roi(position_roi)

        # Vérifier si au moins un mouvement du roi est sûr.
        for mouvement_roi in liste_mouvements_roi:
            if not self.est_en_echec_apres_mouvement(position_roi, mouvement_roi, joueur):
                return False

        # Si le roi ne peut pas bouger, vérifier si d'autres pièces peuvent sauver la situation.
        for i in range(1, self.plateau.NLIGNES + 1):
            for j in range(1, self.plateau.NCOLONNES + 1):
                pos_piece = Pos(i, j)
                if self.plateau.est_case_occupe(pos_piece) and self.est_case_joueur(pos_piece, joueur):
                    liste_mouvements_piece = self.liste_mouvement_pos(pos_piece)
                    for mouvement_piece in liste_mouvements_piece:
                        if not self.est_en_echec_apres_mouvement(pos_piece, mouvement_piece, joueur):
                            return False

        # Si aucune pièce ne peut sauver le roi, c'est un échec et mat.
        if self.est_echec(joueur):
            self.interface.place_curseur_roi(self.pos_roi_joueur(joueur).get_emplacement, checkmate=True)
            return True

        return False

    def est_en_echec_apres_mouvement(self, pos_depart, pos_fin, joueur):
        piece_capturee = self.plateau.piece_a_position(pos_fin)
        self.plateau.bouge_piece(pos_depart, pos_fin)
        echec = self.est_echec(joueur)
        self.plateau.bouge_piece(pos_fin, pos_depart)
        self.plateau.ajoute_piece(piece_capturee, pos_fin)
        return echec

    def isEmplacementDepartValide(self, pos):
        
        return self.plateau.est_case_occupe(pos) and self.plateau.matCases[pos.ligne- 1][pos.colonne- 1].piece.couleur == self.joueurCourant and \
                (not(self.est_echec(self.joueurCourant)) or self.plateau.matCases[pos.ligne - 1][pos.colonne - 1].piece.type == TypePiece.ROI)

    def tour_joueur_courant(self):
        # Sélection de la pièce à déplacer
        flag = True
        while flag:
            emplacement_depart = self.interface.saisir_emplacement()
            pos_depart = Pos(emplacement_depart)
            if self.isEmplacementDepartValide(pos_depart):
                flag = False

        # Sélection de la destination et déplacement de la pièce
        flag = True
        while flag:
            valid_moves = self.liste_mouvement_valide(pos_depart, self.liste_mouvement_pos(pos_depart))
            for move in valid_moves:
                self.interface.place_curseur(move.get_emplacement)
            self.interface.affiche_liste_piece()

            emplacement_fin = self.interface.saisir_emplacement()
            pos_fin = Pos(emplacement_fin)
            
            if emplacement_depart != emplacement_fin:
                if Pos.est_dans_liste_pos(pos_fin, valid_moves):
                   flag = False
                elif self.plateau.est_case_occupe(pos_fin) and self.plateau.matCases[pos_fin.ligne - 1][pos_fin.colonne - 1].piece.couleur == self.joueurCourant:
                    self.interface.enleve_curseur()
                    emplacement_depart = emplacement_fin
                    pos_depart = Pos(emplacement_depart)            

        # Ajoutez piece mangee dans interface
        self.interface.piece_mangee(emplacement_fin)
        # On bouge la pièce
        self.plateau.bouge_piece(pos_depart, pos_fin)   
        # Enlève le curseur
        self.interface.enleve_curseur()             
        # Vérifiez si le pion atteint la dernière rangée pour la promotion
        self.promotePawn(pos_fin)
        # Update board
        self.interface.affiche_liste_piece(self.plateau.liste_piece())

