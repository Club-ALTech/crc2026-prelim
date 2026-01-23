# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 3.
Ceci est le fichier template pour la partie 2 du Prelim 3.
"""
import math

## Constants
G = -9.81
PI = math.pi
MASS = 0.175
AIR_DENSITY = 1.23
AREA = 0.0568
CL0 = 0.1 ## Lift coeff at apha=0
CLA = 1.4 ## Lift coeff dependant on alpha
CD0 = 0.08 ## Drag coeff at alpha=0
CDA = 2.72 ## Drag coeff dependant on alpha
ALPHA0 = -4

DELTA_T = 0.01
START_X = 0
START_Y = 1

def part_2(vx0: float, vy0: float, angle_deg: float):
    """
    Simulate the path of a frisbee

    Parameters:
        vx0 float: The initial velocity in x
        vy0 float: The initial velocity in y
        angle_deg float: The angle of the frisbee in degrees

    Returns:
        [tuple[float, float]]: The coordinates in x and y along the trajectory of the frisbee
    """
    coordinates = []
    ### You code goes here ###
    ### Votre code va ici ###

    CL = CL0 + CLA * angle_deg * PI / 180
    CD = CD0 + CDA * ((angle_deg - ALPHA0) * PI/180) ** 2

    vx = vx0
    vy = vy0

    x = START_X
    y = START_Y

    for _ in range(0, 100):         
        delta_vx = - AIR_DENSITY * (vx ** 2) * AREA * CD * DELTA_T
        delta_vy = (AIR_DENSITY * (vx ** 2) * AREA * CL * MASS / 2 + G) * DELTA_T
    
        vx = delta_vx + vx
        vy = delta_vy + vy

        x = x + vx * DELTA_T
        y = y + vy * DELTA_T

        if y <= 0:
            break

        coordinates.append((round(x, 3), round(y, 3)))

    return coordinates