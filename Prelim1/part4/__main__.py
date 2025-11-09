# Ceci n'est pas un fichier à remettre, il sert uniquement à visualiser le résultat sur le terminal (et débugger par conséquent)

from .part_4 import part_4
import re

def main():
    positions = [tuple(map(int, coordinate)) for coordinate in re.findall(r'([-]?\d+),\s([-]?\d+),\s([-]?\d+)', input("Enter the serie of coordinates in 3D from the pool in this form: (n1, n2, n3), (m1, m2, m3), ... : "))]
    part_4(positions)

if __name__ == "__main__":
    main()


# Pour tester
""" 
(0, 0, 0), (5, 6, 4), (9, 9, 2), (6, 2, 3), (3, 8, 4)
(0, 0, 0), (4, 13, 6), (2, 6, 4), (3, 1, 7), (7, 5, 10)
(16, 17, 5), (4, 4, 9), (11, 16, 14), (8, 4, 9), (11, 18, 8), (17, 2, 15), (10, 18, 7)
(-1, -1, -1), (1, 2, 3), (4, 5, 6)
"""