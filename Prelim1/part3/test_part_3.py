### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part3.part_3 import part_3


def test_from_problem_description():
    assert part_3("Platypus is the best animal in the world.") == [36, 37, 22, 9, 3, 13, -1, -1, 4, 29, -1, 6, 14]

    assert part_3("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur hendrerit nulla suscipit quy rhoncus luctus. Curabitur in ex est. Aenean non sollicitudin nulla") == [1, 2, 30, 6, 20, 67, 13, 16, 94, 48, 92, 9, 3]
    
    assert part_3("What exactly is that thing called an ornithorynque in french??") == [37, 38, 24, 13, 3, 1, 43, 44, 11, 35, 47, 48, 5]

def test_supplementaire():
    assert part_3("When Mr. Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton") == [13, 6, 3, 10, 44, 1, 23, 61, 64, 20, -1, 38, 2]
