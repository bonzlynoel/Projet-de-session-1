from coordonnees_clou import calculer_reflexion_point, calculer_rotate_point,calculer_inclinaison_point

'''
Cette fonction prend un ensemble de points clés représentant un clou et applique trois types de transformation géométrique.(rotation,réflexion,inclinaision)
chaque transformation est appliquée séquentiellement à tous les points clés.

Arguments : 
    points_clou (list) : Une liste de tuple de laquelle chaque tuples contient : une Chaine de caractères ( nom du point) et un tuple de deux nombres (float, float)
        représentant les coordonnées du point dans un plan 2D
    center_rotation( tuple) : représente les coordonnées du centre de rotation 
    angle_rotation (float) : l'angle de rotation en degrés
    angle_inclinaison (float) : l'angle d'inclinaison en degrés
    direction_inclinaison (float) : la direction de l'inclinaison ('x' ou 'y')
    axe_reflexion (str) : l'axe de reflexion ('x' ou 'y')
Retourne : 
    tuple : trois listes de tuple de lesquelles chaque tuples contient : une Chaine de caractères ( nom du point) et un tuple de deux nombres (float, float)
        représentant les coordonnées du point dans un plan 2D après chaque transformation.

'''
def appliquer_transformation_clou(points_clou,center_rotation,angle_rotation,direction_inclinaison,angle_inclinaison,axe_reflexion):
    reflexion_points = [0]*(len(points_clou))
    rotation_points = [0]*(len(points_clou))
    inclinaison_points = [0]*(len(points_clou))
    a=()
    i=0

    for points in points_clou:
        #print(f'{points[1]}')
        a = points[0],calculer_reflexion_point(points[1],axe_reflexion)
        b = points[0],calculer_rotate_point(points[1], angle_rotation, center_rotation)
        c = points[0],calculer_inclinaison_point(points[1], angle_inclinaison, direction_inclinaison)
        reflexion_points[i]= a
        rotation_points[i]=b
        inclinaison_points[i]=c
        i+=1

        #print(f'{reflexion_points,rotation_points,inclinaison_points}')

    return reflexion_points,rotation_points,inclinaison_points

'''
if __name__=='__main__':
    appliquer_transformation_clou([('pt_0', (-5.0, 0.5)), ('pt_1', (-5.0, -0.5)), ('pt_2',
 (-5.75, -1.5)), ('pt_3', (-5.75, 1.5)), ('pk_0', (7.0, 0)), ('pk_1', (5.0, -0.5)), ('pk_2', (5.0,0.5))],(0,0),30,'x',20,'x')
'''
