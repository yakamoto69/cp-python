#!/usr/bin/env python3
import sys
from collections import deque


# dijkstra, deque
def main():
    N = int(input())

    def to_code(s: str):
        code = 0
        for i in range(len(s)):
            c = s[i]
            bit = 1 if c == 'W' else 2
            code = (code << 2) + bit
        return code << 4

    S = to_code(input())
    T = to_code(input())
    dist = {}
    dist[S] = 0
    que = deque()
    que.append((S, 0))

    def move(v, blank, i):
        mask = (1 << (2 * (N + 2))) - 1 - (15 << (i * 2))
        res = (v & mask) | (v >> (2 * i) & 15) << (2 * blank)
        return res

    inf = int(1e9 + 100)
    ans = inf
    while que:
        v, blank = que.popleft()

        if v == T:
            ans = min(ans, dist[v])

        for i in range(N + 1):
            if blank - 1 <= i <= blank + 1:
                continue

            nv = move(v, blank, i)

            if nv not in dist:
                dist[nv] = dist[v] + 1
                que.append((nv, i))

    if ans == inf:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()
