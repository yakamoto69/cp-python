#!/usr/bin/env python3
import sys


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


# function_graph, doubling
def main():
    N, K = list(map(int, input().split(" ")))
    X = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))
    for i in range(N):
        X[i] -= 1

    table = direct_graph_doubling(N, X, 60)
    I = [move(v, K, table, 60) for v in range(N)]
    ans = [A[I[i]] for i in range(N)]
    print(*ans, sep=' ')


if __name__ == '__main__':
    main()
