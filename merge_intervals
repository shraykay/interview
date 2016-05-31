class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        
        newRange = [intervals[0]]
        
        for s in sorted(intervals, key=lambda interval: interval.start):
            last_start = newRange[-1].start
            last_end = newRange[-1].end
            if s.start <= last_end:
                newRange[-1].end = max(last_end, s.end)
            else:
                newRange.append(s)
        
        return newRange
