import math


def main():
    run_time = int(input())
    for x in range(run_time):
        print(is_prime(int(input())))


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n % i) == 0:
            return "Prime"
    return "Not Prime"


main()