from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newI = []

        idx = 0
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, [newInterval[0], newInterval[1]])
                idx = i
                break


        i = 0
        while i <= len(intervals):
            s = intervals[idx][0]
            e = intervals[i][1]
            while s <= e and i != idx:
                newI.insert(idx, [intervals[i][0], max(intervals[i][1], intervals[idx][1] )])
                i += 1
            else:
                newI.insert(i, intervals[i])
                i += 1

        return newI


s = Solution()
s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]]
, [4,8])