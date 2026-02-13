# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 4.
Ceci est le fichier template pour la partie 2 du Prelim 4.
"""

def generate_all_numbers():
    gen_list = []
    for i in range(10):
        gen_list.append(str(i))
    return gen_list

def get_operation(equation: str):
    operators = ["+","-","x","÷","×"]
    all_numbers = generate_all_numbers()
    operation = list(equation)
    small_list = []
    all_list = []
    operator = []
    numbers = []
    if(operation[0] == "-"):
        operation.insert(0,"0")

    for x in operation:
        print(small_list)
        if(x in operators):
            all_list.append(small_list)
            small_list = []
            operator.append(x)
        elif (x not in operators and x not in all_numbers):
            print("Écris bien ton affaire !")
            return -1
        else:
             small_list.append(x)
       

    all_list.append(small_list)

    print(all_list)
    #print(operator)

    for small in all_list:
        number = int(''.join(small))
        numbers.append(number)
    
    #print(numbers)
    solution = 0
    counter = 1
    member = [numbers[0],numbers[1]]

    for i in operator:
        #sorry I have the old version of python (I'm too lazyn to change it) so I don't have access to match
        if i == "+": 
            solution = member[0] + member[1]
        elif i == "-":
            solution = member[0] - member[1]
        elif i == "x" or i == "×":
            solution = member[0] * member[1]
        elif i == "÷":
            solution = member[0] / member[1]
        
        #print(member)
        counter += 1
        if(counter >= len(numbers)):
            pass
        else:
            member = [solution,numbers[counter]]

    #print(solution)
    return solution

def check_palindrome(solution):
    test = list(str(solution))
    another_test = []
    value = ""

    #(test)

    for i in reversed(test):
        another_test.append(i)
    print(another_test)

    if(another_test == test):
        value = "Yes"
    else:
        value = "No"

    return value

def part_2(equation: str):
    """
    Verify if the solution to the equation is a palindrome

    Parameters:
        equation str: The equation to solve

    Returns:
        str: Yes if the answer of the equation is a palindrome, No otherwise
    """
    is_palindrome = "Yes"
    ### You code goes here ###
    ### Votre code va ici ###

    solution = get_operation(equation)

    if(solution == -1):
        is_palindrome = "IDK"
    else:
       is_palindrome = check_palindrome(int(solution))

    print(is_palindrome)

    return is_palindrome


part_2("254168116÷4-62999784")
