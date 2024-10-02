import sys
from typing import List

input = sys.stdin.readline


def main():
    T = int(input())
    for t in range(1, T + 1):
        mapping = list(map(int, input().split()))
        N = int(input())
        words: List[str] = [input().strip() for _ in range(N)]
        encoded = set()
        for word in words:
            for c in word:
                print(c, ord(c) - ord('A'), file=sys.stderr)
            words.append(''.join(str([mapping[ord(c) - ord('A')] for c in word])))

        ans = "YES" if len(encoded) < N else "NO"
        print(f'Case #{t}: {ans}', end='')
    return

if __name__ == '__main__':
    main()