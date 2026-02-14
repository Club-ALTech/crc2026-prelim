from copy import copy
from enum import StrEnum
from dataclasses import dataclass
from itertools import product
from typing import Optional

BOARD_BOUNDS = [-0.5, 15.5]

HORRIZONTAL_WALLS = [
    [5.5, 11.5] + BOARD_BOUNDS,
    [3.5] + BOARD_BOUNDS,
    [6.5] + BOARD_BOUNDS,
    [1.5, 11.5] + BOARD_BOUNDS,
    [4.5, 9.5] + BOARD_BOUNDS,
    BOARD_BOUNDS,
    [3.5] + BOARD_BOUNDS,
    [0.5, 7.5, 10.5] + BOARD_BOUNDS,
    [7.5, 13.5] + BOARD_BOUNDS,
    [4.5] + BOARD_BOUNDS,
    [8.5] + BOARD_BOUNDS,
    [1.5, 11.5] + BOARD_BOUNDS,
    [6.5] + BOARD_BOUNDS,
    [14.5] + BOARD_BOUNDS,
    [2.5, 9.5] + BOARD_BOUNDS,
    [5.5, 11.5] + BOARD_BOUNDS,
]

VERTICAL_WALLS = [
    [4.5, 12.5] + BOARD_BOUNDS,
    [7.5, 10.5] + BOARD_BOUNDS,
    [2.5, 13.5] + BOARD_BOUNDS,
    [6.5] + BOARD_BOUNDS,
    [1.5, 8.5] + BOARD_BOUNDS,
    [3.5] + BOARD_BOUNDS,
    [11.5] + BOARD_BOUNDS,
    [2.5, 7.5] + BOARD_BOUNDS,
    [7.5] + BOARD_BOUNDS,
    [3.5, 9.5] + BOARD_BOUNDS,
    [13.5] + BOARD_BOUNDS,
    [7.5] + BOARD_BOUNDS,
    [2.5, 10.5] + BOARD_BOUNDS,
    [8.5] + BOARD_BOUNDS,
    [13.5] + BOARD_BOUNDS,
    [4.5, 11.5] + BOARD_BOUNDS,
]


class Color(StrEnum):
    RED = "R"
    GREEN = "G"
    BLUE = "B"
    YELLOW = "Y"


class Direction(StrEnum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


@dataclass
class Actor:
    x: int
    y: int
    color: Color

    def pack(t: tuple[int, int, str]):
        return Actor(t[0], t[1], Color(t[2]))

    def unpack(self) -> tuple[int, int, str]:
        return self.x, self.y, self.color


@dataclass
class Move:
    direction: Direction
    penguin_color: Color

    def parse(s: str):
        return Move(direction=Direction(s[1]), penguin_color=Color(s[0]))

    def serialize(self):
        return f"{self.penguin_color.value}{self.direction.value}"


def find_boundary(
    start_coords: tuple[int, int],  # where the penguin we're moving is starting from
    direction: Direction,  # the direction we are moving the penguin
    obstacles: list[tuple[int, int]],  # the locations of the other penguins
) -> tuple[int, int]:
    x, y = start_coords
    vertical_walls = VERTICAL_WALLS[x].copy()
    horizontal_walls = HORRIZONTAL_WALLS[y].copy()
    for ox, oy in obstacles:
        if ox == x:
            vertical_walls.extend([oy - 0.5, oy + 0.5])
        if oy == y:
            horizontal_walls.extend([ox - 0.5, ox + 0.5])

    match direction:
        case Direction.UP:
            (next_wall, *_) = sorted(
                (wy for wy in vertical_walls if wy < y), reverse=True
            )
            return int(x), int(next_wall + 0.5)
        case Direction.DOWN:
            (next_wall, *_) = sorted(
                (wy for wy in vertical_walls if wy > y), reverse=False
            )
            return int(x), int(next_wall - 0.5)
        case Direction.LEFT:
            (next_wall, *_) = sorted(
                (wx for wx in horizontal_walls if wx < x), reverse=True
            )
            return int(next_wall + 0.5), int(y)
        case Direction.RIGHT:
            (next_wall, *_) = sorted(
                (wx for wx in horizontal_walls if wx > x), reverse=False
            )
            return int(next_wall - 0.5), int(y)


@dataclass
class GameState:
    penguins: dict[Color, Actor]
    fish: Actor
    
    def __init__(self, penguins: list[Actor], fish: Actor):
        self.fish = fish
        self.penguins = {}
        for p in penguins:
            self.penguins[p.color] = p

    def win(self):
        p = self.penguins[self.fish.color]
        return p.x == self.fish.x and p.y == self.fish.y

    def next_state(self, move: Move):
        ps = self.penguins.copy()
        p = ps.pop(self.fish.color)
        (x, y) = find_boundary(
            start_coords=(p.x, p.y), direction=move.direction, obstacles=map(lambda o:(o.x, o.y), ps.values())
        )
        if p.x == x and p.y == y:
            return None  # NOTE: state didnt change,
        p = Actor(x, y, p.color)
        ps[p.color] = p
        return GameState(fish=self.fish, penguins=ps.values())


@dataclass
class Node:
    parent: Optional["Node"]
    game_state: GameState
    move: Optional[Move]


def destupid(n: int):
    return int((n-1)/2)

def solve(penguins: list[tuple[int, int, str]], 
          fish: tuple[int, int, str], 
          board):
    """
    Solve the problem as fast and accurately as possible

    Returns:
        [String]: The list of moves to apply
    """
    fish = Actor(x=destupid(fish[0]), y=destupid(fish[1]), color=Color(fish[2]))
    penguins = [
        Actor(x=destupid(x), 
              y=destupid(y), 
              color=Color(c)) 
        for x, y, c 
        in penguins
        if c == fish.color
        ]

    possible_moves =[
        Move(direction=dir, penguin_color=penguins[0].color)
        for dir in product(Direction)
    ]
    initial_state = GameState(penguins=penguins, fish=fish)

    tree = Node(parent=None,
                game_state=initial_state, 
                move=None)
    
    leaves = [tree]
    while True:
        print(len(leaves))
        new_leaves = []
        for leaf in leaves:
            for move in possible_moves:
                next_state = leaf.game_state.next_state(move)
                if next_state is None:
                    # dead end
                    continue
                if next_state.win():
                    # TODO: pop the tree, somehow
                    moves = [move]
                    # print("won")
                    # return []
                    while (node:=node.parent) is not None and node.move is not None:
                        moves.append(node.move)
                    solution = map(Move.serialize, reversed(moves))
                    print(list(solution))
                    return solution
                nnode = Node(parent=leaf,
                             game_state=next_state, 
                             move=move)
                new_leaves.append(nnode)
        leaves = new_leaves
