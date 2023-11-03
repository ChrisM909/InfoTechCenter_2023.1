"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""

#Import Libraries Here
import time
import sys
import random
from time import sleep

timeToSleep = 2

print("\n\nWelcome - InfoTech Center 2023\n")
time.sleep(timeToSleep)

#Add code to have the ellipses add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so, message is printed on top of the previous line
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded - Retina Scanned - Access Granted")

print("\n*****************************************************************************************************\n")
print("Checking current gas levels\n")
sleep(1)

# Function that lists Gas Stations, randomly choosing one and Return its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of GasStations
def listOfGasStations():
    gasStations = ["Shell","Speedway","Exon","Costco","Marathon","BP","Circle K","Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

# Function will call the gasLevelGauge to determine gas level and then find a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, check Google Maps for the closest gas station")
        sleep(1.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print(" Your gas tank is on a Quarter of a Tank of gasoline, check Google Maps for the closest gas station")
        sleep(1.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print(" Your gas tank is on a Half a tank which is plenty enough to arrive toward your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at Three Quarter Tank!")
    else:
        print("Your gas tank is full - congrats!")


gasLevelAlert()

