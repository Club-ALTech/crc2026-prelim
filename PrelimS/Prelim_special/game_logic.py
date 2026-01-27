class Penguin:
    # Color is an uppercase letter
    def __init__(self, color: str, pos_x: int = 0, pos_y: int = 0):
        self.color = color
        self.x = pos_x
        self.y = pos_y
        self.px = pos_x
        self.py = pos_y

    def __str__(self):
        return f"{self.color}"

class Tile:
    # content is color of the penguin (R,G,B,Y) or F for Fish or W for Wall or Connector content
    def __init__(self, content: str = ' ', pos_x: int = 0, pos_y: int = 0):
        self.content = content
        self.x = pos_x
        self.y = pos_y
    
    def __getitem__(self):
        return self.content

    def __repr__(self):
        return f"Tile('{self.content}', x={self.x}, y={self.y})"

    def __str__(self):
        if self.content.strip() == 'W':
            return f"{'═══' if self.x%2 != 0 else '║'}"
        return f"{self.content}"
    
    def is_empty(self):
        return self.content.strip() == ''
    
    def is_wall(self):
        return self.content == 'W'

class Board:
    def __init__(self, nbr_rows, nbr_cols, penguins: list[tuple[int, int, str]], fish: tuple[int, int, str], walls: list[tuple[int, int]] = [],):
        self.rows = nbr_rows
        self.cols = nbr_cols
        self.tiles = [[Tile('   ' if x%2==0 and y%2==1 else ' ', y, x) for y in range(2*nbr_rows+1)] for x in range(2*nbr_cols+1)]
        self.penguins = []

        ## Set tiles for receiving content
        for y in range(1, 2*nbr_rows+1, 2):
            for x in range(1, 2*nbr_cols+1, 2):
                self.tiles[y][x] = Tile(content='   ', pos_x=x, pos_y=y)
        
        ## Set perimeter walls
        for y in range(2*nbr_rows+1):
            for x in range(2*nbr_cols+1):
                if ((y==0 or y==2*nbr_rows) and x%2 == 1):
                    self.tiles[y][x] = Tile(content='W', pos_x=x, pos_y=y)
                if ((x==0 or x==2*nbr_cols) and y%2 == 1):
                    self.tiles[y][x] = Tile(content='W', pos_x=x, pos_y=y)

        for (x, y) in walls:
            self.tiles[y][x] = Tile(content='W', pos_x=x, pos_y=y)

        connection_mapping= {'tr': '╚', 'tb': '║', 'tl': '╝', 'rb': '╔', 'rl': '═', 'bl': '╗', 'trb': '╠', 'trl': '╩', 'tbl': '╣', 'rbl': '╦', 'trbl': '╬'}

        # add connectors
        for y in range(0, 2*nbr_rows+1, 2):
            for x in range(0, 2*nbr_cols+1, 2):
                s = ""
                try:
                    if self.tiles[y-1][x].is_wall():
                        s = f"{s}t"
                except:
                    pass
                try:
                    if self.tiles[y][x+1].is_wall():
                        s = f"{s}r"
                except:
                    pass
                try:
                    if self.tiles[y+1][x].is_wall():
                        s = f"{s}b"
                except:
                    pass
                try:
                    if self.tiles[y][x-1].is_wall():
                        s = f"{s}l"
                except:
                    pass
                connector = connection_mapping.get(s, ' ')
                self.tiles[y][x] = Tile(connector, pos_x=x, pos_y=y)

        # add penguins
        for (x, y, col) in penguins:
            self.penguins.append(Penguin(color=col, pos_x=x, pos_y=y))
            self.tiles[y][x] = Tile(content=col, pos_x=x, pos_y=y)
        # add Fish
        self.fish = fish

    def __repr__(self):
        return self.tiles

    def __str__(self):
        lines = []
        for row in self.tiles:
            line_str = "".join(tile.__str__() for tile in row)
            lines.append(line_str)

        return "\n".join(lines)
    
    def __getitem__(self, index):
        pass
        return self.tiles[index]

    def move_penguin(self, penguin, direction):
        new_x = penguin.x
        new_y = penguin.y

        # clear board tile from previous penguin position
        self.tiles[penguin.y][penguin.x].content = '   '

        if direction == "U":
            while self.tiles[new_y-1][new_x].content.strip() != 'W' and self.tiles[new_y-2][new_x].content.strip() == '':
                new_y -= 2
        elif direction == 'D':
            while self.tiles[new_y+1][new_x].content.strip() != 'W' and self.tiles[new_y+2][new_x].content.strip() == '':
                new_y += 2
        elif direction == "R":
            while self.tiles[new_y][new_x+1].content.strip() != 'W' and self.tiles[new_y][new_x+2].content.strip() == '':
                new_x += 2
        elif direction == 'L':
            while self.tiles[new_y][new_x-1].content.strip() != 'W' and self.tiles[new_y][new_x-1].content.strip() == '':
                new_x -= 2
        
        penguin.x = new_x
        penguin.y = new_y
        # clear board tile from previous penguin position
        self.tiles[new_y][new_x].content = f" {penguin.color} "

    def test_path(self, moves, goal):
        for move in moves:
            color = move[0]
            direction = move[1]
            for penguin in self.penguins:
                if penguin.color.strip() == color:
                    self.move_penguin(penguin, direction)
                if penguin.x == goal[0] and penguin.y == goal[1]:
                    return True
        return False
