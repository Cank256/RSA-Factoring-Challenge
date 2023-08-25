import sys

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None, None

def main(filename):
    try:
        with open(filename, 'r') as file:
            numbers = file.read().splitlines()
            for num in numbers:
                num = int(num)
                p, q = factorize(num)
                if p is not None and q is not None:
                    print(f"{num}={p}*{q}")
                else:
                    print(f"Unable to factorize {num}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
    else:
        filename = sys.argv[1]
        main(filename)
