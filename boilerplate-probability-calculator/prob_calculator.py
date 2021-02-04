import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self,**kwargs):
    self.contents = []
    for colour in kwargs.keys():
      self.contents.extend([colour for x in range(kwargs[colour])])

  def draw(self,number):
    balls = []
    
    if number >= len(self.contents):
      balls.extend(self.contents)
      del self.contents[:]
      return balls

    for num in range(number):
      balls.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
    return balls  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0

  for experiment in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)

    for colour in expected_balls.keys():
      if balls.count(colour) < expected_balls[colour]:
        met_expectations = False
        break
      met_expectations = True
    
    if met_expectations:
      M += 1  
  
  return M/num_experiments 

