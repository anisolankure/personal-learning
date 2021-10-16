class Player:
  def __init__(self, name, age, batAvg, ballAvg):
    self.name = name
    self.age = age
    self.batAvg = batAvg
    self.ballAvg = ballAvg

  def myfunc(self):
    print("Name: " + self.name 
    + "\n Age: " + self.age
    + "\n Batting Avg: " + str(self.batAvg)
    + "\n Balling Avg: " + str(self.ballAvg))