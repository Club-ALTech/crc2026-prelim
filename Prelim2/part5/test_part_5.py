### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part5.part_5 import part_5


def test_from_problem_description():
    assert part_5(grid = [
    ['o', 'n', 'v', 'i'],
    ['a', 'l', 'p', 'w'],
    ['m', 'i', 'k', 's'],
    ['i', 'r', 's', 'r']],
    word = "skips"
    ) == [14, 10, 9, 6, 11]

    assert part_5(grid = [
    ['n', 'n', 'm', 'p'],
    ['o', 's', 'a', 't'],
    ['l', 'b', 'a', 'u'],
    ['i', 'z', 'f', 'n']],
    word = "sablonnat"
    ) == [5, 10, 9, 8, 4, 0, 1, 6, 7]

    assert part_5(grid = [
    ['s', 'a', 'a', 'u'],
    ['i', 'o', 't', 'e'],
    ['w', 'n', 'e', 'e'],
    ['p', 'f', 'e', 'u']],
    word = "notais"
    ) == [9, 5, 6, 1, 4, 0]
        
    

def test_supplementaire():
    assert part_5( grid = [
    ['o', 'n', 'v', 'i'],
    ['a', 'l', 'p', 'w'],
    ['m', 'i', 'k', 's'],
    ['i', 'r', 's', 'r']],
    word = "ikrsw"
    ) == [9, 10, 15, 11, 7]