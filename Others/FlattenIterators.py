# https://techdevguide.withgoogle.com/resources/former-interview-question-flatten-iterators/#!
from collections import deque
class IF:
#  public IF(Iterator<T>[] iterlist){
    def __init__(self, iterlist):
        self._queue = deque()
        for iter in iterlist:
            if iter.hasNext():
                self._queue.append(iter)
#  }
    def next(self):
        if not self.hasNext():
            return None
        iter = self._queue.popleft()
        res = iter.next()
        if res.hasNext():
            self._queue.append(res)
        return res
 
    def hasNext(self):
        return len(self._queue) > 0

