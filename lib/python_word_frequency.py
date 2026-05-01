#!/usr/bin/python3

from collections import Counter
import string
import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print(f'Usage: {sys.argv[0]} <filename>')
        sys.exit(1)

    try:
#       frequency = {}
        frequency = Counter()
        with open(filename, 'r') as fd:
#           while True:
#               line = fd.readline()
#               if not line:
#                   break
            for line in fd:
                for word in line.split():
                    # normalize word (strip punctuation and make lowercase)
                    word = word.strip(string.punctuation).lower()
                    # exclude empty words (punctuation only)
                    if word:
#                       frequency[word] = frequency.get(word, 0) + 1
                        frequency[word] += 1
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

    print(dict(sorted(frequency.items())))

if __name__ == '__main__':
    main()
