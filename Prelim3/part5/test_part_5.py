### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part5.part_5 import part_5


def test_from_problem_description():
    assert part_5(pain=4, geography="europe", family="halictidae", nest="ground") == ['epinephrine']
    assert part_5(pain=2, geography="asia", family="apidae", nest="hole") == ['epinephrine', 'ice']
    assert part_5(pain=8, geography="africa", family="apidae", nest="ground") == ['antihistamine', 'antiseptic cream']


def test_supplementaire():
   assert part_5(pain=5, geography="europe", family="megachilidae", nest="tree") == ['antihistamine', 'antiseptic cream']
