# file name: function.py
from math import sin, log, pi # this line imports two functions sin(), log() and a constant (pi) from the math library.
def func(s): # this is a function which is defined by the coder, and it returns a number.
  return(sin(s)**2+log(s/5)+pi)
if __name__=="__main__":
 print(func(45)) # in this line two functions are called the func(45) and the print().
# the output of this code is computation of sin(45)**2+log(45/5)+3.14=6.062854038990598
