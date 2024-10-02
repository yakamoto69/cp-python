#!/usr/bin/env python3
import sys
from collections import deque


# graph, dijkstra, deque
def main():
    N = int(input())
    grid = [input() for _ in range(N)]
    inf = 1e9
    s = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'P':
                s.append((i, j))
                
    queue = deque()
    idx0, idx1 = s[0][0] * N + s[0][1], s[1][0] * N + s[1][1]
    queue.append((idx0, idx1))
    
    D = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]

    dist = [[inf] * (N * N)  for _ in range(N * N)]
    dist[s[0][0]* N + s[0][1]][s[1][0] * N + s[1][1]] = 0

    ans = inf
    while queue:
        idx0, idx1 = queue.popleft()
        i0, j0 = idx0 // N, idx0 % N
        i1, j1 = idx1 // N, idx1 % N
        # print(f'i0={i0} j0={j0}', file=sys.stderr)
        for di, dj in D:
            ni0 = i0 + di 
            nj0 = j0 + dj
            if not (0 <= ni0 < N and 0 <= nj0 < N and grid[ni0][nj0] != '#'):
                ni0 = i0
                nj0 = j0

            ni1 = i1 + di
            nj1 = j1 + dj
            if not (0 <= ni1 < N and 0 <= nj1 < N and grid[ni1][nj1] != '#'):
                ni1 = i1
                nj1 = j1

            if (ni0, nj0) == (ni1, nj1):
                ans = min(ans, dist[idx0][idx1] + 1)
            else:
                nidx0, nidx1 = ni0 * N + nj0, ni1 * N + nj1
                if dist[nidx0][nidx1] > dist[idx0][idx1] + 1:
                    queue.append((nidx0, nidx1))
                    dist[nidx0][nidx1] = dist[idx0][idx1] + 1

    print(-1 if ans == inf else ans)
    

if __name__ == '__main__':
    main()
