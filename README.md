<div align="justify">

## 1. Objectifs

Le jeu d'échecs est un jeu stratégique ancestral qui oppose deux joueurs sur un plateau. Chaque joueur dispose d'un ensemble de pièces ayant des mouvements et des fonctions spécifiques. Le principal objectif est de mettre le roi adverse en échec et mat, situation dans laquelle le roi est en position d'être capturé sans possibilité d'échappatoire.

Au cours de la partie, les joueurs se déplacent alternativement, déplaçant une pièce à chaque tour. Une pièce peut capturer une pièce adverse si elle se déplace sur la case occupée par cette dernière, la retirant ainsi du plateau.

Ce laboratoire vise à :
1. Familiariser les étudiants avec les concepts fondamentaux de la programmation orientée objet (POO) en utilisant l'exemple du jeu d'échecs.
2. Développer une compréhension des mécanismes tels que l'encapsulation, l'héritage, le polymorphisme, etc.
3. Créer une représentation logicielle du jeu d'échecs, en mettant l'accent sur la modélisation des pièces et leurs mouvements.

Pour ceux qui souhaitent approfondir les règles officielles du jeu d'échecs, vous pouvez consulter la page Wikipedia dédiée au sujet ou d'autres ressources spécialisées.

## 2. Énoncé de travail

L'objectif principal de ce laboratoire est d'implémenter un jeu d'échecs en utilisant Python et la programmation orientée objet (POO). Pour réaliser cette tâche, nous structurerons notre solution à l'aide de plusieurs classes, chacune représentant un élément spécifique du jeu d'échecs.

### Structure des classes
(L'image UML fournie illustre la relation entre ces classes)

### Description des classes

- **Pos**: Cette classe représente une position spécifique sur le plateau d'échecs, avec des attributs pour la ligne et la colonne.
- **TypePiece**: Elle énumère les différents types de pièces présents dans le jeu d'échecs (Roi, Dame, Tour, Fou, Cavalier, Pion).
- **Couleur**: Cette énumération distingue les deux couleurs des joueurs, à savoir Noir et Blanc.
- **Piece**: Représente une pièce individuelle du jeu. Chaque pièce a un type spécifique et une couleur.
- **CasePlateau**: Représente une case individuelle du plateau. Elle peut contenir une pièce ou être vide.
- **Plateau**: Représente le plateau de jeu complet, composé de 8x8 cases.
- **JeuEchec**: Cette classe englobe l'ensemble du jeu, y compris le plateau, les joueurs et la gestion des règles.

### Découpage du travail

1. **L'interface d'affichage**: Cette partie est déjà fournie. Elle permet d'afficher l'état actuel du jeu à l'utilisateur en utilisant une bibliothèque d'interface graphique adaptée à Python.
2. **La représentation de l'état d'une partie d'échecs**: Ce segment est couvert par les classes Pos, TypePiece, Couleur, Piece, CasePlateau, et Plateau. Ensemble, elles définissent et gèrent l'état actuel du plateau et des pièces.
3. **La gestion du jeu d'échecs et de ses règles**: La classe JeuEchec est responsable de cette partie. Elle interagit avec toutes les autres classes pour appliquer les règles du jeu, gérer les tours et déterminer les résultats.

## 3. Concepts

### 3.1 Interface

L'affichage du jeu d'échecs sera géré par une classe nommée `Interface` fournie avec cet énoncé de travail. Cette classe fonctionne de manière autonome et ne nécessite aucune connaissance des éléments à implémenter dans le reste du laboratoire. Pour comprendre son fonctionnement, veuillez consulter la documentation de la classe ainsi que le script de démonstration. Ces ressources vous aideront à vous familiariser avec la manière d'utiliser cette interface.

### 3.2 Règles à implémenter

Toutes les règles du jeu d'échecs ne sont pas faciles à mettre en œuvre. Dans ce laboratoire, nous nous concentrerons sur l'implémentation d'un sous-ensemble des règles complètes du jeu d'échecs. Plus précisément, vous allez travailler sur :
- Les mouvements possibles pour chaque type de pièce.
- L'alternance des tours entre les deux joueurs.
- La détection d'une situation d'échec à la fin d'un tour.
- La détection d'une situation d'échec et mat.

Il y a certaines règles que nous n'aborderons pas dans ce laboratoire en raison de leur complexité. Ces règles comprennent :
- La promotion (lorsqu'un pion atteint la dernière rangée adverse et est promu en une autre pièce).
- Le roque (mouvement spécial impliquant le roi et une tour).
- La prise en passant.
- Un mouvement rendant invalide la position due à une situation d'échec.
- Le pat (situation où aucun mouvement valide n'est possible, mais ce n'est pas un échec et mat).

### Classe Pos

La classe `Pos` représente une position sur le plateau d'échecs.

**Propriétés :**
- `ligne` (int) : Indique la ligne de la position sur le plateau.
- `colonne` (int) : Indique la colonne de la position sur le plateau.
- `emplacement` (str, dépendant) : Ce champ est calculé à partir des attributs `ligne` et `colonne`. Il s'agit d'une représentation sous forme de chaîne de caractères de la position sur le plateau (par exemple, "A1").

**Constructeur :**
  - `Pos(ligne_emplacement_ind: int, colonne: Optional[int] = None)`: 
  - `ligne_emplacement_ind` (int ou str) : Il peut s'agir soit de la ligne de la position, soit d'un indice unique de la case sur le plateau, soit du nom de l'emplacement.
  - `colonne` (int, facultatif) : Indique la colonne de la position. Ce paramètre est facultatif si le premier argument est une chaîne de caractères représentant l'emplacement.

### Méthodes

1. **estDansListePos(pos, listePos)**
   Cette méthode permet de vérifier si la position est présente dans la liste de positions.
   
   **Paramètres :**
   - `pos (Pos)` : La position à rechercher dans la liste.
   - `listePos (list[Pos])` : La liste de positions à parcourir.
   
   **Retour :**
   Renvoie True si la position est trouvée dans la liste, sinon False.

2. **estHorsPlateau(pos)**
   Cette méthode permet de déterminer si la position est hors du plateau 8x8. Peut recevoir une liste d'objets Pos et retourne une liste de réponses correspondantes.
   
   **Paramètres :**
   - `pos (list[Pos])` : Référence sur la liste de positions.
   
   **Retour :**
   Renvoie une liste indiquant si les positions sont hors du plateau (True pour hors du plateau, False sinon).

3. **get_emplacement(pos)**
   Cette méthode construit la chaîne de caractères représentant l'emplacement de la position. Cette fonction est automatiquement appelée lorsque l'on souhaite obtenir la propriété "emplacement" d'une position.
   
   **Paramètres :**
   - `pos (Pos)` : La position.
   
   **Retour :**
   Renvoie la chaîne de caractères représentant l'emplacement.

4. **ind(pos)**
   Cette méthode convertit la position en un indice afin de se localiser sur le plateau 8x8.
   
   **Paramètres :**
   - `pos (Pos)` : La référence à la position.
   
   **Retour :**
   Renvoie l'indice permettant de se localiser sur le plateau 8x8.

5. **plus(pos, addPos)**
   Cette méthode surcharge l'opérateur d'addition (+) pour les positions. Elle additionne les lignes et les colonnes individuellement.
   
   **Paramètres :**
   - `pos (Pos)` : La première position.
   - `addPos (Pos)` : La deuxième position.
   
   **Retour :**
   Renvoie la somme des deux positions.


### Classe TypePiece

L'énumération `TypePiece` définit les différents types de pièces dans le jeu d'échecs. Les membres de cette énumération sont les suivants :
- `ROI`: Le roi.
- `DAME`: La dame.
- `TOUR`: La tour.
- `FOU`: Le fou.
- `CAVALIER`: Le cavalier.
- `PION`: Le pion.

### Méthodes

1. **versChaine(typePiece)**
   Cette méthode retourne le type sous forme de chaîne de caractères.
   
   **Paramètres :**
   - `typePiece (TypePiece)` : Le type de pièce courant.
   
   **Retour :**
   Renvoie la chaîne de caractères représentant le type.

### Classe Couleur

L'énumération `Couleur` définit les deux couleurs des joueurs dans le jeu d'échecs. Les membres de cette énumération sont les suivants :
- `NOIR`: La couleur noire.
- `BLANC`: La couleur blanche.

### Méthodes

1. **not(couleur)**
   Surcharge de l'opérateur de négation (~) pour trouver l'autre couleur.
   
   **Paramètres :**
   - `couleur (Couleur)` : La couleur courante.
   
   **Retour :**
   Renvoie l'autre couleur disponible.

2. **versChaine(couleur)**
   Cette méthode retourne la couleur sous forme de chaîne de caractères.
   
   **Paramètres :**
   - `couleur (Couleur)` : La couleur courante.
   
   **Retour :**
   Renvoie la chaîne de caractères représentant la couleur.


### Classe Piece

La classe `Piece` représente une pièce individuelle du jeu d'échecs.

**Propriétés :**
- `type_piece` (TypePiece) : Le type de la pièce (par exemple, TypePiece.ROI).
- `couleur` (Couleur) : La couleur de la pièce (par exemple, Couleur.BLANC).

**Constructeur :**
- `Piece(type_piece: TypePiece, couleur: Couleur)` : Crée une nouvelle instance de `Piece` avec le type de pièce et la couleur spécifiés.

### Classe CasePlateau

La classe `CasePlateau` représente une case individuelle sur le plateau d'échecs.

**Propriétés :**
- `position` (Pos) : La position de la case sur le plateau.
- `piece` (Optional[Piece]) : La pièce actuellement présente sur la case. Peut être `None` si la case est vide.

**Constructeur :**
Lors de la création d'une instance de `CasePlateau`, le constructeur initialise la propriété `piece` avec la valeur spécifiée en paramètre, qui est une instance de la classe `Piece`.

### Méthodes

1. **estOccupe(casePlateau)**
   Cette méthode permet de déterminer si la case est occupée, c'est-à-dire si elle contient une pièce.
   
   **Paramètres :**
   - `casePlateau (1x1 CasePlateau)` : La case du plateau à vérifier.
   
   **Retour :**
   Renvoie vrai si la case est occupée par une pièce, sinon renvoie faux. Type renvoyé est `1x1 logical`.


### Classe Plateau

Cette classe représente un plateau de jeu d'échecs, qui est le principal composant du jeu. Elle contient les informations sur chaque case du plateau et les méthodes pour interagir avec celles-ci.

**Description :**
La classe `Plateau` modélise un plateau de jeu d'échecs. Elle contient un tableau 2D représentant chaque case du plateau et possède des constantes pour spécifier la taille standard du plateau.

**Propriétés :**
- `matCases (8x8 CasePlateau)` : Il s'agit d'un tableau 2D qui représente le plateau d'échecs. Chaque élément de ce tableau est une instance de `CasePlateau`.
- `NLIGNE = 8 (1x1 double, Constant)` : Cette constante spécifie le nombre de lignes sur le plateau d'échecs.
- `NCOLONNE = 8 (1x1 double, Constant)` : Cette constante spécifie le nombre de colonnes sur le plateau d'échecs.

**Constructeur :**
Lors de la création d'une instance de `Plateau`, le constructeur initialise `matCases` comme un tableau 8x8 composé d'instances de `CasePlateau`.

### Méthodes

1. **ajoutePiece(plateau, piece, pos)**
   Cette méthode permet d'ajouter une pièce à une position spécifique sur le plateau d'échecs. La méthode place la pièce spécifiée à la position donnée sur le plateau. Si une pièce occupe déjà cette position, elle est remplacée par la nouvelle pièce.
   
   **Paramètres :**
   - `plateau (1x1 Plateau)` : L'instance du plateau sur laquelle la pièce doit être ajoutée.
   - `piece (1x1 Piece)` : L'objet représentant la pièce à ajouter.
   - `pos (1x1 Pos)` : La position à laquelle la pièce doit être placée sur le plateau.

2. **bougePiece(plateau, posDepart, posFin)**
   Cette méthode permet de déplacer une pièce d'une position à une autre sur le plateau. Après le déplacement, la position de départ est laissée vide.
   
   **Paramètres :**
   - `plateau (1x1 Plateau)` : L'instance du plateau sur laquelle le déplacement est effectué.
   - `posDepart (1x1 Pos)` : La position initiale de la pièce avant le déplacement.
   - `posFin (1x1 Pos)` : La position finale après le déplacement.

3. **estCaseOccupe(plateau, pos)**
   Cette méthode permet de vérifier si une case particulière du plateau est occupée par une pièce.
   
   **Paramètres :**
   - `plateau (1x1 Plateau)` : L'instance du plateau à vérifier.
   - `pos (1x1 Pos)` : La position à vérifier.
   
   **Retour :**
   Renvoie vrai si la case est occupée, sinon renvoie faux. Type renvoyé est `1x1 logical`.

4. **initPartie(plateau)**
   Cette méthode initialise le plateau pour une nouvelle partie, plaçant chaque pièce à sa position initiale pour un jeu d'échecs standard.
   
   **Paramètres :**
   - `plateau (1x1 Plateau)` : L'instance du plateau à initialiser.

5. **listePiece(plateau)**
   Cette méthode crée une liste des pièces actuellement présentes sur le plateau. Cette liste peut être utilisée pour interagir avec l'interface utilisateur ou pour d'autres fonctionnalités.
   
   **Paramètres :**
   - `plateau (1x1 Plateau)` : L'instance du plateau pour lequel la liste doit être générée.
   
   **Retour :**
   Une liste représentant toutes les pièces sur le plateau. Type renvoyé est `1xn struct`.

6. **pieceAPosition(plateau, pos)**
   Cette méthode retourne la pièce située à une position spécifique sur le plateau.
   
   **Paramètres :**
   - `plateau (1x1 Plateau)` : L'instance du plateau à consulter.
   - `pos (1x1 Pos)` : La position à vérifier.
   
   **Retour :**
   Renvoie la pièce située à la position spécifiée. Type renvoyé est `1x1 Piece`.


### Classe JeuEchec

La classe `JeuEchec` englobe l'ensemble du jeu, y compris le plateau, les joueurs et la gestion des règles.

**Propriétés :**
- `plateau` (Plateau) : Le plateau de jeu.
- `joueur_blanc` (Type[Joueur]) : Le joueur jouant les pièces blanches.
- `joueur_noir` (Type[Joueur]) : Le joueur jouant les pièces noires.
- `tour_blanc` (bool) : Un booléen indiquant si c'est le tour du joueur blanc.

**Constructeur :**
- `JeuEchec()` : Crée une nouvelle instance de `JeuEchec` avec un plateau initialisé et deux joueurs initialisés.

### Méthodes

1. **estCaseJoueur(jeu, pos, joueur)**
   Détermine si une case contient une pièce qui appartient à un joueur.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `pos (1x1 Pos)` : La position à vérifier.
   - `joueur (1x1 Couleur)` : La couleur du joueur à vérifier.
   
   **Retour :**
   Renvoie `true` si la pièce existe à la position et est de la couleur du joueur. Type renvoyé est `1x1 logical`.

2. **estCaseJoueurInverse(jeu, pos, joueur)**
   Détermine si une case contient une pièce qui appartient au joueur adverse.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `pos (1x1 Pos)` : La position à vérifier.
   - `joueur (1x1 Couleur)` : La couleur du joueur à vérifier.
   
   **Retour :**
   Renvoie `true` si la pièce existe à la position et est de la couleur du joueur inverse. Type renvoyé est `1x1 logical`.

3. **estEchec(jeu, joueur)**
   Détermine si un joueur est en échec. Le joueur est en échec si un mouvement du joueur adverse peut capturer son roi.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `joueur (1x1 Couleur)` : La couleur du joueur à vérifier.
   
   **Retour :**
   Renvoie `true` si le joueur adverse a un mouvement valide sur la case du roi du joueur. Type renvoyé est `1x1 logical`.

4. **estEchecEtMat(jeu, joueur)**
   Détermine si un joueur est en échec et mat. Le joueur est en échec et mat si aucun mouvement ne peut le sortir d'être en échec.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `joueur (1x1 Couleur)` : La couleur du joueur à vérifier.
   
   **Retour :**
   Renvoie `true` si aucun mouvement du joueur ne le sort d'être en échec. Type renvoyé est `1x1 logical`.

5. **estMouvementValide(jeu, posDepart, posFin)**
   Détermine si un mouvement est valide. Un mouvement est valide si la pièce à la position de départ peut se déplacer à la position de fin dans sa liste de mouvements valides.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `posDepart (1x1 Pos)` : La position de départ du mouvement.
   - `posFin (1x1 Pos)` : La position finale après le déplacement.
   
   **Retour :**
   Renvoie `true` si le mouvement est valide. Type renvoyé est `1x1 logical`.

6. **jouerPartie(jeu)**
   Joue une partie d'échecs. Initialise l'interface, le plateau, le joueur courant et place les pièces initiales. Tant que le joueur courant n'est pas échec et mat, fait le tour du joueur courant et passe au joueur suivant.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.

7. **listeMouvementCavalier(jeu, pos)**
   Retourne la liste des mouvements possibles d'un cavalier à une position donnée. Assume que le cavalier est présent dans la case.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `pos (1x1 Pos)` : La position du cavalier.
   
   **Retour :**
   La liste des mouvements possibles du cavalier à la position donnée. Type renvoyé est `1xn Pos`.

8. **listeMouvementDame(jeu, pos)**
   Retourne la liste des mouvements possibles d'une dame à une position donnée. Assume que la dame est présente dans la case.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `pos (1x1 Pos)` : La position de la dame.
   
   **Retour :**
   La liste des mouvements possibles de la dame à la position donnée. Type renvoyé est `1xn Pos`.

9. **listeMouvementFou(jeu, pos)**
   Retourne la liste des mouvements possibles d'un fou à une position donnée. Assume que le fou est présent dans la case.
   
   **Paramètres :**
   - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
   - `pos (1x1 Pos)` : La position du fou.
   
   **Retour :**
   La liste des mouvements possibles du fou à la position donnée. Type renvoyé est `1xn Pos`.

10. **listeMouvementPion(jeu, pos)**
    Retourne la liste des mouvements possibles d'un pion à une position donnée. Assume que le pion est présent dans la case.
    
    **Paramètres :**
    - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
    - `pos (1x1 Pos)` : La position du pion.
    
    **Retour :**
    La liste des mouvements possibles du pion à la position donnée. Type renvoyé est `1xn Pos`.

11. **listeMouvementRoi(jeu, pos)**
    Retourne la liste des mouvements possibles d'un roi à une position donnée. Assume que le roi est présent dans la case.
    
    **Paramètres :**
    - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
    - `pos (1x1 Pos)` : La position du roi.
    
    **Retour :**
    La liste des mouvements possibles du roi à la position donnée. Type renvoyé est `1xn Pos`.

12. **listeMouvementTour(jeu, pos)**
    Retourne la liste des mouvements possibles d'une tour à une position donnée. Assume que la tour est présente dans la case.
    
    **Paramètres :**
    - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
    - `pos (1x1 Pos)` : La position de la tour.
    
    **Retour :**
    La liste des mouvements possibles de la tour à la position donnée. Type renvoyé est `1xn Pos`.

13. **listeMouvementValideJoueur(jeu, joueur)**
    Retourne la liste des mouvements possibles de toutes les pièces d'un joueur.
    
    **Paramètres :**
    - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
    - `joueur (1x1 Couleur)` : La couleur du joueur à vérifier.
    
    **Retour :**
    La liste des mouvements possibles de toutes les pièces du joueur. Type renvoyé est `1xn Pos`.

14. **listeMouvementValidePos(jeu, pos)**
    Retourne la liste des mouvements possibles d'une pièce à une position donnée.
    
    **Paramètres :**
    - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
    - `pos (1x1 Pos)` : La position de la pièce.
    
    **Retour :**
    La liste des mouvements possibles de la pièce à la position donnée. Type renvoyé est `1xn Pos`.

15. **posRoiJoueur(jeu, joueur)**
    Retourne la position du roi appartenant au joueur.
    
    **Paramètres :**
    - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.
    - `joueur (1x1 Couleur)` : La couleur du joueur à vérifier.
    
    **Retour :**
    La position du roi du joueur. Type renvoyé est `1x1 Pos`.

16. **tourJoueurCourant(jeu)**
    Effectue le tour du joueur courant. Le tour consiste à :
    - Sélectionner un emplacement de départ.
    - Afficher des curseurs sur les cases où la pièce peut faire un mouvement valide.
    - Sélectionner un emplacement parmi les mouvements possibles.
    - Bouger la pièce sur le plateau et mettre à jour l'interface.
    La fonction doit être robuste par rapport aux actions de l'utilisateur. Si le joueur fait une mauvaise sélection à n'importe quel moment (choisit une case qui n'est pas de sa couleur, sélectionne un deuxième emplacement qui n'est pas un mouvement valide, etc.), recommencer la saisie.
    
    **Paramètres :**
    - `jeu (1x1 JeuEchec)` : Référence au jeu d'échecs.