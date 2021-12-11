def intro():
    print("Poof. You've just landed in the middle of the ocean on a small raft. You look around and all you see is ocean and a small island in the distance. Would you like to swim to shore?")

def start():
    intro()
    answer = input(">").lower()
    if "y" in answer:
        choiceA()
    else:
        gameOver()

def gameOver():
    print("Im sorry, but your game is now over. Would you like to play again?")
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        print("Thanks for playing!")

def choiceA():
    print("You swim to shore with your hands as paddles. This takes you a very long time and you make it to shore. You're very tired. Would you like to take a nap or explore?")
    answer = input(">").lower()
    if "n" in answer:
        choiceAA()
    else:
        choiceAB()


def choiceAA():
    print("You lay down and fall asleep. However, you laid down right on shore and you drown from the ocean")
    gameOver()

def choiceAB():
    print("You decide to stumble up the island and you see a shelter. Would you like to explore it?")
    answer = input(">").lower()
    if "y" in answer:
        choiceABA()
    else:
        choiceABB()



class Animal:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = []
    def addTrick(self, tricks):
        self.tricks.append(tricks)
    def printTricks(self):
        print("You trained " + pet.name + " to: " + ", ".join(self.tricks))

class Shelter:
    def __init__ (self, history, walls):
        self.history = print("You read the paper on the wall and it says that this shelter was built in 1682 by pirates who inhabited the island. They built the shelter to protect themselves from the harsh whether.")
        self.walls = print("You exam the walls. They're made of old sticks and tied together with strong rope that you've never seen before.")

pet = Animal("", [])

def choiceABA():
    print("You go into the shelther and see a small piece of paper on the wall, a small and almost broken bed, and a small window. There is sunlight peaking through everywhere. Do you want to exam the walls or the paper?")
    answer = input(">").lower()
    if "w" in answer:
        choiceABAA()
    else:
        choiceABAB()

def choiceABAA():
    print("")

def choiceABAB():
    print("")

def choiceABB():
    print("You choose not to go to the shelther, you keep walking around the island and you see a bunch of palm trees, some hills, a little bit of grass but mainly sand. You go towards one of the mountains and something is rattling in the bushes. Do you inspect the bush or run away?")
    answer = input(">").lower()
    if "r" in answer:
        choiceABBA()
    else:
        print("You go towards a bush and suddenly a small puppy pops out! He's super happy to see you so you decide to keep him!")
        choiceABBB()

def choiceABBA():
    print("You run away as fast as you can, you also decide to scream at the top of your lungs, what do you say?")
    answer = input(">").upper()
    print("You Scream: " + answer)

def choiceABBB():
    print("What do you want to name him?")
    answer = input(">")
    pet.name = answer
    print("Awesome! You named your new dog " + pet.name)
    choicePetTricks()

def choicePetTricks():
    print("He looks to be very well trained. Maybe you should try and teach him a trick ;) (Type in the trick you want to train your new companion)")
    answer = input(">").lower()
    pet.addTrick(answer)
    pet.printTricks()
    print("Would you like to train " + pet.name + "another trick?")
    newAnswer = input(">").lower()
    if "y" in newAnswer:
        choiceAddAnotherTrick()
    else:
        choiceContStory()
        
def choiceAddAnotherTrick():
    print("Type in another trick")
    answer = input(">").lower()
    pet.addTrick(answer)
    pet.printTricks()
    print("Would you like to train " + pet.name + "another trick?")
    newAnswer = input(">").lower()
    if "y" in newAnswer:
        choiceAddAnotherTrick()
    else:
        choiceContStory()

def choiceContStory():
    print("c")




start()