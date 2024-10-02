import sys
input = sys.stdin.readline


def main():
    T =  int(input())
    for t in range(T):
        S, D, K = list(map(int, input().split()))
        buns = (S + D) * 2
        patties = S + 2 * D  # チーズとパティーはneedも実際の数も一緒になる
        needed_buns = K + 1
        needed_patties = K
        ans = "YES" if buns >= needed_buns and patties >= needed_patties else "NO"
        print(f"Case #{t + 1}: {ans}")


if __name__ == '__main__':
    main()