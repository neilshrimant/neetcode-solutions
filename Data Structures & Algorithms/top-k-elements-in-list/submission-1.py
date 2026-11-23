class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] += 1
        
        count_arr = [[] for _ in range(len(nums)+1)]

        for num,cnt in count_map.items():
            count_arr[cnt].append(num)
        
        res = []

        for i in range(len(count_arr)-1,0,-1):
            for num in count_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        