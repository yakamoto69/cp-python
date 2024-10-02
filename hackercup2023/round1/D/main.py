import sys
from atcoder.lazysegtree import LazySegTree
input = sys.stdin.readline


def main():
    T = int(input())

    def op(x, y):
        if x is None:
            return y
        if y is None:
            return x

        if x[0][0] < y[0][0]:
            l = x[0]
        elif x[0][0] > y[0][0]:
            l = y[0]
        elif x[0][1] < y[0][1]:
            l = x[0]
        else:
            l = y[0]

        if x[1][0] > y[1][0]:
            r = x[1]
        elif x[1][0] < y[1][0]:
            r = y[1]
        elif x[1][1] < y[1][1]:
            r = x[1]
        else:
            r = y[1]

        return l, r

    def composition(f, g):
        return f ^ g

    def e():
        return None

    def _id():
        return 0

    times = 1000000006
    mod = 1000000007
    for test_num in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        V = [((A[i], i), (A[i], i)) for i in range(N)]  # ((min, index), (max, index))
        B = [A[i] * times % mod for i in range(N)]

        def mapping(f, x):
            if x is None:
                return None
            elif f == 0:
                return x
            else:
                li = x[1][1]
                ri = x[0][1]
                # print(f'li: {li}, ri: {ri}', file=sys.stderr)
                lv = A[li] if B[li] == x[1][0] else B[li]
                rv = A[ri] if B[ri] == x[0][0] else B[ri]
                return (lv, li), (rv, ri)
        
        tree = LazySegTree(op, e(), mapping, composition, _id(), V)
        Q = int(input())
        ans = 0
        
        for q in range(Q):
            if q % 1000 == 0:
                print(f'q: {q}', file=sys.stderr)
            l, r = map(int, input().split())
            l -= 1
            tree.apply(l, r, 1)
            ans += tree.all_prod()[1][1] + 1
        print(f'Case #{test_num + 1}: {ans}')


if __name__ == '__main__':
    main()