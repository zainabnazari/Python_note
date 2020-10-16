#file name: match.py

import numpy as np
from numpy.random import choice
def tour(b,r):
    c=b.size//2
    pair=choice(b, size=(c,2), replace=False)
    print("************************")
    print("This is the",r,"round")
    print(pair)
    if b.size % 2 ==1:
     notchosen=b[np.isin(b, pair)==False]
     print("Number", notchosen, "needs to wait.")
    winners=np.asarray(eval(input("Who (are) is the winner(s)? ")))
    if b.size %2==1:
     if winners.size>1:
       lucky=np.asarray(choice(winners, size=(notchosen.size)))
     else:
      lucky=winners
     print("Number", notchosen, "needs to play against", lucky)
     who=np.asarray(eval(input("Who won? ")))
     winners=np.asarray(np.where(winners==lucky, who, winners))
    return winners
p=input("Number of players: ")
a=eval(p)
r=1
people=np.arange(a)
while people.size>=2:
      people=np.asarray(tour(people,r))
      r=r+1
print("Cheers!")

'''
output for 9 participants:

Number of players: 9
************************
This is the 1 round
[[6 3]
 [7 1]
 [0 8]
 [2 4]]
Number [5] needs to wait.
Who (are) is the winner(s)? 6,7,8,2
Number [5] needs to play against [6]
Who won? 5
************************
This is the 2 round
[[2 8]
 [5 7]]
Who (are) is the winner(s)? 2,7
************************
This is the 3 round
[[7 2]]
Who (are) is the winner(s)? 7
Cheers!


'''
