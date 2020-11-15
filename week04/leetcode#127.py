from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        list1 = defaultdict(list)
        for w in wordList:
            for _ in range(n):
                list1[w[:_] + '*' + w[_ + 1:]].append(w)
        # BFS
        queue = deque()
        queue.append((beginWord, 1))
        mark_dic = defaultdict(bool)
        mark_dic[beginWord] = True
        while queue:
            cur_word, level = queue.popleft()
            for i in range(n):
                for neighbour in list1[cur_word[:i] + '*' + cur_word[i + 1:]]:
                    if neighbour == endWord: return level + 1
                    if not mark_dic[neighbour]:
                        mark_dic[neighbour] = True
                        queue.append((neighbour, level + 1))
        return 0
