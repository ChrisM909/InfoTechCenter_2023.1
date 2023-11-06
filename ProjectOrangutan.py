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

# Variable to call weather() once in our Vehicle Response System - VRS
weatherAlert = weather()

# VRS() will allow my vehicle to respond based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated your alarm by 30 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 60 MPH.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated your alarm by 50 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 40 MPH.")
    elif weatherAlert == "Thunder":
        print("\nNational Weather Service has updated your alarm by 40 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 45 MPH.")
    elif weatherAlert == "Rain":
        print("\nNational Weather Service has updated your alarm by 35 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 50 MPH.")
    elif weatherAlert == "Cloudy":
        print("\nThe weather forcast is calling for a", weatherAlert, "day, Enjoy your drive!")
    elif weatherAlert == "clear":
        print("\nThe weather forcast is calling for a", weatherAlert, "day, Enjoy your drive with the blue sky!")
    else:
        print("\nThe weather forcast is calling for a", weatherAlert, "day, Enjoy your drive with the wind in the air!")

vehicleResponseSystem()