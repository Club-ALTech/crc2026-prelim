# Ceci n'est pas un fichier à remettre, il sert uniquement à visualiser le résultat sur le terminal (et débugger par conséquent)

from .part_2 import part_2

def main():
    data = list(
        map(
            int, 
            input("Enter the width, the height, the length, and the age of the platypus respectively (separated by a space): ").split()
        )
    )
    part_2(*data)

if __name__ == "__main__":
    main()


# Pour tester
""" 
10 14 50 4
13 10 47 3
16 17 63 7
9 12 40 8
"""