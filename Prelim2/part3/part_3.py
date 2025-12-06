# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 2.
Ceci est le fichier template pour la partie 3 du Prelim 2.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Literal, Self

colors = Literal["R"] | Literal["G"] | Literal["B"] | Literal["Y"]


@dataclass
class Tile:
    launch: colors | None
    color: colors
    step: int
    gadget: Literal["fan"] | Literal["core"] | Literal["turbine"] | None
    airway: Literal["entry"] | Literal["target"]
    final: bool

    def parse(s: str) -> Self:
        def idx_or_none(s, i):
            return s[i] if i < len(s) else None
        
        if idx_or_none(s, 1) == "L":
            launch = s[2]
            s = s[4:]
        else:
            launch = None
        
        color = s[0]
        step = s[2]
        s = s[4:]
        
        if idx_or_none(s, 1)  == "G":
            match s[2]:
                case 'C':
                    gadget = "core"
                case 'F':
                    gadget = "fan"
                case 'T':
                    gadget = 'turbine'
                case _:
                    gadget = None
            s = s[4:]
        else:
            gadget = None
        
        if idx_or_none(s, 1)  == 'T':
            airway = 'target'
            s = s[3:]
        elif idx_or_none(s, 1) == 'E':
            airway = 'entry'
            s = s[3:]
        else:
            airway = None

        final = idx_or_none(s, 1) == 'F'
        
        return Tile(launch=launch,
                    color=color,
                    step=step,
                    gadget=gadget,
                    airway=airway,
                    final=final)


def part_3(
    main_path: list[str],
    red_final: list[str],
    blue_final: list[str],
    yellow_final: list[str],
    green_final: list[str],
    team: str,
):
    """
    Find the minimum number of turns required for your team to reach the destination.

    Parameters:
        main_path list[str]: The array of 52 strings representing each space on the main path.
        red_final list[str]: The array of 6 strings representing each space on the red final path.
        blue_final list[str]: The array of 6 strings representing each space on the blue final path.
        yellow_final: list[str]: The array of 6 strings representing each space on the yellow final path.
        green_final list[str]: The array of 6 strings representing each space on the green final path.
        team str: The color of your team ('R', 'B', 'Y', or 'G').

    Returns:
    [int]: The single integer representing the minimum number of turns required for your plane to reach the destination.
    """
    turn = 0
    
    position = 0
    target = 0
    
    board: list[Tile] = [Tile.parse(t) for t in main_path]
    
    def tile(idx) -> Tile:
        return idx % len(board)

    
    # for pos, t in enumerate(board):
    #     if t.final == team:
    #         target = pos
    #         break
    # else:
    #     print("couldnt find start pos")
    
    
    # find where you start according to the team
    
    for pos, t in enumerate(board):
        if t.launch == team:
            start_offset = pos
            break
    else:
        print("couldnt find start pos")
        
    airway_target_pos = board.index(next(
        tile for tile in board 
        if tile.airway == "target" and tile.color == team
        ))
    
    gadget = None
    position = start_offset
    
    while True:
        turn +=1
        idx = start_offset + position
        t = tile(idx)
        
        moveby = t.step
        
        match gadget:
            case 'fan': 
                moveby += 3
            case 'core': 
                moveby *=2
            case 'turbine': 
                moveby *=3
        
        if t.airway == 'entry':
            end_position = airway_target_pos
            print("airway!")
            # TODO: return?
        
        
        if t.gadget:
            gadget = t.gadget
        print(f"Turn {turn}: From main path position {position} -> Move {t.step} steps to main path position {position}")
        
        position = end_position
    return turn
