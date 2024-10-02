import sys

input = sys.stdin.readline


def main():
    T = int(input())
    for t in range(T):
        solve()


def solve():
    M = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]
    inc = [[-1] * M for _ in range(2)]  # increasing
    dec = [[-1] * M for _ in range(2)]  # decreasing
    for i in range(2):
        inc[i][M - 1] = M - 1
        dec[i][M - 1] = M - 1
        for j in range(M - 2, -1, -1):
            j_go = inc[i][j + 1]
            j_back = dec[i][j + 1]
            inc[i][j] = j if A[i][j] + j > A[i][j_go] + j_go else j_go
            dec[i][j] = j if A[i][j] - j > A[i][j_back] - j_back else j_back

    print(f'{A}\ninc:{inc}\ndec:{dec}', file=sys.stderr)

    ans = 1e18
    best = 0  # j-1まで四角形に全部埋めてj-1の場所にいるときの最短。i=0のときはうまくいかないうまくいかない
    for j in range(M):
        if j == 0:
            j_go = dec[0][1]
            j_back = inc[1][0]
            w1 = max(0, A[0][j_go] + 1 - j_go)
            t1 = w1 + M - 1  # 一番右
            w2 = max(0, A[1][j_back] + 1 - (M - j_back) - t1)
            t2 = t1 + w2 + M  # 戻ってきた
            ans = min(ans, t2)
            best = max(best, A[1][0]) + 1
        elif j % 2 == 0:
            j_go = dec[0][j]
            j_back = inc[1][j]
            w1 = max(0, A[0][j_go] + 1 - (j_go - (j - 1)) - best)
            t1 = best + w1 + (M - 1 - (j - 1))  # 一番右
            w2 = max(0, A[1][j_back] + 1 - ((M - 1) - j_back + 1) - t1)
            t2 = t1 + w2 + ((M - 1) - j + 1)  # 戻ってきた
            ans = min(ans, t2)
            best = max(max(best, A[0][j]) + 1, A[1][j]) + 1
        else:
            j_go = dec[1][j]
            j_back = inc[0][j]
            w1 = max(0, A[1][j_go] + 1 - (j_go - (j - 1)) - best)
            t1 = best + w1 + (M - 1 - (j - 1))  # 一番右
            w2 = max(0, A[0][j_back] + 1 - ((M - 1) - j_back + 1) - t1)
            t2 = t1 + w2 + ((M - 1) - j + 1)  # 戻ってきた
            ans = min(ans, t2)
            best = max(max(best, A[1][j]) + 1, A[0][j]) + 1

        # print(f'j={j}, w1={w1}, w2={w2}, t1={t1}, t2={t2}, best={best}, ans={ans}', file=sys.stderr)
    print(ans)

if __name__ == '__main__':
    main()