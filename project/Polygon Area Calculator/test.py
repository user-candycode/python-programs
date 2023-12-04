import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    print(kwargs)
    if kwargs["blue"].isdigit():
      self.blue = kwargs["blue"]
    if kwargs["orange"].isdigit():
      self.orange = kwargs["orange"]
    if kwargs["black"].isdigit():
      self.black = kwargs["black"]
    if kwargs["green"].isdigit():
      self.green = kwargs["green"]
    if kwargs["green"].isdigit():
      self.green = kwargs["green"]
    print("self.green",self.green)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass