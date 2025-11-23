### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part1.part_1 import part_1


def test_from_problem_description():
    assert part_1(3) == [
        "|_._._._._._|",
        "|_._._._._._|",
        "|_._._._._._|",
        "|_._._._._._|",
        " \\_._._._._/ ",
        "  \\_._._._/  ",
        "   \\_._._/   ",
    ]
    assert part_1(2) == [
        "|_._._._|",
        "|_._._._|",
        "|_._._._|",
        " \\_._._/ ",
        "  \\_._/  ",
    ]


def test_supplementaire():
    assert part_1(7) == [
        "|_._._._._._._._._._._._._._|",
        "|_._._._._._._._._._._._._._|",
        "|_._._._._._._._._._._._._._|",
        "|_._._._._._._._._._._._._._|",
        "|_._._._._._._._._._._._._._|",
        "|_._._._._._._._._._._._._._|",
        "|_._._._._._._._._._._._._._|",
        "|_._._._._._._._._._._._._._|",
        " \\_._._._._._._._._._._._._/ ",
        "  \\_._._._._._._._._._._._/  ",
        "   \\_._._._._._._._._._._/   ",
        "    \\_._._._._._._._._._/    ",
        "     \\_._._._._._._._._/     ",
        "      \\_._._._._._._._/      ",
        "       \\_._._._._._._/       ",
    ]
