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
    print("You lay down and fall asleep. However, you laid down right on shore and you drown from the ocean's waves")
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
    def printHistory(self):
        print("You go to the paper on the wall. It's really hard to make out what it says but you decipher it to say: this shelter was built in 1682 by pirates who inhabited the island. They built the shelter to protect themselves from the harsh whether.")
    def printWalls(self):
        print("You exam the walls. They're made of old sticks and are tied together with a strong rope that you've never seen before.")

class NumberCombo:
    def __init__(self, numbers):
        self.numbers = []
    def addNumber(self, numbers):
        self.numbers.append(numbers)
    def printNumbers(self):
        print("You put in the numbers: " + ", ".join(self.numbers))

def addition(n):
    return n + n
pet = Animal("", [])
shelter = Shelter()
chosenNumbers = NumberCombo([])
correctCombo = 18

def choiceABA():
    print("You go into the shelther and see a small piece of paper on the wall, a small and almost broken bed, and a small window. There is sunlight peaking through everywhere. Do you want to exam the walls or the paper?")
    answer = input(">").lower()
    if "w" in answer:
        choiceWalls()
    else:
        choicePaper()

def choiceWalls():
    shelter.printWalls()
    print("\nAfter examining the walls, you take a step back. Would you like to read what the paper says now?")
    answer = input(">").lower()
    if "y" in answer:
        choicePaper()
    else:
        choiceBed()

def choicePaper():
    shelter.printHistory()
    print("\nAfter reading the peice of paper, you're extremly intrugied and interested about the island now. However, you're very tired and you should get some rest. Would you like to go to bed?")
    answer = input(">").lower()
    if "y" in answer:
        choiceBed()
    else:
        print("You go back outside of the shelther and start walking around. You walk for a couple hours and eventually pass out. A great storm comes over and magically kills you.")
        gameOver()

def choiceBed():
    print("You lay down on the broken bed but it supports your body weight.")
    if pet.name != "":
        print(pet.name + " lays down next to you and you both fall asleep.")
    else:
        print("You eventually fall asleep.")
    print("You wake up in the middle of the night to hearing a crazy storm. Surprisingly, no part of the storm is seeping into the shelter.")
    weather()


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
    print("Would you like to train " + pet.name + " another trick?")
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
    print("Would you like to train " + pet.name + " another trick?")
    newAnswer = input(">").lower()
    if "y" in newAnswer:
        choiceAddAnotherTrick()
    else:
        choiceContStory()

def choiceContStory():
    print("You begin to walk back from where you started now with your new companion. You go back and see the shelter again. It's been a very long day and the sun is starting to set so you go into the shelther that you passed by earlier.")
    choiceABA()

def weather():
    print("You get up out of bed and look out the window. It looks like it's raining acid! you think to yourself:") 
    print("*how can this even be possible?* Very confused, you just decide to head back to bed thinking that you're dreaming.")
    print("You wake up the next morning to see a bunch of sunshine and the storm last night felt like it never happened.")
    print("You walk outside the hut, do you want to get back on your raft and swim away or do some exploring?")
    answer = input(">").lower()
    if "r" or "s" in answer:
        print("You get on your raft and go out into the ocean. After 3 days you see nothing and die of starvation/dehydration.")
        gameOver()
    else:
        exploreIsland()

def exploreIsland():
    if pet.name != "":
        print(pet.name + " runs out of the hut chasing after you. You smile with glee. He sprints out in front of you and you chase after him.")
        print("You finally catch up to " + pet.name + " and look up to see some beautiful mountains and new terrian. " + pet.name + " is wagging their tail.")
        print("Do you follow " + pet.name + "?")
        answer = input(">").lower()
        if "y" in answer:
            xMarksTheSpot()
        else:
            mountains()
    else:
        print("You start randomly exploring the island and you go up a random hill. You reach the summit and look out and admire the beauty.")
        print("You begin your decent back down the hill")
        finalDestination()

def mountains():
    print("You go up the mountain and then trip down the other side and die")
    gameOver()

def finalDestination():
    print("You trip over a rock and tumble down the hill and die")
    gameOver()

def xMarksTheSpot():
    print("You follow " + pet.name + " as they guide you up the mountain. Suddenly, " + pet.name + " starts doing all the " + pet.printTricks)
    print("You stand there confused and then " + pet.name + " starts digging, still clearly very excited. You begin to dig with " + pet.name + ".")
    print("After a couple hours of continuous digging, you pull out a treasure chest!")
    print("You pull it out of the ground and " + pet.name + "sits next to you. You see it has a 4 combo lock on it. You put in 4 random numbers and try to open the chest but nothing happens")
    openChest()

def openChest():
    print("You try again and nothing happens. You look around the chest and notice it says the combo is a random variation of 4 numbers that add up to 1.... you can't read the rest as it's been scratched away.")
    guessNumbers()

def guessNumbers():
    print("Put in the first number")
    guessOne = input(">")
    chosenNumbers.addNumber()
    print("Put in the second number")
    guessTwo = input(">")
    chosenNumbers.addNumber()
    print("Put in the third number")
    guessThree = input(">")
    chosenNumbers.addNumber()
    print("Put in the last number")
    guessFour = input(">")
    chosenNumbers.addNumber()
    comboAddition = map(addition, chosenNumbers.numbers)
    if comboAddition != correctCombo:
        openChest()
    else:
        print("You opened the chest! You find a magic crystal that says teleportation. You say: ")
        print("Take me home please. and Poof, you're back home. The End, you win!")




start()