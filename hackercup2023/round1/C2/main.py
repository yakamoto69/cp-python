import sys
input = sys.stdin.readline


def main():
    T = int(input())
    for test_num in range(T):
        N = int(input())
        S0 = input().rstrip()
        S = [0] * (N + 1)
        # init S
        for i in range(N):
            if S0[i] == '1':
                S[i + 1] = 1

        # init A1
        B = [0] * (N + 1)
        cnt = 0  # number of 1 in A1
        for x in range(1, N + 1):
            if S[x] == 1:
                for i in range(x, N + 1, x):
                    S[i] ^= 1
                B[x] = 1
                cnt += 1
        # print(f'A1: {A1} cnt: {cnt}', file=sys.stderr)

        ans = 0
        Q = int(input())
        for i in range(Q):
            b = int(input())
            if B[b] == 1:
                B[b] = 0
                cnt -= 1
                ans += cnt
            else:
                B[b] = 1
                cnt += 1
                ans += cnt

        print(f'Case #{test_num + 1}: {ans}')


if __name__ == '__main__':
    main()