### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part1.part_1 import part_1


def test_from_problem_description():
    assert part_1(start=9, end=15) == ['Fizz', 'Buzz', '11', 'Fizz', '13', 'Bees', 'FizzBuzz']
    assert part_1(start=100, end=110) == ['Buzz', '101', 'Fizz', '103', '104', 'FizzBuzzBees', '106', '107', 'Fizz', '109', 'Buzz']
    assert part_1(start=20, end=42) == ['Buzz', 'FizzBees', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', 'Bees', '29', 'FizzBuzz', '31', '32', 'Fizz', '34', 'BuzzBees', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'FizzBees']

def test_supplementaire():
    assert part_1(start=1, end=10) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Bees', '8', 'Fizz', 'Buzz']
