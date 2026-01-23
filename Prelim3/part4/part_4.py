# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 3.
Ceci est le fichier template pour la partie 4 du Prelim 3.
"""

def part_4(r: int, v: list[int], t: list[int], trafic_dist: list[int], d: list[int]):
    """
    Find the quickest path to get home

    Parameters:
        r int: the number of path
        v list[int]: the speed limit for each path
        t list[int]: the speed limit in trafic
        trafic_dist list[int]: the length of the trafic
        d list[int]: the distance for each path
        
    Returns:
        int: The shortest path's number
    """
    shortest = -1
    ### YOUR CODE GOES HERE ###
    ### VOTRE CODE VA ICI ###

    time = 0
    shortest_time = 0

    for i in range(r):
        time = trafic_dist[i] / t[i] + (d[i] - trafic_dist[i]) / v[i]

        if time < shortest_time or shortest_time == 0:
            shortest_time = time
            shortest = i + 1

    return shortest
