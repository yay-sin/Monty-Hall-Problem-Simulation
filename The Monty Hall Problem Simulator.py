# The Monty Hall Problem Simulator
import random

# This program overall will ask whether you want to switch or stay at the same door.
# This same decision will be simulated 3000 times, and the number of times and the rate your decision leads to the prize will be written.

print("You have chosen a door, and Monty Hall opens a door that contains a goat. Do you stay with your door of choice or do you switch?")
print("Type \"stay\" or \"switch\".")
while True:
    decision = input()
    if decision.upper() == "STAY":
        break
    elif decision.upper() == "SWITCH":
        break

print("How many times would you like to run this simulation?")

# Waits for the user to input an integer. This integer is the number of times this simulation
# will run. Any non-integer input will ask the user to try again.
while True:
    numberOfTimes = input()
    try:
        if (int(numberOfTimes) - int(numberOfTimes)) == 0:
            break
    except:
        print("Please input an integer.")
        continue

wins = 0 # Wins counter.

# Runs simulation for how many times written in range().
for i in range(int(numberOfTimes)):
    doorWithPrize = random.randint(1,3) # The door number with the million dollar prize.
    doorYouChoose = random.randint(1,3) # The door number the contestent chooses at random.

    # Generates number door that Monty Hall chooses until it is not equal to the door the contestant chooses and the door the prize is in.
    while True:
        doorMontyHallChooses = random.randint(1,3)
        if doorMontyHallChooses != doorWithPrize and doorMontyHallChooses != doorYouChoose:
            break
        else:
            continue
    
    # This is the remaining door not chosen by the contestent or Monty Hall. Logic is basically the same as above.
    while True:
        doorYouDidNotChoose = random.randint(1,3)
        if doorYouDidNotChoose != doorYouChoose and doorYouDidNotChoose != doorMontyHallChooses:
            break
        else:
            continue

    if decision.upper() == "STAY":
        if doorYouChoose == doorWithPrize:
            wins += 1
    elif decision.upper() == "SWITCH":
        if doorYouDidNotChoose == doorWithPrize:
            wins += 1

print("You won " + str(wins) + " out of " + numberOfTimes + " times! That's " + str(round(wins / int(numberOfTimes) * 100, 2)) + "%!")