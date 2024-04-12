#Section 10 :
    #Extraction de caractéristiques à partir de données visuelles


#Cette fonction transforme une image en couleur en une nouvelle image en niveaux de gris.

#Arguments :
    #path_image_orig (str): Le chemin de l'image en couleur à transformer.
    #path_image_ng (str): Le chemin où sauvegarder l'image résultante en niveaux de gris.
#Retourne :
    #rien
###commentaire :
    #on doit définir le chemin pour se rendre à l'image de couleur dans 'chemin_image_couleur' et le chemin de l'image grise dans 'chemin_image_gris'

def appliquer_rgb_to_gry(path_image_orig, path_image_ng):

    #Charger l'image en couleur
    image_couleur = Image.open(path_image_orig)

    #Convertir l'image en niveaux de gris
    image_array = convertir_rgb_to_gry(image_couleur)

    # Sauvegarder l'image en niveaux de gris
    image_array.save(path_image_ng)

def convertir_rgb_to_gry(image_couleur):

    largeur, hauteur = image_couleur.size
    image_array = Image.new('L', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            # Obtenir les composantes RGB du pixel
            r, g, b = image_couleur.getpixel((x, y))

            # Calculer la moyenne des composantes RGB
            moyenne = (r + g + b) // 3

            # Définir la nouvelle valeur de pixel en niveaux de gris
            image_array.putpixel((x, y), moyenne)

    return image_array




####Test à faire

#Cette fonction prend une image en niveaux de gris sous forme d'un tableau NumPy 2D et applique une transformation pour simplifier et
#extraire des caractéristiques significatives de l'image.

#Arguments :
    #image_gris (numpy.ndarray): Un tableau 2D NumPy représentant une image en niveaux de gris. Chaque élément du tableau correspond à
    #l'intensité d'un pixel de l'image.
#Retourne :
    #numpy.ndarray: Un tableau 2D NumPy résultant de la transformation appliquée.

def appliquer_transformation_1(image_array):

    #Créer un tableau pour stocker les résultats de la transformation
    resultat_transformation = np.zeros_like(image_array, dtype=np.uint8)

    #Dimensions de l'image
    hauteur, largeur = image_array.shape

    #Parcourir chaque pixel de l'image
    for y in range(1, hauteur - 1):  # Ignorer les bords pour éviter les problèmes
        for x in range(1, largeur - 1):
            #Obtenir les valeurs de gris des voisins
            voisins = [
                image_array[y - 1, x - 1], image_array[y - 1, x], image_array[y - 1, x + 1],
                image_array[y, x - 1], image_array[y, x + 1],
                image_array[y + 1, x - 1], image_array[y + 1, x], image_array[y + 1, x + 1]
            ]
            #Pixel central
            pixel_central = image_array[y, x]

            #Comparaison avec les voisins pour former le motif binaire
            motif_binaire = ''.join(['1' if voisin >= pixel_central else '0' for voisin in voisins])

            #Convertir le motif binaire en valeur décimale
            valeur_decimale = int(motif_binaire, 2)

            #Assigner la valeur décimale au pixel correspondant dans le résultat de la transformation
            resultat_transformation[y, x] = valeur_decimale

    return image_trasf_1




#### Test à faire

# Cette fonction transforme les données visuelles complexes d’une image en ensembles de caractéristiques plus simples et plus significatives.

# Arguments image_gris (numpy.ndarray):
    # Un tableau 2D NumPy représentant une image en niveaux de gris.
    # rayon (int): Un entier spécifiant le rayon du voisinage à considérer pour chaque pixel lors de la transformation.
# Retourne numpy.ndarray:
    # Un tableau 2D NumPy résultant de la transformation appliquée.
    # Cette transformation est basée sur le rayon spécifié et peut modifier les caractéristiques visuelles originales de l'image.

def appliquer_transformation_2(image_array, radius):
    # Créer un tableau pour stocker les résultats de la transformation
    resultat_transformation = np.zeros_like(image_array, dtype=np.float32)

    # Dimensions de l'image
    hauteur, largeur = image_array.shape

    # Parcourir chaque pixel de l'image
    for y in range(rayon, hauteur - radius):  # Ignorer les bords pour éviter les problèmes
        for x in range(rayon, largeur - radius):
            # Calculer la valeur de sortie O(x,y) pour chaque pixel en utilisant la formule donnée
            valeur_sortie = (
                    np.log10(1 + abs(image_array[y, x + radius] - 2 * image_array[y, x] + image_array[y, x - radius])) +
                    np.log10(1 + abs(image_array[y + radius, x] - 2 * image_array[y, x] + image_array[y - radius, x])) +
                    np.log10(1 + abs(image_array[y - rayon, x + radius] - 2 * image_array[y, x] + image_array[y + radius, x - radius]))
            )

            # Assigner la valeur de sortie au pixel correspondant dans le résultat de la transformation
            resultat_transformation[y, x] = valeur_sortie

    # Remplacer les valeurs des pixels de bord par zéro
    resultat_transformation[:radius, :] = 0
    resultat_transformation[-radius:, :] = 0
    resultat_transformation[:, :radius] = 0
    resultat_transformation[:, -radius:] = 0

    # Convertir la matrice résultante de float à int
    resultat_transformation = resultat_transformation.astype(np.int)

    return image_trasf_2
