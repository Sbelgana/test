<div align="justify">

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Polytechnique_Montr%C3%A9al_logo.jpg" />
</p>

# TP04 : Programmation orientée objet
- [Directives particulières](#directives)
- [Introduction](#introduction)
- [Objectifs du laboratoire](#objectif)
- [Description du problème](#description)
- [Concepts](#concepts)
- [Classes à implémenter](#classes)
    - [Classe Pos](#pos)
    - [Classe TypePiece](#typepiece)
    - [Classe Couleur](#couleur)
    - [Classe Piece](#piece)
    - [Classe CasePlateau](#caseplateau)
    - [Classe Plateau](#plateau)
    - [Classe JeuEchec](#jeu)
- [Barème](#bareme)
- [Annexe: Guide et normes de codage](#annexe)

:alarm_clock: [[Date de remise le dimanche 6 novembre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20231106T235959&p0=165&font=cursive)

## Directives particulières <a name="directives"></a>
* Respecter [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Noms de variables et fonctions adéquats (concis, compréhensibles);  
* Pas de librairies externes autres que celles déjà importées;

## 1. Introduction <a name="introduction"></a>
Bienvenue dans cette aventure de programmation orientée objet (POO), où nous allons explorer ensemble le monde captivant du jeu d'échecs, en utilisant Python comme outil de création. Ce laboratoire est une occasion unique de s'immerger dans les principes de la POO tout en s'amusant à modéliser l'un des jeux de stratégie les plus anciens et les plus appréciés au monde.

Le jeu d'échecs, connu pour sa profondeur stratégique et ses règles élaborées, se prête parfaitement à l'exercice de structuration et d'organisation du code selon les principes de la POO, tels que les classes, l'héritage, le polymorphisme et l'encapsulation. En décomposant le jeu en différentes composantes – pièces, plateau, mouvements – vous allez non seulement apprendre à coder de manière plus intuitive et structurée, mais aussi à penser de manière abstraite, une compétence clé en programmation.

L'objectif ici n'est pas seulement de construire une application Python qui simule une partie d'échecs, mais aussi de vous familiariser avec une approche de codage qui favorise la clarté, la modularité et la réutilisabilité. C'est une invitation à voir au-delà du code et à comprendre comment des éléments séparés s'assemblent pour créer un système complet et fonctionnel.

Préparez-vous donc à une expérience riche en apprentissages et en défis. Ce laboratoire est plus qu'un simple exercice technique; c'est une exploration de la logique, de la stratégie, et de l'histoire, le tout encadré par la puissance et la souplesse de programmation; c'est un voyage à travers l'histoire, la stratégie et la logique, facilité par les puissants outils de la programmation orientée objet.

## 2. Objectifs <a name="objectif"></a>

Le jeu d'échecs est un jeu stratégique ancestral qui oppose deux joueurs sur un plateau. Chaque joueur dispose d'un ensemble de pièces ayant des mouvements et des fonctions spécifiques. Le principal objectif est de mettre le roi adverse en échec et mat, situation dans laquelle le roi est en position d'être capturé sans possibilité d'échappatoire.

Au cours de la partie, les joueurs se déplacent alternativement, déplaçant une pièce à chaque tour. Une pièce peut capturer une pièce adverse si elle se déplace sur la case occupée par cette dernière, la retirant ainsi du plateau.

Ce laboratoire vise à :
1. Familiariser les étudiants avec les concepts fondamentaux de la programmation orientée objet (POO) en utilisant l'exemple du jeu d'échecs.
2. Développer une compréhension des mécanismes tels que l'encapsulation, l'héritage, le polymorphisme, etc.
3. Créer une représentation logicielle du jeu d'échecs, en mettant l'accent sur la modélisation des pièces et leurs mouvements.

Pour ceux qui souhaitent approfondir les règles officielles du jeu d'échecs, vous pouvez consulter la page [Wikipedia](https://fr.wikipedia.org/wiki/%C3%89checs#R%C3%A8gles_du_jeu) dédiée au sujet ou d'autres ressources spécialisées.

## 3. Description du problème <a name="description"></a>

L'objectif principal de ce laboratoire est d'implémenter un jeu d'échecs en utilisant Python et la programmation orientée objet (POO). Pour réaliser cette tâche, nous structurerons notre solution à l'aide de plusieurs classes, chacune représentant un élément spécifique du jeu d'échecs.

### Structure des classes
<p align="center">
    <img src="UML.svg">
</p>

### Description des classes

- **Pos**: Cette classe représente une position spécifique sur le plateau d'échecs, avec des attributs pour la ligne et la colonne.
- **TypePiece**: Elle énumère les différents types de pièces présents dans le jeu d'échecs (Roi, Dame, Tour, Fou, Cavalier, Pion).
- **Couleur**: Cette énumération distingue les deux couleurs des joueurs, à savoir Noir et Blanc.
- **Piece**: Représente une pièce individuelle du jeu. Chaque pièce a un type spécifique et une couleur.
- **CasePlateau**: Représente une case individuelle du plateau. Elle peut contenir une pièce ou être vide.
- **Plateau**: Représente le plateau de jeu complet, composé de 8x8 cases.
- **JeuEchec**: Cette classe englobe l'ensemble du jeu, y compris le plateau, les joueurs et la gestion des règles.
- **Interface**: Cette classe contient les fonctions pour l'interface graphique (GUI).

### Découpage du travail

1. **L'interface d'affichage**: Cette partie est déjà fournie. Elle permet d'afficher l'état actuel du jeu à l'utilisateur en utilisant une bibliothèque d'interface graphique adaptée à Python.
2. **La représentation de l'état d'une partie d'échecs**: Ce segment est couvert par les classes Pos, TypePiece, Couleur, Piece, CasePlateau, et Plateau. Ensemble, elles définissent et gèrent l'état actuel du plateau et des pièces.
3. **La gestion du jeu d'échecs et de ses règles**: La classe JeuEchec est responsable de cette partie. Elle interagit avec toutes les autres classes pour appliquer les règles du jeu, gérer les tours et déterminer les résultats.

## 4. Concepts <a name="concepts"></a>

### 4.1 Interface

L'affichage du jeu d'échecs sera géré par une classe nommée `Interface` fournie avec cet énoncé de travail. Cette classe fonctionne de manière autonome et ne nécessite aucune connaissance des éléments à implémenter dans le reste du laboratoire. Pour comprendre son fonctionnement, veuillez consulter la documentation de la classe ainsi que le script de démonstration. Ces ressources vous aideront à vous familiariser avec la manière d'utiliser cette interface.

### 4.2 Règles à implémenter

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

## 5. Classes à implémenter <a name="classes"></a>

### 5.1. Classe Pos <a name="pos"></a>

La classe `Pos`, essentielle dans notre modèle d'échecs en Python, sert à représenter les positions sur le plateau de jeu. Elle démontre comment la programmation orientée objet peut efficacement modéliser des concepts complexes de manière intuitive.


**Attributs de la Classe :**
- `ligne` (int) : Représente la ligne de la position sur le plateau, avec 1 correspondant à la première ligne.
- `colonne` (int) : Indique la colonne de la position, numérotée de 1 à 8, correspondant respectivement aux colonnes 'a' à 'h' dans le jeu d'échecs.
- `emplacement` (str) : Propriété calculée qui combine les attributs `ligne` et `colonne` pour former une représentation alphanumérique de la position (par exemple, "b3").

**Constructeur :**
Initialise une instance de `Pos`. Si `ligne_emplacement_ind` est une chaîne, elle extrait la ligne et la colonne à partir des indices dans la chaîne. Si `ligne_emplacement_ind` est un entier et `colonne` est fourni, ils sont directement utilisés comme ligne et colonne. Si `ligne_emplacement_ind` est un entier sans `colonne`, elle calcule la ligne et la colonne à partir de l'indice linéaire.

- `ligne_emplacement_ind` peut être un entier ou une chaîne. Si c'est un entier, il représente soit l'indice unique d'une case sur le plateau (numérotation de 1 à 64), soit la ligne si la colonne est également spécifiée. Si c'est une chaîne, elle représente l'emplacement alphanumérique (par exemple, "c4").
- `colonne` est facultatif si `ligne_emplacement_ind` est une chaîne. Si fourni, il spécifie la colonne de la position.


### Méthodes

1. **estDansListePos(pos, listePos)**

  Méthode Statique qui vérifie si une position donnée (`pos`) se trouve dans une liste spécifiée de positions (`listePos`). Renvoie `True` si `pos` est trouvée dans `listePos`, sinon `False`.

   **Paramètres :**
   - `pos (Pos)` : La position à rechercher dans la liste.
   - `listePos (list[Pos])` : La liste de positions à parcourir.
   
   **Retour :**
   Renvoie True si la position est trouvée dans la liste, sinon False.

2. **estHorsPlateau(pos)**

  Méthode Statique  qui vérifie si une ou plusieurs positions sont hors des limites d'un plateau de jeu standard (8x8). Retourne une liste de booléens indiquant si chaque position spécifiée est hors des limites.
 
   **Paramètres :**
   - `pos (list[Pos])` : Référence sur la liste de positions.
   
   **Retour :**
   Renvoie une liste indiquant si les positions sont hors du plateau (True pour hors du plateau, False sinon).

3. **get_emplacement(self)**

  Calcule et retourne l'emplacement alphanumérique de la position basée sur les attributs `ligne` et `colonne`.   
   
   **Retour :**
   Renvoie la chaîne de caractères représentant l'emplacement.

4. **ind(self)**
 
  Convertit une position en un indice linéaire, permettant une gestion facile des positions sur un plateau représenté par un tableau unidimensionnel ou des listes.
 
   **Retour :**
   Renvoie l'indice permettant de se localiser sur le plateau 8x8.

5. **__add__(self, pos)**

Cette méthode surcharge l'opérateur d'addition (+) pour les positions. Elle permet d'additionner deux instances de `Pos`. Cela revient à additionner séparément les valeurs des lignes et des colonnes des deux instances, créant ainsi une nouvelle position résultante.
   
   **Paramètres :**
   - `pos (Pos)` : La position.
   
   **Retour :**
   Renvoie la somme des deux positions.


6. **__eq__(self, pos)**

  Cette méthode surcharge l'opérateur de comparaison (=) pour les positions Compare l'instance actuelle de `Pos` avec une autre instance pour vérifier si elles représentent la même position. 
  
   **Paramètres :**
   - `pos (Pos)` : La position.
   
   **Retour :**
   Renvoie `True` si les lignes et les colonnes des deux instances sont identiques.



7. **__str__(self, )**

  Cette méthode surcharge l'opérateur de d'affichage pour les positions. Fournit une représentation textuelle de l'instance `Pos`, incluant les informations sur la ligne, la colonne et l'emplacement alphanumérique. 

     
   **Retour :**
   Renvoie la chaîne de caractères représentant l'instance `Pos`.


---

### 5.2. Classe TypePiece <a name="typePiece"></a>

La classe `TypePiece`, implémentée en tant qu'énumération (`Enum`), joue un rôle clé dans notre modèle d'échecs en Python en définissant les différents types de pièces utilisées dans le jeu. Cette structure permet une représentation claire et standardisée des pièces d'échecs, facilitant ainsi leur gestion et leur identification dans le code.

Chaque type de pièce d'échecs est représenté par une valeur unique de l'énumération. Les types disponibles sont :
  - `ROI` (valeur 1) : Représente le roi.
  - `DAME` (valeur 2) : Représente la dame.
  - `TOUR` (valeur 3) : Représente la tour.
  - `FOU` (valeur 4) : Représente le fou.
  - `CAVALIER` (valeur 5) : Représente le cavalier.
  - `PION` (valeur 6) : Représente le pion.

**Méthode :**

1. **vers_chaine(self)**
Convertit l'identifiant numérique d'un type de pièce en une chaîne de caractères représentant son nom. Cette méthode facilite la compréhension du code et l'interaction avec l'utilisateur en transformant les valeurs énumérées en termes plus descriptifs et reconnaissables.

   **Retour :** 
   Chaîne de caractères correspondant au nom du type de pièce (par exemple, 'Roi', 'Dame', etc.).

---


### 5.3. Classe Couleur <a name="couleur"></a>

La classe `Couleur`, implémentée comme une énumération (`Enum`), est un composant essentiel de notre modèle d'échecs en Python. Elle est utilisée pour représenter de façon distincte les deux couleurs des joueurs dans le jeu d'échecs, à savoir Blanc et Noir. L'approche d'énumération assure une utilisation cohérente et standardisée des couleurs dans tout le code.

Les membres de cette énumération sont les suivants :
- `NOIR`: La couleur noire.
- `BLANC`: La couleur blanche.

### Méthodes de Classe

1. **not(cls, couleur)**
   Surcharge de l'opérateur de négation (~). Renvoie la couleur opposée à celle fournie. Cette méthode est particulièrement utile pour alterner les tours entre les joueurs Blanc et Noir.
  
   
   **Paramètres :**
   - `couleur (Couleur)` : La couleur courante.
   
   **Retour :**
   La couleur opposée (par exemple, si `BLANC` est fourni, la méthode renvoie `NOIR`).

2. **versChaine(cls, couleur)**
   Convertit la couleur énumérée en une chaîne de caractères, facilitant l'affichage et la compréhension par l'utilisateur.
     
   **Paramètres :**
   - `couleur (Couleur)` : La couleur courante.
   
   **Retour :**
   Représentation en chaîne de la couleur (par exemple, 'Blanc' pour `BLANC`).


### 5.4. Classe Piece <a name="piece"></a>

La classe `Piece` est une composante fondamentale de notre modèle de jeu d'échecs en Python. Elle est conçue pour représenter une pièce d'échecs individuelle, en combinant son type (par exemple, Roi, Dame, etc.) et sa couleur (Blanc ou Noir). Cette classe incarne l'approche de la programmation orientée objet en associant des attributs et des comportements spécifiques à chaque pièce du jeu.

**Attributs de la Classe :**
- `type` (TypePiece) : Décrit le type de la pièce, en utilisant les valeurs de l'énumération `TypePiece`. Cela permet d'identifier facilement si la pièce est un Roi, une Dame, etc.
- `couleur` (Couleur) : Indique la couleur de la pièce, soit Blanc soit Noir, en utilisant l'énumération `Couleur`. Cet attribut est crucial pour déterminer à quel joueur appartient la pièce.

**Constructeur :**
Initialise une nouvelle instance de la classe `Piece`.
- `type_piece` (TypePiece) : Le type de la pièce (par exemple, TypePiece.ROI).
- `couleur` (Couleur) : La couleur de la pièce (par exemple, Couleur.BLANC).
    
### 5.5. Classe CasePlateau <a name="caseplateau"></a>

La classe `CasePlateau` joue un rôle crucial dans notre modèle d'échecs en Python. Elle représente une case individuelle sur le plateau de jeu. Chaque case peut contenir une pièce d'échecs ou être vide, ce qui est un aspect fondamental de la mécanique du jeu d'échecs.

**Attributs de la Classe :**
- `piece` (Piece, optionnel) : Cet attribut stocke une référence à une instance de la classe `Piece` si la case est occupée. Si la case est vide, `piece` est `None`.


**Constructeur :**
Initialise une nouvelle instance de la classe `CasePlateau`.
- `piece` (Piece, optionnel) : La pièce à placer dans la case. Si aucune pièce n'est fournie, la case est considérée comme vide.

### Méthodes

1. **estOccupe(self)**
Détermine si la case est occupée par une pièce. Cette méthode est essentielle pour de nombreuses règles du jeu d'échecs, telles que le déplacement des pièces et la capture.
   
   **Retour :**
   Renvoie True si la case est occupée par une pièce False sinon. 


### 5.6. Classe Plateau <a name="plateau"></a>

La classe `Plateau` est une composante clé de notre modèle d'échecs en Python. Elle représente le plateau de jeu d'échecs, qui est essentiellement un ensemble de cases (instances de `CasePlateau`). La classe gère l'ensemble du plateau, y compris le placement et le mouvement des pièces.

**Attributs de la Classe :**
- `matCases` (2D list of `CasePlateau`) : Une matrice 2D qui représente le plateau d'échecs, composée de 8 lignes et 8 colonnes.
- `NLIGNE = 8 (1x1 double, Constant)` : Cette constante spécifie le nombre de lignes sur le plateau d'échecs.
- `NCOLONNE = 8 (1x1 double, Constant)` : Cette constante spécifie le nombre de colonnes sur le plateau d'échecs.

**Constructeur :**
Initialise un nouveau plateau de jeu en créant une grille 8x8 de cases vides.

### Méthodes

1. **ajoute_piece(self, piece, pos)**

Ajoute une pièce à une position spécifique sur le plateau. La méthode place la pièce spécifiée à la position donnée sur le plateau. Si une pièce occupe déjà cette position, elle est remplacée par la nouvelle pièce.
   - **Paramètres :** 
     - `piece` (Piece) : La pièce à ajouter.
     - `pos` (Pos) : La position où placer la pièce.


2. **bouge_piece(self, pos_depart, pos_fin)**

Déplace une pièce d'une position de départ à une position de fin sur le plateau. Après le déplacement, la position de départ est laissée vide.
   - **Paramètres :** 
     - `pos_depart` (Pos) : La position initiale de la pièce.
     - `pos_fin` (Pos) : La position finale de la pièce.

3. **est_case_occupe(self, pos)**

Vérifie si une case spécifique est occupée par une pièce.
   - **Paramètres :** 
     - `pos` (Pos) : La position de la case à vérifier.
      
   **Retour :**
   Renvoie vrai si la case est occupée, sinon renvoie faux. 

4. **init_partie(self)**

   Initialise le plateau pour une nouvelle partie, plaçant les pièces dans leurs positions de départ standard.


5. **liste_piece(self)**

Crée et retourne une liste des pièces actuellement présentes sur le plateau, incluant des informations sur leur type, couleur et emplacement.
      
   **Retour :**
   Une liste représentant toutes les pièces sur le plateau. 

6. **piece_a_position(self, pos)**

Retourne la pièce située à une position spécifiée sur le plateau.
  **Paramètres :** 
     - `pos` (Pos) : La position à vérifier sur le plateau.
   
   **Retour :**
   Renvoie la pièce située à la position spécifiée.


### 5.7. Classe JeuEchec <a name="jeu"></a>

La classe `JeuEchec` est le cœur de notre application de jeu d'échecs en Python. Elle coordonne les éléments du jeu, y compris le plateau, les pièces, et les règles du jeu d'échecs. Cette classe gère également le déroulement de la partie, y compris le changement de tour entre les joueurs.

**Attributs de la Classe :**
- `plateau` (Plateau) : Représente le plateau de jeu.
- `joueurCourant` (Couleur) : Indique le joueur qui doit jouer, initialisé à Blanc.

**Constructeur :**
Initialise le jeu d'échecs en créant un nouveau plateau et en définissant le joueur courant.

### Méthodes

1. **est_case_joueur(self, pos, joueur)**

Vérifie si une case est occupée par une pièce appartenant au joueur spécifié.

  **Paramètres :** 
     - `pos` (Pos) : Position de la case à vérifier.
     - `joueur` (Couleur) : Joueur (Couleur) à vérifier.
   
   **Retour :**
   Renvoie `True` si la pièce existe à la position et est de la couleur du joueur. 

2. **est_case_joueur_inverse(self, pos, joueur)**
Vérifie si une case est occupée par une pièce appartenant à l'adversaire du joueur spécifié.
   
   **Paramètres :**
     - `pos` (Pos) : Position de la case à vérifier.
     - `joueur` (Couleur) : Joueur (Couleur) à vérifier.
   
   **Retour :**
   Renvoie `true` si la pièce existe à la position et est de la couleur du joueur inverse. 


3. **liste_mouvement_cavalier(self, pos)**

Calcule et retourne une liste des mouvements valides pour un cavalier à une position donnée.
   
   **Paramètres :**
   - `pos` (Pos) : La position du cavalier.
   
   **Retour :**
   La liste des mouvements possibles du cavalier à la position donnée.


4. **liste_mouvement_fou(self, pos)**

Calcule et retourne une liste des mouvements valides pour un fou à une position donnée.
   
   **Paramètres :**
   - `pos` (Pos) : : La position du fou.
   
   **Retour :**
   La liste des mouvements possibles du fou à la position donnée.


5. **liste_mouvement_tour(self, pos)**

Calcule et retourne une liste des mouvements valides pour une tour à une position donnée.
   
   **Paramètres :**
    - `pos` (Pos) : La position de la tour.
   
   **Retour :**
    La liste des mouvements possibles de la tour à la position donnée.

    
6. **listeMouvementDame(jeu, pos)**
   Calcule et retourne une liste des mouvements valides pour une dame à une position donnée.
   
   **Paramètres :**
   - `pos` (Pos) : : La position de la dame.
   
   **Retour :**
   La liste des mouvements possibles de la dame à la position donnée. 


7. **listeMouvementRoi(jeu, pos)**
    Calcule et retourne une liste des mouvements valides pour un roi à une position donnée.
    
    **Paramètres :**
    - `pos` (Pos) : La position du roi.
    
    **Retour :**
    La liste des mouvements possibles du roi à la position donnée.
    

8. **listeMouvementPion(jeu, pos)**
    Calcule et retourne une liste des mouvements valides pour un pion à une position donnée.
    
    **Paramètres :**
    - `pos` (Pos) : La position du pion.
    
    **Retour :**
    La liste des mouvements possibles du pion à la position donnée. 

9. **estMouvementValide(jeu, posDepart, posFin)**
   Détermine si le déplacement d'une pièce d'une position de départ à une position de fin est valide.

   **Paramètres :**
   - `posDepart (Pos)` : La position de départ du mouvement.
   - `posFin (Pos)` : La position finale après le déplacement.
   
   **Retour :**
   Renvoie `true` si le mouvement est valide.
   

10. **listeMouvementValideJoueur(jeu, joueur)**
    Calcule et retourne tous les mouvements valides pour toutes les pièces d'un joueur.
    
    **Paramètres :**
    - `joueur (Couleur)` : La couleur du joueur à vérifier.
    
    **Retour :**
    La liste des mouvements possibles de toutes les pièces du joueur. 

11. **listeMouvementValidePos(jeu, pos)**
    Calcule et retourne tous les mouvements valides pour une pièce à une position donnée.
    
    **Paramètres :**
    - `pos (Pos)` : La position de la pièce.
    
    **Retour :**
    La liste des mouvements possibles de la pièce à la position donnée.
    
12. **posRoiJoueur(jeu, joueur)**
    Retourne la position du roi pour le joueur spécifié.
    
    **Paramètres :**
    - `joueur (Couleur)` : La couleur du joueur à vérifier.
    
    **Retour :**
    La position du roi du joueur. 

13. **estEchec(self, joueur)**
   Détermine si le joueur spécifié est en situation d'échec.
   
   **Paramètres :**
   - `joueur (Couleur)` : La couleur du joueur à vérifier.
   
   **Retour :**
   Renvoie `true` si le joueur adverse a un mouvement valide sur la case du roi du joueur. 

14. **estEchecEtMat(self, joueur)**
   Détermine si le joueur spécifié est en situation d'échec et mat.
   
   **Paramètres :**
   - `joueur (Couleur)` : La couleur du joueur à vérifier.
   
   **Retour :**
   Renvoie `true` si aucun mouvement du joueur ne le sort d'être en échec.
   





15. **tourJoueurCourant(jeu)**
Gère un tour complet du joueur courant.

Le tour consiste à :
    - Sélectionner un emplacement de départ.
    - Afficher des curseurs sur les cases où la pièce peut faire un mouvement valide.
    - Sélectionner un emplacement parmi les mouvements possibles.
    - Bouger la pièce sur le plateau et mettre à jour l'interface.
    La fonction doit être robuste par rapport aux actions de l'utilisateur. Si le joueur fait une mauvaise sélection à n'importe quel moment (choisit une case qui n'est pas de sa couleur, sélectionne un deuxième emplacement qui n'est pas un mouvement valide, etc.), recommencer la saisie.


16. **isEmplacementDepartValide(self)**
   Vérifie si l'emplacement de départ d'un mouvement est valide.

17. **reset(self)**
   Réinitialise le plateau pour une nouvelle partie.

18. **jouerPartie(self)**
   Gère le déroulement d'une partie d'échecs, y compris les tours des joueurs et la vérification des conditions de fin de partie.


## 8. Barème /100 <a name="bareme"></a>

|**Nom des fonctions**|**Nombre de points attribuer**|
| :- | :- |  


## Annexe: Guide et normes de codage <a name="annexe"></a>
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. 
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)

