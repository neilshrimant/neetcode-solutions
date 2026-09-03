class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index = 0
        count_map = {}
        for c in keyboard:
            count_map[c] = index
            index += 1
        res = count_map[word[0]]
        for i in range(1, len(word)):
            res += abs(count_map[word[i]] - count_map[word[i - 1]])
        return res


