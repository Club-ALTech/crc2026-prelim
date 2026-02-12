from copy import copy
from enum import StrEnum
from dataclasses import dataclass
from itertools import product

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
    [14.5, 2.5, 9.5] + BOARD_BOUNDS,
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
        return Actor(t[0], t[1], t[2].upper())

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
            return x, next_wall + 0.5
        case Direction.DOWN:
            (next_wall, *_) = sorted(
                (wy for wy in vertical_walls if wy > y), reverse=False
            )
            return x, next_wall - 0.5
        case Direction.LEFT:
            (next_wall, *_) = sorted(
                (wx for wx in horizontal_walls if wx < x), reverse=True
            )
            return next_wall + 0.5, y
        case Direction.RIGHT:
            (next_wall, *_) = sorted(
                (wx for wx in horizontal_walls if wx > wx), reverse=False
            )
            return next_wall - 0.5, y


@dataclass
class GameState:
    penguins: dict[Color, Actor]
    fish: Actor

    def win(self):
        p = self.penguins[self.fish.color]
        return p.x == self.fish.x and p.y == self.fish.y
    
    def next_state(self, move: Move):
        ps = copy(self.penguins)
        p = ps.pop(self.fish.color)
        (x, y) = find_boundary(
            start_coords=(p.x, p.y), 
            direction=move.direction,
            obstacles=ps)
        if p.x == x and p.y == y:
           return None # NOTE: state didnt change,
        p.x = x
        p.y = y
        ps[p.color] = p
        return GameState(fish=self.fish, penguins=ps)
    

@dataclass
class Node:
    parent: None | "Node"
    children: list["Node"]
    game_state: GameState
    previous_move: Move | None


def solve(penguins: list[tuple[int, int, str]], fish: tuple[int, int, str], board):
    """
    Solve the problem as fast and accurately as possible

    Returns:
        [String]: The list of moves to apply
    """
    penguins = [Actor.pack(*p) for p in penguins]
    fish = Actor.pack(*fish)

    possible_moves = [Move(direction=dir, penguin_color=color) for dir, color in product(Direction, Color)]
    initial_state = GameState(penguins=penguins, fish=fish)
    
    tree = Node(parent=None, value=(initial_state, None))
    leaves=[tree]
    while True:
        for node in leaves:
            new_leaves = []
            for move in possible_moves:
                next_state = node.state.next_state(move)
                if next_state is None:
                    # dead end
                    continue
                if next_state.win():
                    # TODO: pop the tree, somehow
                    pass
                
                nnode = Node(parent=node, value=(next_state, move))
                node.children.append(node)
                new_leaves.append(nnode)
            leaves = new_leaves
            
    
    
    leaves = [initial_state]
    while True:
        new_leaves = []
        for leaf in leaves:
            for move in possible_moves:
                next_state = leaf.next_state(move)
                if next_state is None:
                    # dead end
                    continue
                if next_state.win():
                    # TODO: pop the tree, somehow
                    pass
                new_leaves.append(next_state)
        leaves = new_leaves
            
        

    # return moves
