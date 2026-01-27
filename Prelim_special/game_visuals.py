import pygame

FLOOR_SIZE = 40         # 60×60
WALL_THICKNESS = 6     # 10 px thickness
CONNECTOR_SIZE = 6     # 10×10

PENGUIN_SPEED = 8  # pixels per frame (tweak to adjust sliding speed)

PENGUIN_COLORS = {
    "R": (255, 0, 0),
    "G": (0, 255, 0),
    "B": (0, 128, 255),
    "Y": (255, 255, 0),
}

def init_pygame(board, name="Penguin Slide Arena"):
    pygame.init()
    width = board.cols * FLOOR_SIZE + (board.cols+1) * WALL_THICKNESS
    height = board.rows * FLOOR_SIZE + (board.rows+1) * WALL_THICKNESS
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    return screen

def get_tile_rect(tile):
    x = tile.x
    y = tile.y

    # floor (odd, odd)
    if x % 2 == 1 and y % 2 == 1:
        w = FLOOR_SIZE
        h = FLOOR_SIZE

    # vertical wall (even, odd): 10x80
    elif x % 2 == 0 and y % 2 == 1:
        w = WALL_THICKNESS
        h = FLOOR_SIZE

    # horizontal wall (odd, even): 80x10
    elif x % 2 == 1 and y % 2 == 0:
        w = FLOOR_SIZE
        h = WALL_THICKNESS

    # connector (even, even): 10x10
    else:
        w = CONNECTOR_SIZE
        h = CONNECTOR_SIZE

    # Convert grid coordinate to pixel position
    px = compute_pixel_x(x)
    py = compute_pixel_y(y)

    return pygame.Rect(px, py, w, h)

def compute_pixel_x(x):
    px = 0
    for i in range(x):
        if i % 2 == 1:     # odd = floor tile or horizontal wall
            px += FLOOR_SIZE
        else:             # even = vertical wall or connector
            px += WALL_THICKNESS
    return px


def compute_pixel_y(y):
    py = 0
    for j in range(y):
        if j % 2 == 1:     # odd = floor tile or vertical wall
            py += FLOOR_SIZE
        else:             # even = horizontal wall or connector
            py += WALL_THICKNESS
    return py


def draw_board(screen, board):
    for row in board.tiles:
        for tile in row:
            draw_tile(screen, tile)

    # draw penguins on top
    draw_penguins(screen, board.penguins)
    (x, y, color) = board.fish
    draw_fish(screen, x, y, color)


def draw_tile(screen, tile):
    rect = get_tile_rect(tile)

    x = tile.x
    y = tile.y
    # floor (odd, odd)
    if x % 2 == 1 and y % 2 == 1:
        pygame.draw.rect(screen, (200, 200, 200), rect)

    # wall (even, odd) or (odd, even): 10x80 or 80x10
    elif (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
        if tile.content.strip() == 'W':
            pygame.draw.rect(screen, (20, 20, 20), rect)  # walls
        else:
            pygame.draw.rect(screen, (180, 180, 180), rect)  # walls

    # connector (even, even): 10x10
    else:
        if tile.content.strip() != '':
            pygame.draw.rect(screen, (20, 20, 20), rect)  # walls
        else:
            pygame.draw.rect(screen, (180, 180, 180), rect)  # walls


COLOR_MAP = {
    'R': (255, 50, 50),
    'G': (50, 200, 50),
    'B': (50, 100, 255),
    'Y': (255, 220, 50)
}
def draw_penguins(screen, penguins):
    for penguin in penguins:
        draw_penguin(screen, penguin)

def draw_fish(screen, x, y, color):
    px = compute_pixel_x(x)
    py = compute_pixel_y(y)
    rect = pygame.Rect(px, py, FLOOR_SIZE, FLOOR_SIZE)
    cx = rect.centerx
    cy = rect.centery

    img_name = "F" + color.strip() 
    img_full_path = "./sprites/"+img_name+'.png'

    image_surface = pygame.image.load(img_full_path).convert_alpha()
    screen.blit(image_surface, (cx-25, cy-25))


def draw_penguin(screen, penguin):
    px = compute_pixel_x(penguin.x)
    py = compute_pixel_y(penguin.y)
    rect = pygame.Rect(px, py, FLOOR_SIZE, FLOOR_SIZE)

    cx = rect.centerx
    cy = rect.centery
    img_name = "P" + penguin.color.strip() 
    img_full_path = "./sprites/"+img_name+'.png'

    image_surface = pygame.image.load(img_full_path).convert_alpha()
    screen.blit(image_surface, (cx-25, cy-25))

def slide_penguin(penguin, dx, dy):
    target_x = penguin.x + dx
    target_y = penguin.y + dy

    penguin.x = target_x
    penguin.y = target_y

def animate_penguins(board):
    all_done = False
    while not all_done:
        all_done = True
        for p in board.penguins:
            # distance left to travel
            diff_x = p.x - p.fx
            diff_y = p.y - p.fy

            if abs(diff_x) > 0.01 or abs(diff_y) > 0.01:
                p.fx += diff_x * 0.25
                p.fy += diff_y * 0.25
                all_done = False

        yield  # return control to main loop

def show_initial_board(screen, board, clock):
    # Draw once
    screen.fill((30, 30, 30))
    draw_board(screen, board)

    draw_penguins(screen, board.penguins)
    pygame.display.flip()

    # Keep it visible for 1 second
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 1000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        clock.tick(60)
    return True

def wait_for_close(screen, board, clock):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 1000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((30, 30, 30))
        draw_board(screen, board)
        draw_penguins(screen, board.penguins)
        pygame.display.flip()
        clock.tick(600)

def move_penguin(board, penguin, direction):
    new_x = penguin.x
    new_y = penguin.y

    # clear board tile from previous penguin position
    board.tiles[penguin.y][penguin.x].content = '   '

    if direction == "U":
        while board.tiles[new_y-1][new_x].content.strip() != 'W' and board.tiles[new_y-2][new_x].content.strip() == '':
            new_y -= 2
    elif direction == 'D':
        while board.tiles[new_y+1][new_x].content.strip() != 'W' and board.tiles[new_y+2][new_x].content.strip() == '':
            new_y += 2
    elif direction == "R":
        while board.tiles[new_y][new_x+1].content.strip() != 'W' and board.tiles[new_y][new_x+2].content.strip() == '':
            new_x += 2
    elif direction == 'L':
        while board.tiles[new_y][new_x-1].content.strip() != 'W' and board.tiles[new_y][new_x-1].content.strip() == '':
            new_x -= 2
    
    penguin.x = new_x
    penguin.y = new_y
    # clear board tile from previous penguin position
    board.tiles[new_y][new_x].content = f" {penguin.color} "


def run_pygame_animation(board, moves, name = ""):
    print("Animation starting...")
    screen = init_pygame(board, name)
    clock = pygame.time.Clock()

    # Initialize floating positions
    for p in board.penguins:
        p.fx = p.x
        p.fy = p.y

    # Show initial board for 1 second
    if not show_initial_board(screen, board, clock):
        pygame.quit()
        return

    # Process moves (stepping version)
    for move in moves:
        color = move[0]
        direction = move[1]
        for penguin in board.penguins:
            if penguin.color.strip() == color:
                move_penguin(board, penguin, direction)

        # draw updated board
        screen.fill((20, 20, 20))
        draw_board(screen, board)
        draw_penguins(screen, board.penguins)
        pygame.display.flip()

        pygame.time.wait(500)  # 0.5s between moves

    # Final board stays visible until user closes window
    wait_for_close(screen, board, clock)
    pygame.quit()


