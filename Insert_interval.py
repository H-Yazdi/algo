# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

 class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        bisect.insort(intervals, newInterval)
        i = intervals.index(newInterval)
        if i - 1 >= 0 and intervals[i-1][1] >= intervals[i][0]:
            intervals[i -1][1] = max(intervals[i-1][1], intervals[i][1])
            intervals.remove(intervals[i])
            i -= 1
        while i + 1 < len(intervals) and intervals[i][1] >= intervals[i + 1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            intervals.remove(intervals[i + 1])
                    
        return intervals