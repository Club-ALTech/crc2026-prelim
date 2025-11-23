### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from collections import Counter
from part4 import Tile, Board, part_4

tileSet1 = [
    Tile("crgr", 1, 1)
] # With Tile("ggrr")

board1 = Board(3, 3)
board1.populate(tileSet1)

tileSet2 = [
    Tile("crgr", 1, 1),
    Tile("ccrr", 1, 2),
    Tile("rgrr", 2, 2)
] # With Tile("rgrr")

board2 = Board(4, 4)
board2.populate(tileSet2)

tileSet3 = [
    Tile("grrg", 1, 2),
    Tile("rrrr", 1, 3),
    Tile("ccgg", 2, 1),
    Tile("rccc", 2, 2),
    Tile("rrcc", 2, 3),
    Tile("rggr", 2, 4),
    Tile("grrg", 3, 1),
    Tile("crgr", 3, 3),
    Tile("ggrr", 3, 4),
    Tile("grgr", 4, 2),
    Tile("ggrr", 4, 3)
] # With Tile("crgr")

board3 = Board(6, 6)
board3.populate(tileSet3)

def test_from_problem_description():
    assert Counter(part_4(Tile("ggrr"), board1)) == Counter([
        (1, 0),
        (1, 2),
        (2, 1)
    ])

    assert Counter(part_4(Tile("rgrr"), board2)) == Counter([
        (1, 0),
        (2, 1),
        (2, 3),
        (3, 2)
    ])
    
    assert Counter(part_4(Tile("crgr"), board3)) == Counter([
        (0, 2),
        (0, 3),
        (2, 0),
        (2, 5),
        (3, 0),
        (3, 2),
        (3, 5),
        (4, 4),
        (5, 2),
        (5, 3)
    ])
