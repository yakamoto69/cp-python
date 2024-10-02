import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder__bit_code = """
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2

    return x
"""

atcoder._bit = types.ModuleType('atcoder._bit')
exec(_atcoder__bit_code, atcoder._bit.__dict__)


_atcoder_segtree_code = """
import typing

# import atcoder._bit


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = atcoder._bit._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
"""

atcoder.segtree = types.ModuleType('atcoder.segtree')
atcoder.segtree.__dict__['atcoder'] = atcoder
atcoder.segtree.__dict__['atcoder._bit'] = atcoder._bit
exec(_atcoder_segtree_code, atcoder.segtree.__dict__)
SegTree = atcoder.segtree.SegTree

#!/usr/bin/env python3

import sys
from operator import add
from typing import List
# from atcoder.segtree import SegTree

sys.setrecursionlimit(300000)

# g: List[List[(to_node, edge_id, edge_info)]] edge_infoにはfrom, to以外の情報を引いたweightなどが入っている([:2])
#
# @return (in, out, tour, visit, depth, edge)
# in: サブツリーの開始
# out: サブツリーの終了
# tour: in, outを展開した配列
# visit: tourとは違って、訪れている時にどこにいるかの配列
# depth: 深さ
# edge:
def euler_tour(N, g: List[List[any]], root):
    tour = [-1] * (2*N)
    depth = [-1] * (2*N)
    visit = [-1] * (2*N)
    edge = [-1] * (2*N)
    i_in = [-1] * N
    i_out = [-1] * N
    i = 0

    stack = [(root, -1, 0, -1)]
    first_visit = [True] * N

    while stack:
        u, par, d, e = stack.pop()
        if first_visit[u]:
            first_visit[u] = False
            stack.append((u, par, d, e))
            depth[i] = d
            i_in[u] = i
            tour[i] = u
            visit[i] = u
            edge[i] = e
            i += 1
            for e1 in g[u]:
                v = e1[0]
                if v == par:
                    continue
                stack.append((v, u, d + 1, e1[1]))

        else:
            i_out[u] = i
            depth[i] = d - 1
            tour[i] = u
            visit[i] = par
            edge[i] = e
            i += 1

    return i_in, i_out, tour, visit, depth, edge

def lca(segment_tree, i_in, u, v):
    left, right = i_in[u], i_in[v]
    if left > right:
        left, right = right, left
    return segment_tree.prod(left, right + 1)[1]

# @return List[List[(to_node, edge_id, edge_info)]]
# edge_info([2:])はedgesで受けとたたものからfrom, toの情報を抜いたもの
def pack_u_graph(n: int, edges: List[List[int]]):
    p = [0] * n
    m = len(edges)

    for i in range(m):
        p[edges[i][0]] += 1
        p[edges[i][1]] += 1

    g: List[List[(int, int, List[int])]] = [[None] * p[i] for i in range(n)]

    for i in range(m):
        from_node = edges[i][0]
        to_node = edges[i][1]

        p[from_node] -= 1
        p[to_node] -= 1

        g[from_node][p[from_node]] = (to_node, i, edges[i][2:])
        g[to_node][p[to_node]] = (from_node, i, edges[i][2:])

    return g


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N - 1)]
    for e in E:
        e[0] -= 1
        e[1] -= 1

    g = pack_u_graph(N, E)
    i_in, i_out, tour, visit, depth, edge = euler_tour(N, g, 0)
    # print(i_in, i_out, tour, visit, depth, edge, file=sys.stderr)
    tree_tour = SegTree(min, (1e9, -1), [(depth[i], visit[i]) for i in range(len(tour))])

    # ルート(0)には値が入っていない
    node_edge = [-1] * N
    edge_node = [-1] * N
    for u in range(1, N):
        node_edge[u] = edge[i_in[u]]
        edge_node[edge[i_in[u]]] = u

    init_w = [0] * (2*N)
    for u in range(1, N):
        edge_id = node_edge[u]
        w = E[edge_id][2]
        init_w[i_in[u]] = w
        init_w[i_out[u]] = -w

    tree_weight = SegTree(add, 0, init_w)

    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            edge_id = q[1] - 1
            w = q[2]
            u = edge_node[edge_id]
            tree_weight.set(i_in[u], w)
            tree_weight.set(i_out[u], -w)
        else:
            u = q[1] - 1
            v = q[2] - 1
            w = lca(tree_tour, i_in, u, v)
            a = tree_weight.prod(0, i_in[u] + 1)
            b = tree_weight.prod(0, i_in[v] + 1)
            c = tree_weight.prod(0, i_in[w] + 1)
            # print(f'lca({u},{v})={w}', a, b, c, file=sys.stderr)
            print(a + b - c * 2)

    pass

if __name__ == '__main__':
    main()
