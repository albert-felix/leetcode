class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        for interval in intervals:
            if(not len(result) or (result[-1][1] < interval[0]) ):
                result.append(interval)
            else:
                result[-1][1] = max(interval[1], result[-1][1] )
        return result
        
