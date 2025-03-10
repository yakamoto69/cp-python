#!/usr/bin/env python3
import sys
import heapq
from typing import List


# Undirected Graph用。隣接リスト形式で(node_id, edge_id)が入っている
# 自己ループに対応してる(自己ループの場合、エッジが２本できる)
def pack_undirected_graph(N: int, M: int, s: List[int], t: List[int]) -> "List[List[(int, int)]]":
    p = [0] * N
    for e in range(M):
        p[s[e]] += 1
        p[t[e]] += 1
    g = [[(-1, -1)] * p[i] for i in range(N)]
    for e in range(M):
        u = s[e]
        v = t[e]
        g[u][p[u] - 1] = (v, e)
        p[u] -= 1
        g[v][p[v] - 1] = (u, e)
        p[v] -= 1
    return g

# graph, undirected, dijkstra
# Generated by 2.14.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, M = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))
    U = [-1] * M
    V = [-1] * M
    for i in range(M):
        u, v = list(map(int, input().split(" ")))
        U[i] = u - 1
        V[i] = v - 1

    g = pack_undirected_graph(N, M, U, V)
    # print(f'g={g}', file=sys.stderr)

    D = [0] * N
    D[0] = 1
    heap = [(A[0], -1, 0)]  # (a, -d, u) a: asc, d: desc。-dにして同一aにの場合はdの逆順で処理したほうが(上書きはdが高い -> 低いの場合に発生するので)上書きが発生しにくい。最大Mしか上書きが発生しないので別に-dにしなくてもよかったかも
    while len(heap) > 0:
        a, d_neg, u = heapq.heappop(heap)
        d = -d_neg
        if D[u] > d:
            continue

        # print(f'a={a} d={d} u={u}', file=sys.stderr)
        for v, _ in g[u]:
            if A[u] < A[v] and D[u] + 1 > D[v]:
                D[v] = D[u] + 1
                heapq.heappush(heap, (A[v], -D[v], v))
            elif A[u] == A[v] and D[u] > D[v]:
                D[v] = D[u]
                heapq.heappush(heap, (A[v], -D[v], v))
    ans = D[N - 1]
    print(ans)


if __name__ == '__main__':
    main()
