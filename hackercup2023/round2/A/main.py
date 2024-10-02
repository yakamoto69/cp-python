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

        ok = False

        for r in range(R):
            for c in range(C):
                if board[r][c] != '.':
                    continue
                board[r][c] = "A1"

                dsu = DSU(R * C)
                has_empty = [False] * (R * C)
                for i in range(R):
                    for j in range(C):
                        if board[i][j] != 'W':
                            continue
                        for di in range(-1, 2):
                            for dj in range(-1, 2):
                                if di == 0 and dj == 0:
                                    continue
                                ni = i + di
                                nj = j + dj
                                if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == "W":
                                    dsu.merge(i * C + j, ni * C + nj)

                for i in range(R):
                    for j in range(C):
                        if board[i][j] != 'W':
                            continue

                        for d in D:
                            ni = i + d[0]
                            nj = j + d[1]
                            if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == ".":
                                has_empty[dsu.leader(i * C + j)] = True

                # print(f'has_empty: {has_empty}', file=sys.stderr)

                for i in range(R):
                    for j in range(C):
                        if board[i][j] != 'W':
                            continue
                        v = i * C + j
                        if dsu.leader(v) == v and not has_empty[v]:
                            ok = True

                board[r][c] = "."

        ans = "YES" if ok else "NO"
        print(f'Case #{test_num + 1}: {ans}')


if __name__ == '__main__':
    main()