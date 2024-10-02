import sys
from typing import List

input = lambda: sys.stdin.buffer.readline().decode('utf-8').rstrip('\r\n')


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


def main():
    N, Q = map(int, input().split())
    queries = [[-1, -1, -1] for _ in range(Q)]
    bits = [[-1] * 30 for _ in range(N)]
    for q in range(Q):
        i, j, x = map(int, input().split())
        i -= 1
        j -= 1
        queries[q][0] = i
        queries[q][1] = j
        queries[q][2] = x
        # queries.append((i, j, x))

    s = [-1] * Q
    t = [-1] * Q
    for q in range(Q):
        i, j, x = queries[q]
        if i > j:
            i, j = j, i
        s[q] = i
        t[q] = j
        for k in range(30):
            if x >> k & 1 == 0:  # 0の場合はどちらも0で決まり
                bits[i][k] = 0
                bits[j][k] = 0

    g = pack_directed_graph(N, len(s), s, t)

    for k in range(30):
        for u in range(N):
            set_one = False
            if bits[u][k] == 1:
                continue

            for v, e in g[u]:
                if queries[e][2] >> k & 1 == 1 and bits[v][k] == 0:  # どこかの相手に0がいたらuを1にするしかない
                    set_one = True
                    break

            if set_one:
                bits[u][k] = 1
            else:
                # uが0|1どちらでもいいとなったら0にして、相手側を1にする
                bits[u][k] = 0
                for v, e in g[u]:
                    if queries[e][2] >> k & 1 == 1:
                        bits[v][k] = 1

    for i in range(N):
        ans = 0
        for k in range(30):
            if bits[i][k] == 1:
                ans |= 1 << k
        print(ans, end=" ")


if __name__ == '__main__':
    main()