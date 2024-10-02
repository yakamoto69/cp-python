import sys
from atcoder.dsu import DSU
input = sys.stdin.readline


def main():
    T = int(input())
    for test_num in range(T):
        R, C = list(map(int, input().split()))
        board = [[]] * R
        for i in range(R):
            board[i] = [c for c in input()]
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        dsu = DSU(R * C)
        emptied = [-1] * (R * C)
        count = [0] * (R * C)
        for i in range(R):
            for j in range(C):
                if board[i][j] != 'W':
                    continue
                for d in D:
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == "W":
                        dsu.merge(i * C + j, ni * C + nj)

        for i in range(R):
            for j in range(C):
                if board[i][j] != 'W':
                    continue

                g = dsu.leader(i * C + j)
                count[g] += 1

                for d in D:
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == ".":
                        if emptied[g] == -1 or emptied[g] == ni * C + nj:
                            emptied[g] = ni * C + nj
                        else:
                            emptied[g] = -2  # ２種類以上の空白マスがある

        wins = [0] * (R * C)
        for i in range(R):
            for j in range(C):
                if board[i][j] != 'W':
                    continue
                v = i * C + j
                g = dsu.leader(v)
                if g == v and emptied[g] >= 0:
                    wins[emptied[g]] += count[g]

        # print(f'emptied: {emptied}', file=sys.stderr)
        # print(f'count: {count}', file=sys.stderr)
        # print(f'wins: {wins}', file=sys.stderr)

        ans = max(wins)
        print(f'Case #{test_num + 1}: {ans}')


if __name__ == '__main__':
    main()