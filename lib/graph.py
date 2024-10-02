from typing import List
from collections import deque

# cycleがある時はNoneを返す
def topological_sort(g: List[List[int]]) -> List[int]:
    n = len(g)
    indeg = [0] * n
    for u in range(n):
        for v in g[u]:
            indeg[v] += 1
    que = [u for u in range(n) if indeg[u] == 0]

    res = []
    while que:
        u = que.pop()
        res.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                que.append(v)
    return res if len(res) == n else None


# Directed Graph用。隣接リスト形式で(node_id, edge_id)が入っている
def pack_directed_graph(N: int, M: int, s: List[int], t: List[int]) -> "List[List[(int, int)]]":
    p = [0] * N
    for e in range(M):
        p[s[e]] += 1
    g = [[(-1, -1)] * p[i] for i in range(N)]
    for e in range(M):
        u = s[e]
        v = t[e]
        p[u] -= 1
        g[u][p[u]] = (v, e)
    return g


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


# 重さ１固定のグラフなのでdequeを使っている
# @param g: 隣接リスト形式で(node_id, edge_id)が入っている
# @return D: sからの最短距離
# @return route: 最短距離でnodeに到達した時の、(dist, edge_id)
def dijkstra(N: int, M: int, g: "List[List[(int, int)]]", s: int) -> (List[int], List[(int, int)]):
    inf = int(1e9)
    que = deque()
    que.append(s)
    D = [inf] * N
    D[s] = 0
    route = [(N, M)] * N  # (node, edge)
    while len(que):
        u = que.popleft()
        for v, e in g[u]:
            if D[v] > D[u] + 1:
                D[v] = D[u] + 1
                route[v] = (u, e)
                que.append(v)
    return D, route


# P: 遷移先。木のルートは自己ループになっていると嬉しい
#   TODO ルート=-1 に対応できるように拡張したほうが使い勝手が良い
# K: 2^Kまで計算する
def direct_graph_doubling(N: int, P: [int], pow: int) -> [[int]]:
    table = [[-1] * N for _ in range(pow)]
    for i in range(N):
        table[0][i] = P[i]

    for i in range(1, pow):
        for v in range(N):
            # -1だったら行き止まりを表現の場合は対応できていない
            table[i][v] = table[i - 1][table[i - 1][v]]

    return table


# table, direct_graph_doublingの結果
# K: direct_graph_doublingで渡した値
def move(v: int, times: int, table: [[int]], pow: int) -> int:
    for i in range(pow):
        if times >> i & 1 == 1:
            v = table[i][v]
    return v
