#!/usr/bin/python3

import time
import sys
import argparse


def restore_path(i, j, prev):
    while prev[i][j]:
        i, j = prev[i][j]
    return i, j


def local_align(seq1, seq2):
    n1 = len(seq1) + 1
    n2 = len(seq2) + 1

    matrix = [[0] * n2 for _ in range(n1)]
    prev = [[None] * n2 for _ in range(n1)]

    max_value = 0
    max_pos = 0, 0

    for i in range(1, n1):
        for j in range(1, n2):
            matrix[i][j] = matrix[i - 1][j - 1] + (1 if seq1[i - 1] == seq2[j - 1] else -1)
            prev[i][j] = i - 1, j - 1

            if matrix[i - 1][j] - 1 > matrix[i][j]:
                matrix[i][j] = matrix[i - 1][j] - 1
                prev[i][j] = i - 1, j
            if matrix[i][j - 1] - 1 > matrix[i][j]:
                matrix[i][j] = matrix[i][j - 1] - 1
                prev[i][j] = i, j - 1
            if matrix[i][j] < 0:
                matrix[i][j] = 0
                prev[i][j] = None

            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_pos = i, j

    i1, j1 = max_pos
    i0, j0 = restore_path(i1, j1, prev)
    return i0, j0, i1, j1


complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}


def analyze_files(f1, f2, out):
    for line1, line2 in zip(f1, f2):
        seq1 = next(f1).strip()
        seq2 = next(f2).strip()
        next(f1)
        next(f2)
        qual1 = next(f1).strip()
        qual2 = next(f2).strip()

        seq2 = ''.join(complement[nt] for nt in seq2[::-1])
        qual2 = qual2[::-1]
        
        i0, j0, i1, j1 = local_align(seq1, seq2)
        out.write('%s%s%s\n+\n%s%s\n' % (line1, seq1[:i1], seq2[j1:], qual1[:i1], qual2[j1:]))


def main():
    with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2, open(sys.argv[3], 'w') as out:
        start = time.perf_counter()
        analyze_files(f1, f2, out)
        print(time.perf_counter() - start)


def main():
    parser = argparse.ArgumentParser(description='Glue reads together')
    parser.add_argument('-1', help='First input read', type=argparse.FileType('r'),
                        dest='input1', required=True, metavar='FILE')
    parser.add_argument('-2', help='Second input read', type=argparse.FileType('r'),
                        dest='input2', required=True, metavar='FILE')
    parser.add_argument('-o', '--output', help='Output glued read', type=argparse.FileType('w'),
                        required=True, metavar='FILE')
    parser.add_argument('-t', '--time', help='Print time', action='store_true')
    args = parser.parse_args()

    start = time.perf_counter()
    analyze_files(args.input1, args.input2, args.output)
    if args.time:
        sys.stderr.write('Time: %f\n`' % (time.perf_counter() - start))

if __name__ == '__main__':
    main()

