import sys
input = sys.stdin.readline


def main():
    T = int(input())
    for test_num in range(T):
        N = int(input())
        X = list(map(int, input().split()))
        X.sort()
        ans = 0
        if N >= 6 or N == 4:
            s = (X[0] + X[1]) / 2
            t = (X[-1] + X[-2]) / 2
            ans = max(ans, t - s)
        else:
            s = (X[0] + X[2]) / 2
            t = (X[-1] + X[-2]) / 2
            ans = max(ans, t - s)

            s2 = (X[0] + X[1]) / 2
            t2 = (X[-1] + X[-3]) / 2
            ans = max(ans, t2 - s2)

        print('Case #{}: {:.1f}'.format(test_num + 1, ans))



if __name__ == '__main__':
    main()