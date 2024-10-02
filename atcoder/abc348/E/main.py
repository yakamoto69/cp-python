#!/usr/bin/env python3
import sys


# Undirected Graph用。隣接リスト形式で(node_id, edge_id)が入っている
# 自己ループに対応してる(自己ループの場合、エッジが２本できる)
def pack_undirected_graph(N: int, M: int, s: list[int], t: list[int]) -> "list[list[(int, int)]]":
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


# 全方位木DP, tree_dp
def main():
    N = int(input())
    A = [-1] * (N - 1)
    B = [-1] * (N - 1)
    for i in range(N - 1):
        a, b = list(map(int, input().split(" ")))
        A[i] = a - 1
        B[i] = b - 1

    C = list(map(int, input().split(" ")))

    graph = pack_undirected_graph(N, N - 1, A, B)
    dist, par, queue = trace_bfs(graph)
    f = [0] * N
    g = [0] * N # fをsub-treeのみで計算したもの
    c_sum = [0] * N

    for i in range(N - 1, -1, -1):
        u = queue[i]

        c_sum[u] += C[u]
        for v, _ in graph[u]:
            if v == par[u]:
                continue

            c_sum[u] += c_sum[v]
            g[u] += g[v] + c_sum[v]

    f[0] = g[0]
    # print(f'g={g}', file=sys.stderr)
    # print(f'c_sum={c_sum}', file=sys.stderr)
    # print(f'f[0]={f[0]}', file=sys.stderr)

    for i in range(N):
        u = queue[i]
        for v, _ in graph[u]:
            if v == par[u]:
                continue
            c_sum_par = c_sum[0] - c_sum[v]  # uをsub-treeとしたときのc_sum = vのsub-tree以外の合計
            f[v] = f[u] + c_sum_par - c_sum[v]

    # print(f'f={f}', file=sys.stderr)
    ans = min(f)
    print(ans)


if __name__ == '__main__':
    main()
