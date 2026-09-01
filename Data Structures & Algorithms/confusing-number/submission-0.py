class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid = {"0" : "0", "1" : "1", "6" : "9", "8" : "8", "9" : "6"}
        res = []
        for num in str(n):
            if num not in valid:
                return False

            res.append(valid[num])
        
        res = "".join(res)

        return int(res[::-1]) != n