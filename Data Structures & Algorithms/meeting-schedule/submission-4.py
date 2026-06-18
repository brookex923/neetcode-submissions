"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True 

        intervals.sort(key = lambda x: x.start)
        for i in intervals:
            print(i.start)

        curr_min = intervals[0].start
        curr_max = intervals[0].end

        for meeting in intervals[1:]:
            if meeting.start < curr_max:
                return False
            
            
            curr_min = min(curr_min, meeting.start)
            curr_max = max(curr_max, meeting.end)
        
        return True





