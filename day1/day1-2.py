
import re
import sys

fstpat = re.compile(r'(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine|zero)')
lastpat = re.compile(r'.*(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine|zero)')

lut = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
     'one': '1',
     'two': '2',
     'three': '3',
     'four': '4',
     'five': '5',
     'six': '6',
     'seven': '7',
     'eight': '8',
     'nine': '9',
     'zero': '0'}


def parserow(s):
    fst = fstpat.search(s).groups()[0]
    snd = lastpat.search(s).groups()[0]
    return int(lut[fst] + lut[snd])


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            n = sum(map(parserow, lines))
            print(n)


if __name__ == '__main__':
    main()

