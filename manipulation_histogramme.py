# Section 11 :
    #Création et comparaison d'histogrammes


# Cette fonction génère un histogramme pour chaque pixel de l'image en utilisant un carré de voisinage de taille spécifiée.

# Arguments :
    # tableau_2D (numpy.ndarray): Un tableau 2D NumPy représentant une image.
    # w (int): La taille du carré de voisinage autour de chaque pixel pour lequel l'histogramme est calculé.
# Retourne :
    #numpy.ndarray: Un tableau 2D NumPy où chaque ligne représente un histogramme pour le carré correspondant de l'image.

def calculer_histogramme(tableau, w):

    # Déterminer la taille de l'image
    hauteur, largeur = len(tableau), len(tableau[0])

    # Calculer la valeur maximale dans le tableau 2D
    valeur_max = np.max(tableau)
    
    # Initialiser l'histogramme
    histogramme = []

    # Nombre de carrés dans l'image
    nb_carres_hauteur = hauteur - w + 1
    nb_carres_largeur = largeur - w + 1

    # Parcourir chaque fenêtre dans l'image
    for x in range(nb_carres_hauteur):
        for y in range(nb_carres_largeur):
           
            # Extraire le carré de voisinage
            fenetre = tableau[x:x + w, y:y + w]

            # Calculer l'histogramme
            hist, _ = np.histogram(fenetre, bins=[0, valeur_max / 4, valeur_max / 2, (3 * valeur_max) / 4, valeur_max], range=(0, valeur_max))

            histogramme.append(hist)

    return np.array(histogramme)

# Cette fonction calcule la distance entre deux histogrammes.

# Arguments:
    # histogramme1 (numpy.ndarray): Premier histogramme sous forme de tableau 1D NumPy.
    # histogramme2 (numpy.ndarray): Deuxième histogramme sous forme de tableau 1D NumPy
# Retourne float:
    # La distance entre les deux histogrammes.

def calculer_distance_1(h1, h2):

    # Vérifier que les histogrammes ont la même taille
    if len(h1) != len(h2):
        print(ValueError("Les histogrammes doivent avoir la même taille."))

    # Calculer la distance entre les deux histogrammes
    distance_carree = np.sum((h1 - h2) ** 2)
    distance = np.sqrt(distance_carree)

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie_1 = round(distance, 2)

    return distance_arrondie_1

# Cette fonction calcule la distance entre deux histogrammes.

# Arguments :
    # histogramme1 (numpy.ndarray): Premier histogramme sous forme de tableau 1D NumPy.
    # histogramme2 (numpy.ndarray): Deuxième histogramme sous forme de tableau 1D NumPy
#Retourne float:
    # La distance entre les deux histogrammes.

def calculer_distance_2(h1, h2):
    # Vérifier que les histogrammes ont la même taille
    if len(h1) != len(h2):
        print(ValueError("Les histogrammes doivent avoir la même taille."))

    # Calculer la distance entre les deux histogrammes
    distance = np.sum(np.abs(h1 - h2))

    # Arrondir le résultat à deux chiffres après la virgule
    distance_arrondie_2 = round(distance, 2)

    return distance_arrondie_2
