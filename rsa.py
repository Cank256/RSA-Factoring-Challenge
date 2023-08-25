import sys
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)

    return d

def factorize_prime(n):
    factors = []
    while n > 1:
        factor = pollard_rho(n)
        factors.append(factor)
        n //= factor
    return factors

def main(filename):
    try:
        with open(filename, 'r') as file:
            num = int(file.readline())
            factors = factorize_prime(num)
            if len(factors) == 2:
                p, q = factors
                print(f"{num}={p}*{q}")
            else:
                print(f"Unable to factorize {num} within the time limit.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prime_factors.py <file>")
    else:
        filename = sys.argv[1]
        main(filename)
