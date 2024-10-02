import sys

input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = 0
        for i in range(N - 1):
            if A[i] == 0:
                continue

            if i < N - 1:
                A[i + 1] ^= A[i]
                A[i] = 0
                ans += 1
            else:
                A[i] = 0
                ans += 1
        print(ans)


if __name__ == '__main__':
    main()