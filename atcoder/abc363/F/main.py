#!/usr/bin/env python3
import sys
from collections import deque


def find_divisers(x: int) -> [int]:
    divisers = []
    post = []
    d = 1
    while d * d <= x:
        if x % d == 0:
            divisers.append(d)
            if d * d != x:
                post.append(x // d)
        d += 1

    for i in range(len(post) - 1, -1, -1):
        divisers.append(post[i])
    return divisers


# divisor
def main():
    N = int(input())
    divisors = set(find_divisers(N))

    valid_divisors = [] # (divisor, left number, right number)
    for i in range(1, int(1e6) + 1):
        s = str(i)
        if '0' in s:
            continue
        j = int(s[::-1])
        d = j * i
        if d in divisors:
            valid_divisors.append((d, i, j))

    print(f'valid_divisors={valid_divisors}', file=sys.stderr)

    visited = {N: (-1, -1, -1)}
    queue = deque([N])
    while queue:
        x = queue.popleft()
        for d, i, j in valid_divisors:
            if x % d == 0 and x // d not in visited:
                nx = x // d
                visited[nx] = (x, i, j)
                queue.append(nx)

    print(f'visited={visited}', file=sys.stderr)

    def is_valid_palindrome(x):
        s = str(x)
        n = len(s)
        if '0' in s:
            return False

        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True

    def print_answer(x):
        answer = str(x)
        while visited[x][0] != -1:
            y, i, j = visited[x]
            answer = f"{i}*{answer}*{j}"
            x = y
        print(answer)

    for x in visited.keys():
        if is_valid_palindrome(x):
            print_answer(x)
            return

    print(-1)


if __name__ == '__main__':
    main()
