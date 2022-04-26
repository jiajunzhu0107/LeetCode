#setBlockDates([1,3],[5,8],[13,20]);
#[-8,5], [5,3], [20, 50]
#[4,4]
# returns nothing

#getAvailableDates();
#[4,4],[9,12],[21,30]

#setBlockDates([24,28]);
#// returns nothing
# range[1,30] 
#getAvailableDates();
#[4,4],[9,12],[21,23],[29,30]

#start : Long.MIN
#end : Long.MAX
#setBlockDates([1,3],[5,8],[13,20]);
#setBlockDates([7,9]);
min [1, 5, 7, 13]
max [3, 8, 9, 20]

#getAvailableDates();
#[Long.MIN,0],[4,4],[9,12],[21,Long.MAX]

class AvailableDates():
  def __init__(self):
    self.available_dates = [i for i in range(1, 31)]
  def setBlockDates(self, *args):
    for date_range in args:
      for date in range(date_range[0],date_range[1]+1):
        if date in self.available_dates:
            self.available_dates.remove(date)
  
  def getAvailableDates(self):
    res = []
    current_min = None
    current_max = None
    for i, date in enumerate(self.available_dates):
      if not current_min:
        current_min = date
      if i+1 >= len(self.available_dates) or self.available_dates[i+1] > date + 1:
        #if len(current_range) == 1: # for [2,2]
        #  current_range.append(date)
        #res.append(current_range)
        current_max = date
        res.append([current_min, current_max])
        current_min = None       
    return res

obj = AvailableDates()
obj.setBlockDates([1,3],[5,8],[13,20])
res = obj.getAvailableDates()
print(res)
obj.setBlockDates([24,28])
res = obj.getAvailableDates()
print(res)
