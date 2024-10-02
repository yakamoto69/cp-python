import sys
from typing import List
from atcoder.segtree import SegTree
input = sys.stdin.readline


def manacher(S):
    C = []
    for a in S:
        C.append(a)
        C.append(0)
    C.pop()

    L = len(C)

    R = [0]*L

    i = j = 0
    while i < L:
        while j <= i < L-j and C[i-j] == C[i+j]:
            j += 1
        R[i] = j
        k = 1
        while j-R[i-k] > k <= i < L-k:
            R[i+k] = R[i-k]
            k += 1
        i += k; j -= k

    # for i in range(L):
    #     if i & 1 == R[i] & 1:
    #         R[i] -= 1
    return R



def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        S = A + B + A + B
        P = manacher(S)
        is_small = [S[i] < S[i + N] for i in range(3 * N)]
        is_small_tree = SegTree(lambda x, y: x and y, True, is_small)
        is_large = [S[i] > S[i + N] for i in range(3 * N)]
        is_large_tree = SegTree(lambda x, y: x and y, True, is_large)

        # print(P, file=sys.stderr)
        # print(is_small, file=sys.stderr)
        # print(is_large, file=sys.stderr)

        ans = -1
        for jj in range(len(P)):  # -1の位置
            if ans != -1:
                continue

            if jj % 2 == 0:
                continue

            if P[jj] >= N * 2:
                s_pos = jj - 2*N + 1  # P上の位置
                i = s_pos // 2  # -1を取り除いた本来の位置
                # print(f't:{t} jj: {jj}, i: {i}', file=sys.stderr)
                if is_small_tree.prod(i, i + N // 2) and is_large_tree.prod(i + N - N // 2, i + N):
                    ans = i

        print(f'Case #{t + 1}: {ans}')


if __name__ == '__main__':
    main()