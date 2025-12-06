# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements

"""part_5.py
This is the template file for the part 5 of the Prelim 2.
Ceci est le fichier template pour la partie 5 du Prelim 2.
"""

class Tile:
    # g = Grass
    # r = Road
    # c = Castle
    # n = None (only used for blank tiles)
    def __init__(self, sides = "nnnn", pos_x = 0, pos_y = 0):
        self.sides = list(sides[:4])    # List of all 4 sides
        self.x = pos_x
        self.y = pos_y
   
    @property
    def top(self):
        return self.sides[0]
    
    @property
    def right(self):
        return self.sides[1]

    @property
    def bottom(self):
        return self.sides[2]
    
    @property
    def left(self):
        return self.sides[3]
    
    def __getitem__(self, index):
        return self.sides[index]

    def __repr__(self):
        return f"Tile('{self.top + self.right + self.bottom + self.left}', x={self.x}, y={self.y})"

    def __str__(self):
        return f"{self.top + self.right + self.bottom + self.left}"
    
    def __len__(self):
        return len(self.sides)
    
    def to_ascii(self):
        t = ' ' if self.top == 'n' else self.top
        r = ' ' if self.right == 'n' else self.right
        b = ' ' if self.bottom == 'n' else self.bottom
        l = ' ' if self.left == 'n' else self.left

        top_row    = f"┌─ {t} ─┐"
        middle_row = f"{l}     {r}"
        bottom_row = f"└─ {b} ─┘"

        return [top_row, middle_row, bottom_row]
    
    def is_blank(self):
        return True if self.sides[0] == "n" else False

    def rotate(self):
        self.sides.insert(0, self.sides.pop())
    

class Board:
    def __init__(self, rows, cols):
        self.board = [[Tile("nnnn") for j in range(cols)] for i in range(rows)]

    def __repr__(self):
        return self.board

    def __str__(self):
        lines = []

        for row in self.board:
            ascii_tiles = [tile.to_ascii() for tile in row]

            for row in range(3):
                line = " ".join(tile[row] for tile in ascii_tiles)
                lines.append(line)

        return "\n".join(lines)
    
    def __getitem__(self, index):
        return self.board[index]

    def populate(self, tileSet):
        for tile in tileSet:
            self.board[tile.x][tile.y] = tile
    
    def is_valid_placement(self, tile, pos_x, pos_y):
        ### YOUR CODE GOES HERE ###
        ### VOTRE CODE VA ICI ###

        rotation_count = 0
        tile_copy = Tile(tile.sides)
        
        while rotation_count < 4:
            top_is_valid = False
            right_is_valid = False
            bottom_is_valid = False
            left_is_valid = False

            if pos_y - 1 < 0 or (
                self.board[pos_y - 1][pos_x].is_blank() or 
                tile_copy.top == self.board[pos_y - 1][pos_x].bottom
            ):
                top_is_valid = True

            if pos_x + 1 >= len(self.board[pos_y]) or (
                self.board[pos_y][pos_x + 1].is_blank() or 
                tile_copy.right == self.board[pos_y][pos_x + 1].left
            ):
                right_is_valid = True

            if pos_y + 1 >= len(self.board) or (
                self.board[pos_y + 1][pos_x].is_blank() or 
                tile_copy.bottom == self.board[pos_y + 1][pos_x].top
            ):
                bottom_is_valid = True

            if pos_x - 1 < 0 or (
                self.board[pos_y][pos_x - 1].is_blank() or 
                tile_copy.left == self.board[pos_y][pos_x - 1].right
            ):
                left_is_valid = True

            if top_is_valid and right_is_valid and bottom_is_valid and left_is_valid:
                return True
            
            tile_copy.rotate()
            rotation_count += 1
        
        return False

    def is_adjacent(self, pos_x, pos_y):
        ### YOUR CODE GOES HERE ###
        ### VOTRE CODE VA ICI ###

        return self.board[pos_y][pos_x].is_blank() and (
            pos_y - 1 >= 0 and not self.board[pos_y - 1][pos_x].is_blank() or
            pos_x + 1 < len(self.board[pos_y]) and not self.board[pos_y][pos_x + 1].is_blank() or
            pos_y + 1 < len(self.board) and not self.board[pos_y + 1][pos_x].is_blank() or
            pos_x - 1 >= 0 and not self.board[pos_y][pos_x - 1].is_blank()
        )


def part_4(tile: Tile, board: Board):
    """
    Find all possible locations the given Tile can be placed on the Board

    Parameters:
        tile Tile: A Tile object with a set of 4 sides with a different structure
        board Board: A 2D array filled with Tiles
    Returns:
        list[Tuple[int, int]]: An ordered list of coordinates where the tile can be placed on the board
    """

    positions = []
    ### YOUR CODE GOES HERE ###
    ### VOTRE CODE VA ICI ###

    adjacent_positions = []
    
    for y in range(len(board.board)):
        for x in range(len(board[y])):
            if board.is_adjacent(x, y):
                adjacent_positions.append((y, x))

    for position in adjacent_positions:
        if board.is_valid_placement(tile, position[1], position[0]):
            positions.append(position)

    return positions