#!/usr/bin/python3

import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print(f'Usage: {sys.argv[0]} <filename>')
        sys.exit(1)

    try:
        frequency = {}
        with open(filename, 'r') as fd:
#           while True:
#               line = fd.readline()
#               if not line:
#                   break
            for line in fd:
                for word in line.split():
                    if word in frequency:
                        frequency[word] += 1
                    else:
                        frequency[word] = 1
    except Exception as e:
        print(f'Error: {e}')

    print(dict(sorted(frequency.items())))

if __name__ == '__main__':
    main()
