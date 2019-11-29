import os
import sys
import time

from os import system, name   
def clear(): 
    if name == 'nt': 
        _ = system('cls')   
    else: 
        _ = system('clear') 

def countingValleys(steps):
    altitude = 0
    valleyCount = 0
    valley = False

    for step in steps:
        if step == "D":
            altitude-=1
            if altitude < 0 and valley == False:
                valley = True
                valleyCount+=1
        if step == "U":
            altitude+=1
            if altitude >= 0 and valley == True:
                valley = False

    return (valleyCount)

print(r"""

        _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/jgs     `.  / /       `.~-^=-=~=^=.-'      '-._ `._

Challenge: Counting Valleys

ASCII Artist: Joan Stark @ https://www.asciiart.eu/
      
  """)

time.sleep(5)
clear() 
time.sleep(2)

steps = input("Input the string of steps taken with 'D' for down and 'U' for up. Leave no space in between: ")

result = countingValleys(steps)

print("\nThere were a total of " + str(result) + " valley(s).\n")

time.sleep(10)