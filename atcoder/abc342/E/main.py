#!/usr/bin/env python3

import heapq
import sys


# priority_queue, heapq, dijkstra, directed_graph
def main():
    N, M = list(map(int, input().split(" ")))
    trains = [list(map(int, input().split(" "))) for _ in range(M)]
    for i in range(M):
        trains[i][4] -= 1
        trains[i][5] -= 1

    I: list[list[int]] = [[] for _ in range(N)]  # toでindexする
    for i in range(M):
        I[trains[i][5]].append(i)

    dp = [0] * N
    dp[N - 1] = int(4e18)

    heap = []
    heapq.heappush(heap, (dp[N - 1] * -1, N - 1))

    while heap:
        negative_cost, v = heapq.heappop(heap)
        # dijkstraのいつもの上書きされたケースの除外
        if dp[v] != negative_cost * -1:
            continue

        # print(f'visit v={v}', file=sys.stderr)
        for e in I[v]:
            # print(f'visit e={e}', file=sys.stderr)
            l, d, k, c, u, _ = trains[e]
            # l + dx0 <= dp - c
            # x0 <= (dp - c- l) // d を満たす最大のx0
            x0 = (dp[v] - c - l) // d
            x = min(k - 1, x0)  # 中で 0 <= x < k の条件を満たす最大のx
            best = l + d * x
            if dp[u] < best:
                dp[u] = best
                heapq.heappush(heap, (dp[u] * -1, u))

    for i in range(N - 1):
        if dp[i] == 0:
            print("Unreachable")
        else:
            print(dp[i])

if __name__ == '__main__':
    main()
