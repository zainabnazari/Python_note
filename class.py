# file name: class.py

#We define a blueprint of how a time looks like and what it can do:
class time:
  #Here we define which attributes an object of the class time has and how they are initialized:
  hour=1
  minute=1
  #Here we define which functions the class time offers:
  #settime sets the time to a given hour and minute.
  def settime(self,hour,minute):
    self.hour=hour
    self.minute=minute
  #addmin adds a given number of minutes to the time.
  def addmin(self, adm):
    self.hour+=(self.minute+adm)//60
    self.minute=(self.minute+adm)%60
    self.hour=self.hour%24
  #Print time prints the time in a nicely formatted way.
  def printtime(self):
    print(self.hour,'h', self.minute, 'min')

#Here we start using the class.
mytime=time()#We now have an object of the class time which is called mytime.
mytime.settime(19, 20)#This is how we call a function of that object: objectname.functionname(parameters).
#The mytime is now 19 hours and 20 minutes.
mytime.addmin(40)
#The mytime is now 20 hours and 0 minutes - because we added 40 minutes.
mytime.printtime()
mytime.addmin(400)
#The time is now 2 hours and 40 minutes, because we added 400 minutes to the previous state of mytime, which was 20 hours and 0 minutes.
mytime.printtime()
print(type(mytime))

'''
the output:
20 h 0 min
2 h 40 min
<class '__main__.time'>
'''
