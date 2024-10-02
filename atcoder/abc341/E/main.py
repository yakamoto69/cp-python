#!/usr/bin/env python3
import sys

from atcoder.fenwicktree import FenwickTree

# fenwick_tree, bit
def main():
    N, Q = list(map(int, input().split(" ")))
    S = input()
    tree_to_right = FenwickTree(N)
    tree_to_left = FenwickTree(N)

    def flip(tree, i):
        if 0 <= i < N:
            # prev + cur = 1
            # cur = prv + x
            # => x = 1 - 2*prev
            tree.add(i, 1 - 2 * tree.sum(i, i + 1))

    for i in range(1, N):
        if S[i] == S[i - 1]:
            tree_to_right.add(i, 1)

    for i in range(0, N - 1):
        if S[i] == S[i + 1]:
            tree_to_left.add(i, 1)

    for _ in range(Q):
        tpe, l, r = list(map(int, input().split(" ")))
        l -= 1
        if tpe == 1:
            # tree_to_right
            if l > 0:
                flip(tree_to_right, l)
            flip(tree_to_right, r)

            # tree_to_left
            flip(tree_to_left, l - 1)
            if r - 1 < N - 1:
                flip(tree_to_left, r - 1)
        else:
            yes = tree_to_right.sum(l + 1, r) == 0 and tree_to_left.sum(l, r - 1) == 0
            ans = "Yes" if yes else "No"
            print(ans)

if __name__ == '__main__':
    main()
