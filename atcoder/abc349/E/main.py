#!/usr/bin/env python3
import sys
from functools import cache


# dfs, win_lose, game
def main():
    A = [list(map(int, input().split(" "))) for _ in range(3)]
    S = A[0] + A[1] + A[2]

    def next_hands(s) -> list[int]:
        possible_hands = [i for i in range(9) if (s >> (2 * i) & 3) == 0]
        return possible_hands

    # 0: no winner, 1: takahashi, 2: aoki
    def test_strait(s):
        def test_3spaces(spaces):
            unq = list(set(spaces))
            if len(unq) == 1 and unq[0] != 0:
                return unq[0]

        horizontal = [[s >> (i * 6 + j * 2) & 3 for j in range(3)] for i in range(3)]
        vertical = [[s >> (i * 6 + j * 2) & 3 for i in range(3)] for j in range(3)]
        diagonal = [
            [s >> (i * 6 + i * 2) & 3 for i in range(3)],
            [s >> ((2 - i) * 6 + i * 2) & 3 for i in range(3)]
        ]
        all = horizontal + vertical + diagonal
        res = list(filter(lambda x: x is not None, map(test_3spaces, all)))
        # print(f'all={all} res={res}', file=sys.stderr)
        return res[0] if len(res) > 0 else 0


    @cache
    def dfs(s, player) -> bool:
        # マスが埋まったので点数チェック
        if len(next_hands(s)) == 0:
            score = 0
            for i in range(9):
                if s >> (i * 2) & player != 0:
                    score += S[i]
                elif s >> (i * 2) & player == 0:
                    score -= S[i]
                else:
                    assert(False)

            # print(f's={bin(s)} player={bin(player)} score={score}', file=sys.stderr)
            return score > 0

        winner = test_strait(s)
        if winner != 0:
            # print(f's={bin(s)} player={bin(player)} winner={winner}', file=sys.stderr)
            return player == winner

        win = False
        for i in next_hands(s):
            assert(s >> (2 * i) & 3 == 0)
            if not dfs(s | (player << (2 * i)), player ^ 3):
                win = True # 相手が負けるとwinになる

        return win


    ans = "Takahashi" if dfs(0, 1) else "Aoki"
    print(ans)


if __name__ == '__main__':
    main()
