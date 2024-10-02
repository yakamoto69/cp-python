import sys
input = sys.stdin.readline


def main():
    T =  int(input())
    for t in range(T):
        R, C, A, B = list(map(int, input().split()))
        ans = "YES" if R > C else "NO"
        print("Case #{}: {}".format(t+1, ans))


if __name__ == '__main__':
    main()