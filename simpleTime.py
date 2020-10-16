#file name: simpleTime.py

class simpleTime:
	minutes = 0
	hours = 0
	def setTime(self, hour, minute):
		self.hours = hour % 24
		self.minutes = minute % 60
		

myTime = simpleTime()
myTime.setTime(59, 2445)
print(myTime.hours, ":", myTime.minutes)
#output: 11 : 45
#setTime takes care of transforming the numbers into a meaningful time.
myTime.minutes = 2445
myTime.hours = 59
print(myTime.hours, ":", myTime.minutes)
#output: 59 : 2445
#manipulating the attributes directly bypasses any efforts to keep them consistent.
"""
output:
11 : 45
59 : 2445
"""