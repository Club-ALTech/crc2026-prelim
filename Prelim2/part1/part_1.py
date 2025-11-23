# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 2.
Ceci est le fichier template pour la partie 1 du Prelim 2.
"""


"""
    TODO : What if there is at least two longest ladders? Which one should be used?
           Should we simulate the game in each case and pick the one with the min steps?
    TODO : Test all the possible cases, don't be lazy o-o
"""


def get_longest_ladder(ladders: list[tuple[int, int]]):
    return max(ladders, key=lambda ladder: ladder[1] - ladder[0])


def should_be_avoided(snakes: list[tuple[int, int]], ladders: list[tuple[int, int]], next_position: int, next_targeted_ladder: tuple[int, int]) -> bool:
    for snake in snakes:
        # If the next position contains a snake head, then avoid it
        if next_position == snake[0]:
            return True
        
    if next_targeted_ladder:
        for ladder in ladders:
            # If the next position contains the start of a ladder we're not targeting and it's in the way, then avoid it
            if next_position == ladder[0] and ladder != next_targeted_ladder:
                return True
        
    return False


def get_next_targeted_ladder(position: int, ladders: list[tuple[int, int]]):
    # All the useful ladders that will help us reach the longest one (included), aka shortest way
    targets: list[tuple[int, int]] = []

    if not ladders:
        return None
    
    longest_ladder = get_longest_ladder(ladders)

    if not longest_ladder:
        return None
    
    # If we already used or passed the longest ladder, then if there is still ladders remaining, use them
    if position >= longest_ladder[1]:
        if ladders[ladders.index(longest_ladder) + 1:]:
            return get_next_targeted_ladder(position, ladders[ladders.index(longest_ladder) + 1:])
        return None

    # Find the ladders that will help us reach the longest one, or finish the game (pos 100)
    for ladder in ladders:
        """ 
            If we still haven't passed the ladder AND :
                - It's before the longest one BUT : its end is before the longest one's start
                    (   It's supposed to be helping us reach the longest one, faster    )
                OR
                - It's the longest one itself
                OR
                - It comes after the longest one : will help us end the game faster
        """
        if position < ladder[0] and (ladder[1] <= longest_ladder[0] or ladder == longest_ladder or longest_ladder[1] < ladder[0]):
            targets.append(ladder)
        
    if targets:
        return targets[0]
    
    return None
    

def get_next_move(d: int, position: int, ladders: list[tuple[int, int]], snakes: list[tuple[int, int]], target: int) -> int:    
    # The distance separating the current position from the target
    moves_remaining = target - position

    # If the distance remaining is greater than 'd', then move with d blocks (max)
    if moves_remaining > d:
        moves_remaining = d

    next_targeted_ladder = get_next_targeted_ladder(position, ladders)

    if next_targeted_ladder:
        # If moving 'd' blocks takes us past the end of the targeted ladder, then it's useless, just move normally (check TEST 3)
        if d + position > next_targeted_ladder[1]:
            moves_remaining = d

    # Before moving, check if the target should be avoided (snakes ... etc)
    while should_be_avoided(snakes, ladders, moves_remaining + position, next_targeted_ladder):
        moves_remaining -= 1

    return moves_remaining


def part_1(d: int, ladders: list[tuple[int, int]], snakes: list[tuple[int, int]]):
    """
    Find the minimum amount of steps to complet Snakes and ladders

    Parameters:
        d int: The maximum value you can move per turn
        ladders list[tuple[int, int]]: The start and end coordinates of the ladders
        snakes list[tuple[int, int]]: The start and end coordinates of the snakes

    Returns:
        int: The minimum amount of steps
    """
    steps = 0
    ### YOUR CODE GOES HERE ###
    current_position = 0
    next_targeted_ladder: tuple[int, int]

    while current_position != 100:
        next_targeted_ladder = get_next_targeted_ladder(current_position, ladders)

        if next_targeted_ladder:
            while current_position < next_targeted_ladder[0]:
                current_position += get_next_move(d, current_position, ladders, snakes, next_targeted_ladder[0])
                steps += 1
                print(current_position, steps)

            if current_position < next_targeted_ladder[1]:
                current_position = next_targeted_ladder[1]
                print(current_position, steps)
        else:
            current_position += get_next_move(d, current_position, ladders, snakes, 100)
            steps += 1
            print(current_position, steps)

    return steps




part_1(
    d = 6,
    ladders = [(1, 38), (4, 14),(21, 42), (28, 84)],
    snakes = [(48, 26), (49, 11), (62, 19), (87, 24)]
)

print("==================================")
part_1(
    d = 8,
    ladders = [(7, 50)],
    snakes = [(80, 30)]
)

print("==================================")
part_1(
    d = 10,
    ladders = [(4, 9), (41, 99)],
    snakes = [(31, 5), (50, 20)]
)

print("==================================")
part_1(
    d = 6,
    ladders = [(1, 38), (4, 14),(21, 42), (28, 84), (88, 99)],
    snakes = [(48, 26), (49, 11), (62, 19), (87, 24)]
)

""" print("==================================")
part_1(
    d = 6,
    ladders = [(1, 38), (4, 14), (8, 18), (21, 42), (28, 84)],
    snakes = [(48, 26), (49, 11), (62, 19), (87, 24)]
)

print("==================================")
part_1(
    d = 6,
    ladders = [(1, 38), (4, 14), (8, 18), (21, 42), (28, 50), (51, 73)],
    snakes = [(48, 26), (49, 11), (62, 19), (87, 24)]
)

print("==================================")
part_1(
    d = 6,
    ladders = [(1, 11), (4, 14), (8, 28), (21, 41), (51, 71)],
    snakes = [(48, 26), (49, 11), (62, 19), (87, 24)]
)
 """
