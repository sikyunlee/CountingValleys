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

steps = input("Input the string of steps taken with 'D' for down and 'U' for up. Leave no space in between: ")

result = countingValleys(steps)

print("There were a total of " + str(result) + " valleys.\n")
