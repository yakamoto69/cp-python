import sys
input = sys.stdin.readline


def main():
    T = int(input())
    for test_num in range(T):
        N = int(input())
        S0 = input().rstrip()
        S = [0] * (N + 1)
        cnt = 0
        for i in range(N):
            if S0[i] == '1':
                S[i + 1] = 1
                cnt += 1
        Q = int(input())
        B = [0] * (N + 1)

        def apply(x):
            nonlocal cnt
            for i in range(x, N + 1, x):
                cnt -= S[i]
                S[i] ^= 1
                cnt += S[i]

        #  init A1
        for i in range(Q):
            x = int(input())
            B[x] ^= 1

        # print(f'S: {S} A1: {A1} cnt: {cnt}', file=sys.stderr)

        #  apply A1
        for i in range(1, N + 1):
            if B[i] == 1:
                apply(i)

        ans = 0
        for i in range(1, N + 1):
            if S[i] == 1:
                apply(i)
                ans += 1

        print(f'Case #{test_num + 1}: {ans}')


if __name__ == '__main__':
    main()