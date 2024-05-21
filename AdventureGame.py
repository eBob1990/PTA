weapon = False

def showShadowFigure():
    directions = ["right", "left","down"]
    print("You see a dark shadowy figure appear in the distance. Your feel fear rush over you. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/down")
        userInput == input()
        if userInput == "right":
            shieldScene()
        elif userInput == "left":
            print("You find a secret path")
        elif userInput == "down":
            introScene()
        else:
            print("Please enter a valid option for the adventure game.")

def shieldScene():
    directions = ["up", "down"]
    print("You find a broken shield that has been dropped on the ground. You recognise the crest on it. Someone has been here recently. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: up/down")
        userInput = input()
        if userInput == "up":
            print("You made it! You've made it to Berlos! You exit the path and head for the city.")
            quit()
        elif userInput == "down":
            showShadowFigure()
        else:
            print("Please enter a valid option for the adventure game.")

def hauntedPath():
    directions = ["right","left","up"]
    print("You hear strage voices. YOu think you have awoken some of the dead. Where would you like to go?")
    userInput = ""
    while userInput not in directons:
        print("Options: right/left/down")
        userInput = input()
        if userInput == "right":
            print("Multiple ghoul-like creaters start emerging as you enter the room. You are killed.")
        elif userInput == "left":
            print("You made it! You've made it through the haunted path and out to the city of Berlos!")
        elif userInput == "down":
            introScene()
        else:
            print("Please enter a valid option for the adventure game.")

def showSkeletons():
    directions = ["down","up"]
    global weapon
    print("You see a wall of skeletons as you walk down this path. Someone is watching you. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/down/up")
        userInput = input()
        if userInput == "left":
            print("You find a rock that looks like it has been moved recently. You move the rock to discover a knife.")
            weapon = True
        elif userInput == "down":
            introScene()
        elif userInput == "up":
            strangeCreature()
        else:
            print("Please enter a valid option for the adventure game.")

def stangeCreature():
    actions = ["fight","flee"]
    global weapon
    print("A strange ghoul-like creature has appeared. You can either run or fight it. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("You kill the ghoul with the knife you found earlier. After moving forward past the corpse of the Ghoul you see over the horizon, the city of Berlos. Well done!")
            else:
                print("The ghoul creature has killed you.")
            quit()
        elif userInput == "flee":
            showSkeletons()
        else:
            print("Please eneter a valid option for the adventure game.")

def introScene():
    directions = ["left" , "right", "up", "down"]
    print("You are at a crossroads, and you can choose do go down any of the four paths. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/up/down")
        userInput = input()
        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            showSkeletons()
        elif userInput == "up":
            hauntedPath()
        elif userInput == "down":
            print("You find a secret path.")
        else:
            print ("Please enter a valid option for the adventure game.")

if __name__ == "__main__":
    while True:
        print ("Welcome to the Adventure Game!")
        print ("You are travelling to the city of Berlos.")
        print ("However, during your journey, you find yourself lost.")
        print ("You can choose to walk in multiple directions to find the city of Berlos.")
        print ("This is how your adventure begins...")

        print ("Let's start with your name: ")
        name = input()
        print ("Good luck, " +name+ ".")
        introScene()