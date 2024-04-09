#### Test à faire


#Section 11 :
    #Création et comparaison d'histogrammes


# Cette fonction génère un histogramme pour chaque pixel de l'image en utilisant un carré de voisinage de taille spécifiée.

# Arguments :
    # tableau_2D (numpy.ndarray): Un tableau 2D NumPy représentant une image.
    # w (int): La taille du carré de voisinage autour de chaque pixel pour lequel l'histogramme est calculé.
#Retourne :
    #numpy.ndarray: Un tableau 2D NumPy où chaque ligne représente un histogramme pour le carré correspondant de l'image.

def calculer_histogramme(image_trasf_2, w):

    # Déterminer la taille de l'image
    hauteur, largeur = image_trasf_2.shape

    # Calculer la valeur maximale dans le tableau 2D
    max_value = np.max(image_trasf_2)

    # Créer un tableau pour stocker les histogrammes
    tab_histo = np.zeros((hauteur - w + 1, largeur - w + 1, 5), dtype=np.int)
    # Le dernier axe (5) représente les bins: [0, max/4, max/2, 3*max/4, max]

    # Parcourir chaque fenêtre dans l'image
    for y in range(hauteur - w + 1):
        for x in range(largeur - w + 1):
            # Extraire la fenêtre
            fenetre = image_trasf_2[y:y + w, x:x + w]

            # Calculer l'histogramme de la fenêtre
            hist, _ = np.histogram(fenetre, bins=[0, max_value / 4, max_value / 2, (3 * max_value) / 4, max_value],
                                   range=(0, max_value))

            # Assigner l'histogramme au tableau des histogrammes
            tab_histo[y, x, :] = hist

    return tab_histo






#### Test à faire

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





#### Test à faire

# Calculer la distance entre deux histogrammes.
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