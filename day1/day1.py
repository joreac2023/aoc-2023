
import sys


def isdigit(c):
    return c >= '0' and c <= '9'


def parserow(s):
    numbers = [d for d in s if isdigit(d)]
    return int(numbers[0] + numbers[-1])


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            n = sum(map(parserow, lines))
            print(n)


if __name__ == '__main__':
    main()

