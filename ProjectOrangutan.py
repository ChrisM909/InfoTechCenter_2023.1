print("\n**************************************************\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a function randomly choosing the weather from a list
def weather():
    weatherForcast = ["Snowing","Blizzard","Thunder","Rain","Cloudy","Clear","Windy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition
