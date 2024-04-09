#### Test à faire

# Section 12
    # Segmentation de données en groupes basée sur les histogrammes des points


# Cette fonction divise un ensemble de points dans un plan 2D en un nombre défini de groupes.

# Arguments data (numpy.ndarray):
    # Un tableau 2d numpy représentant l'ensemble de données à partitionner. Chaque ligne du tableau représente un histogramme décrivant un point.
    # k (int): Le nombre de groupes à identifier dans l'ensemble de données.
    # max_iterations (int): Le nombre maximal d'itérations que l'algorithme exécutera. La valeur par défaut est 50.
# Retourne numpy.ndarray:
    # Un tableau numpy 1D où chaque élément correspond à l'indice du centre le plus proche pour chaque point de l'ensemble de données.
    # C'est un vecteur d'entiers de la même longueur que le nombre de points dans 'data', indiquant l'affectation de groupe pour chaque point.

def regrouper_points(data, k, max_iterations=50):

    # Initialiser les centres de groupes aléatoirement
    indices_aleatoires = np.random.choice(len(data), k, replace=False)
    centres = data[indices_aleatoires]

    # Répéter jusqu'à convergence ou jusqu'au nombre maximal d'itérations
    for _ in range(max_iterations):
        # Assigner chaque point au groupe le plus proche
        groupes = []
        for point in data:
            distances = [calcul_distance_1(point, centre) for centre in centres]
            groupe = np.argmin(distances)
            groupes.append(groupe)

        # Mettre à jour les centres de groupe
        nouveaux_centres = []
        for groupe in range(k):
            points_groupe = data[np.array(groupes) == groupe]
            centre_groupe = np.mean(points_groupe, axis=0)
            nouveaux_centres.append(centre_groupe)

        # Vérifier la convergence
        if np.allclose(centres, nouveaux_centres):
            break

        centres = np.array(nouveaux_centres)

    return np.array(groupes)