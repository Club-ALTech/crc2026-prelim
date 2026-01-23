### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part3.part_3 import part_3

mesures1 = [
    [ (0, 5, 2, 1, 0, -1),
      (1, 3, 3, 0, 0, -1)
    ],
    [ (10, 4, 3, 1, 1, -1),
      (11, 7, 1, 2, 0, 0)
    ],
    [ (20, 3, 3, 1, 0, -1),
      (21, 8, 4, 2, 0, 1),
      (22, 6, 2, 0, 1, -1)
    ],
    [ (30, 9, 2, 2, 0, -1),
      (31, 4, 5, 0, 0, -1)]
] # [1, 10, 22, 30]

mesures2 = [
    [ (0, 4, 3, 0, 0, -1),
      (1, 6, 4, 1, 0, -1)
    ],
    [ (10, 7, 2, 1, 0, -1),
      (11, 5, 3, 2, 0, -1)
    ],
    [ (20, 8, 3, 2, 0, -1),
      (21, 3, 4, 0, 0, -1)
    ],
    [ (30, 9, 2, 0, 0, -1),
      (31, 2, 5, 1, 0, -1)]
] # [0, 10, 20, 30]

mesures3 = [
    [ (0, 6, 3, 1, 0, -1),
      (1, 3, 2, 0, 0, -1)
    ],
    [ (10, 5, 2, 2, 1, -1),
      (11, 4, 4, 1, 0, 0)
    ],
    [ (20, 7, 5, 0, 1, -1),
      (21, 2, 3, 2, 0, 1),
      (22, 9, 3, 1, 0, -1)
    ],
    [ (30, 4, 7, 0, 0, -1),
      (31, 10, 3, 2, 0, -1)]
] # [1, 10, 22, 31]

mesures4 = [
    [ (0, 4, 2, 0, 0, -1),
      (1, 7, 3, 1, 0, -1)
    ],
    [ (10, 3, 4, 1, 1, -1),
      (11, 6, 2, 2, 0, 0)
    ],
    [ (20, 2, 3, 1, 0, 2),
      (21, 9, 4, 2, 0, 2),
      (22, 8, 3, 0, 1, -1)
    ],
    [ (30, 10, 2, 1, 0, -1),
      (31, 5, 5, 0, 0, -1)]
] # [1, 11, 22, 30]

def test_from_problem_description():
    assert part_3(mesures1) == [1, 10, 22, 30]
    assert part_3(mesures2) == [0, 10, 20, 30]
    assert part_3(mesures3) == [1, 10, 22, 31]

def test_supplementaire():
    assert part_3(mesures4) == [1, 11, 22, 30]

