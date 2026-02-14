# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 4.
Ceci est le fichier template pour la partie 4 du Prelim 4.
"""

from math import acos

PI = 3.141592653589793
epsilon = 1e-12

def supposed_angles(sides):
    return ((sides-2) * 180)

def radian_to_degree(radian):
    return ((radian * 180) / PI)

def distance(line):
    diff_x = (line[1][0] - line[0][0]) ** 2
    diff_y = (line[1][1] - line[0][1]) ** 2
    dist = (diff_x + diff_y) ** 0.5
    return dist

def create_lines(coordinates):
    lines = []
    size = len(coordinates)
    for i in range(size):
        lines.append([coordinates[i],coordinates[(i+1)%size]])
    return lines

def get_angle(lines,distances):
    begin_line = lines[0][0]
    end_line = lines[1][1]
    new_line = [begin_line,end_line]
    a = distances[0]
    b = distances[1]
    c = distance(new_line)
    cos = ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b)
    angle = radian_to_degree(acos(cos))
    
    return angle


def part_4(coordinates: list[tuple[int, int]]):
    """
    Is that shape convex?

    Parameters:
        coordinates list[tuple[int, int]]: list of coordinates

    Returns:
        bool: can the coordinates be linked to form a convex polygon
    """

    is_convex = False
    ### YOUR CODE GOES HERE ###

    lines = create_lines(coordinates)
    distances = []
    some_lines = [] 
    some_distances = []
    side = len(lines)
    angles = []

    for line in lines:
        distances.append(distance(line))

    for i in range(side):
        some_lines.append(lines[i])
        some_lines.append(lines[(i+1)%side])
        some_distances.append(distances[i])
        some_distances.append(distances[(i+1)%side])
        angle = get_angle(some_lines,some_distances)
        angles.append(angle)
        some_lines = []
        some_distances = []

    polygon_angle = supposed_angles(side)
    max_value = polygon_angle + epsilon
    min_value = polygon_angle - epsilon
    all_angles = sum(angles)
    
    if(all_angles >= min_value and all_angles <= max_value):
        is_convex = True

    return is_convex

print(part_4([(-6, -15), (3, 3), (-2, 3), (4, 18), (-8, 0), (-4, 0)]))