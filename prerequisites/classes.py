#Classes

class MyClass:
  def __init__(self, nums):
    #Create member vars
    self.nums = nums
    self.size = len(nums)

  # self keyword required as a param
  def getLength(self):
    return self.size
  
  def getDooubleLength(self):
    return 2 * self.getLength()


