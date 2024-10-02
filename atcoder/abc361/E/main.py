#!/usr/bin/env python3
import sys
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


# (dist, parent, queue)
# root nodeのparent = -1
# @param rt ルートノードを指定する。-1の場合は全ノード辿るまで繰り返す
def trace_bfs(g: list[list[(int, int)]], rt = 0):
    n = len(g)
    q = [-1] * n
    d = [-1] * n
    p = [-2] * n
    h = 0
    t = 0

    def bfs(rt):
        nonlocal h, t
        p[rt] = -1
        q[t] = rt
        t += 1
        d[rt] = 0
        while h < t:
            u = q[h]
            h += 1
            for v, _ in g[u]:
                if p[v] == -2:
                    p[v] = u
                    q[t] = v
                    t += 1
                    d[v] = d[u] + 1

    if rt != -1:
        bfs(rt)
    else:
        for v in range(n):
            if p[v] == -2:
                bfs(v)
    return d, p, q


# 全方位木DP
def main():
    N = int(input())
    A = [-1] * (N - 1)
    B = [-1] * (N - 1)
    C = [-1] * (N - 1)
    for i in range(N - 1):
        a, b, c = list(map(int, input().split(" ")))
        A[i] = a - 1
        B[i] = b - 1
        C[i] = c
    g = pack_undirected_graph(N, N - 1, A, B)
    dist, parent, queue = trace_bfs(g)

    dp = [0] * N

    for i in range(N - 1, -1, -1):
        u = queue[i]
        max_child = 0
        for v, e in g[u]:
            if v == parent[u]:
                continue
            max_child = max(max_child, C[e] + dp[v])

        dp[u] = max_child

    print(f'dp={dp}', file=sys.stderr)

    cut = 0
    dp2 = [0] * N
    for i in range(N):
        u = queue[i]
        children = []
        children.append((dp2[u], parent[u]))
        for v, e in g[u]:
            if v == parent[u]:
                continue
            children.append((dp[v] + C[e], v))

        children.sort(reverse=True)
        if len(children) == 0:
            best = 0
        if len(children) == 1:
            best = children[0][0]
        else:
            best = children[0][0] + children[1][0]
        cut = max(cut, best)

        for v, e in g[u]:
            if v == parent[u]:
                continue

            if children[0][1] != v:
                dp2[v] = children[0][0] + C[e]
            elif len(children) > 1:
                dp2[v] = children[1][0] + C[e]
            else:
                dp2[v] = C[e]

    ans = sum(C) * 2 - cut
    print(ans)


if __name__ == '__main__':
    main()
