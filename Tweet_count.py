# Implement the class TweetCounts that supports two methods:

# 1. recordTweet(string tweetName, int time)

# Stores the tweetName at the recorded time (in seconds).
# 2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)

# Returns the total number of occurrences for the given tweetName per minute, hour, or day (depending on freq) starting from the startTime (in seconds) and ending at the endTime (in seconds).
# freq is always minute, hour or day, representing the time interval to get the total number of occurrences for the given tweetName.
# The first time interval always starts from the startTime, so the time intervals are [startTime, startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ... , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)> for some non-negative number i and delta (which depends on freq).  
     
     
from collections import *
class TweetCounts(object):
 
    def __init__(self):
        
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        
        times = self.tweets[tweetName]
        
        size = 0 
        secs = 0
        
        if(freq == 'minute'):
            secs = 60
            size = (endTime - startTime) / 60 + 1
        elif(freq == 'hour'):
            secs = 3600
            size = (endTime - startTime) / 3600 + 1
        else:
            secs = 86400
            size = (endTime - startTime) / 86400 + 1
                
        r = [0] * int(size)
        
        for i in times:
            if(startTime <= i and i <= endTime):
                index = int((i-startTime)/secs)
                r[index] += 1
        return r