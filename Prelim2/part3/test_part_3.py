### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part_3 import part_3


def test_from_problem_description_0():
    assert part_3(
        ["G#4#[F]", "R#1#", "B#1#", "[LG]Y#4#", "G#1#", "R#4#", "B#6#[T]", "Y#5#[E]", "G#2#", "R#2#", "B#2#", "Y#4#",
         "G#4#", "R#1#[GF][F]", "B#2#", "Y#2#", "[LR]G#3#", "R#5#", "B#6#[GC]", "Y#2#[T]", "G#2#[E]", "R#6#", "B#3#",
         "Y#4#", "G#2#", "R#5#", "B#2#[F]", "Y#4#", "G#4#", "[LB]R#3#", "B#1#", "Y#3#", "G#4#[T]", "R#3#[E]", "B#1#",
         "Y#4#", "G#4#[GF]", "R#3#", "B#2#", "Y#4#[F]", "G#2#[GC]", "R#6#", "[LY]B#4#", "Y#1#", "G#4#", "R#6#[T]",
         "B#5#[GC][E]", "Y#4#", "G#3#", "R#5#", "B#2#", "Y#6#"],
        ["R#3#[GC]", "R#4#", "R#3#", "R#6#", "R#6#", "R#5#"],
        ["B#6#", "B#3#", "B#4#", "B#5#", "B#6#", "B#1#"],
        ["Y#4#", "Y#5#", "Y#3#", "Y#4#", "Y#6#", "Y#6#"],
        ["G#3#", "G#4#", "G#2#", "G#2#", "G#3#", "G#2#"],
        'B'
    ) == 11


def test_from_problem_description_1():
    assert part_3(
        ["G#6#[F]", "R#6#[GF]", "B#2#[GT]", "[LG]Y#6#", "G#5#[GF]", "R#1#[GC]", "B#6#[GC][T]", "Y#3#[E]", "G#6#[GF]",
         "R#4#", "B#5#", "Y#3#", "G#6#[GT]", "R#1#[F]", "B#2#", "Y#4#", "[LR]G#5#", "R#6#", "B#6#", "Y#1#[T]",
         "G#4#[GF][E]", "R#2#", "B#2#", "Y#4#[GF]", "G#5#", "R#4#", "B#5#[GC][F]", "Y#2#", "G#2#", "[LB]R#6#", "B#6#",
         "Y#3#[GF]", "G#3#[T]", "R#3#[E]", "B#4#", "Y#1#", "G#6#", "R#1#", "B#2#", "Y#3#[F]", "G#6#", "R#2#",
         "[LY]B#6#[GC]", "Y#4#", "G#6#", "R#6#[T]", "B#2#[E]", "Y#4#[GF]", "G#4#", "R#2#", "B#4#", "Y#2#"],
        ["R#3#", "R#5#", "R#2#[GC]", "R#3#", "R#4#[GF]", "R#3#[GF]"],
        ["B#3#[GC]", "B#6#", "B#1#", "B#5#[GF]", "B#6#", "B#6#"],
        ["Y#4#", "Y#5#", "Y#4#[GF]", "Y#1#", "Y#1#", "Y#6#"],
        ["G#6#", "G#1#", "G#5#[GF]", "G#2#", "G#4#", "G#2#"],
        'R'
    ) == 9


def test_from_problem_description_2():
    assert part_3(
        ["G#4#[F]", "R#2#", "B#4#", "[LG]Y#2#", "G#3#", "R#4#", "B#4#[T]", "Y#6#[E]", "G#1#", "R#1#", "B#5#", "Y#6#",
         "G#1#[GF]", "R#6#[GF][F]", "B#1#", "Y#2#", "[LR]G#4#", "R#3#", "B#2#", "Y#1#[T]", "G#3#[E]", "R#1#[GC]",
         "B#2#", "Y#3#", "G#3#", "R#6#", "B#2#[F]", "Y#6#", "G#6#", "[LB]R#6#", "B#4#", "Y#4#", "G#3#[T]", "R#4#[E]",
         "B#1#", "Y#1#", "G#2#", "R#6#", "B#6#", "Y#2#[F]", "G#6#", "R#5#", "[LY]B#1#", "Y#2#", "G#5#", "R#5#[T]",
         "B#3#[E]", "Y#3#", "G#1#", "R#5#", "B#2#", "Y#3#"],
        ["R#1#", "R#1#", "R#1#", "R#2#", "R#4#", "R#2#[GT]"],
        ["B#4#", "B#1#", "B#2#", "B#2#", "B#2#", "B#1#"],
        ["Y#3#[GF]", "Y#2#[GF]", "Y#6#[GC]", "Y#2#[GF]", "Y#5#", "Y#3#"],
        ["G#3#", "G#6#", "G#1#", "G#1#", "G#5#", "G#3#"],
        'Y'
    ) == 14
