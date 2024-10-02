#!/usr/bin/env python3
import sys


class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


# trie
def main():
    N = int(input())
    S = input().split(" ")

    trie = [TrieNode()]
    ans = 0
    for s in S:
        cur = 0
        for c in map(lambda x: ord(x) - ord('a'), s):
            if trie[cur].next[c] == None:
                trie[cur].next[c] = len(trie)
                trie.append(TrieNode())
            cur = trie[cur].next[c]
            ans += trie[cur].cnt
            trie[cur].cnt += 1

    print(ans)


if __name__ == '__main__':
    main()
