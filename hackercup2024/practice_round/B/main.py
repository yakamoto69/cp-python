import sys
input = sys.stdin.readline


def main():
    T =  int(input())
    for t in range(T):
        N, P = list(map(int, input().split()))
        p_dash = pow(P / 100, (N - 1) / N)
        # print(f'p_dash={p_dash}', file=sys.stderr)
        ans = p_dash * 100 - P
        print(f'Case #{t+1}: {ans:.15f}')


if __name__ == '__main__':
    main()
