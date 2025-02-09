class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = []
        for interval in intervals:
            for num in range(interval[0], interval[1] + 1):
                new.append(num)
        
        new = sorted(set(new))

        merged = []
        start = new[0]
        
        for i in range(1, len(new)):
            if new[i] != new[i - 1] + 1:
                merged.append([start, new[i - 1]])
                start = new[i]
        
        merged.append([start, new[-1]])

        return merged
