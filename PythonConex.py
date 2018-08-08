# Initialization
import sys
# Used for sleeping
import time

# Command Interface Stuff?
print("Adding location of Newport.CONEXCC.CommandInterface.dll to sys.path")
# sys.path.append(r"C:\\Program Files\\Newport\\MotionControl\\CONEX-CC\Bin")
# sys.path.append(r'C:\\Program Files (x86)\\Newport\\MotionControl\\CONEX-CC\Bin')

# Add reference to assembly and import names from namespace
# from CommandInterface import *
# import System

# .NET runtime stuff
# import clr
# clr.AddReferenceToFile("Newport.CONEXCC.CommandInterface.dll")




# OBJECTIVES
# 1) First, a user will specify which controller to move and how much to move it by
# 2) After each increment, the program will ask if the user wishes to move it again or to reset

class PythonConex:

    def __init__(self, instrumentKey):
        # These are the coordinates that should be accepted 
        self.acceptedCoordinates = ['X', 'Y']
        self.currentPosition = 0.0

        # Has something to do with the opening of an instrument
        
        self.instrumentKey = instrumentKey
        self.ret = CC.OpenInstrument(self.instrumentKey)

    def move_absolute(self, positionToMoveTo):
        CC.PA_Set(self.controllerAddress, positionToMoveTo)

    def move_repetitively(self, userIncrement, userStoppingValue, timeToSleep = 30):
        while (self.currentPosition + userIncrement) <= userStoppingValue:
            print(f"Current Position: {self.currentPosition}")
            print(f"About to move position by: {userIncrement}")

            self.currentPosition += userIncrement

            # Should move the controller if working properly
            hasMoved = (CC.PA_Set(self.controllerAddress, self.currentPosition)) == 0

            if hasMoved:
                print("Increment has moved.")

            print(f"Current Position: {self.currentPosition}\n")
            print("About to sleep")
            # Sleeps
            time.sleep(timeToSleep)

    # This gets the coordinate to use
    def get_coordinate(self):
        userCoordinate = input("Would you like to move the X or Y coordinate?\n").upper()

        while (userCoordinate in self.acceptedCoordinates) is False:
            print("Wrong coordinate is inputted.")
            userCoordinate = input("would you like to move the X or Y coordinate?\n").upper()

        return userCoordinate
    
    def get_increment(self):
        userIncrement = float(input("How much would you like to increment the value by?\n"))
        return userIncrement

    def get_stopping_value(self):
        userStoppingValue = float(input("What ending value do you want?\n"))
        return userStoppingValue

    def execute(self):
        userCoordinate = self.get_coordinate()
        userIncrement = self.get_increment()
        userStoppingValue = self.get_stopping_value()
        self.move_repetitively(userIncrement, userStoppingValue)
        CC.CloseInstrument()