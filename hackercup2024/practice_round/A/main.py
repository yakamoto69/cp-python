import sys
input = sys.stdin.readline


def main():
    T =  int(input())
    for t in range(T):
        def can_within_K():
            N, K = list(map(int, input().split()))
            S = [int(input()) for _ in range(N)]
            S.sort()
            times = max(1, 2 * N  - 3)
            return times * S[0] <= K

        ans = 'YES' if can_within_K() else 'NO'
        print(f"Case #{t + 1}: {ans}")


if __name__ == '__main__':
    main()