from .part_1 import part_1, print_tail

def main():
    sizes = list(map(int, input("Enter the size of every platypus' tail (separated by a space): ").split()))
    
    for size in sizes:
        print_tail(part_1(size))

if __name__ == "__main__":
    main()