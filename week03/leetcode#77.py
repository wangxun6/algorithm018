class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()

        def backtrack(tmp: list, index: int) -> None:
            if len(tmp) == k:
                ans.append(tmp[:])
                return
            for i in range(index, n + 1):
                tmp.append(i)
                backtrack(tmp, i + 1)
                tmp.pop()
        backtrack([], 1)
        return ans