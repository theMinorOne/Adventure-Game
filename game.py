#imports
import random as rand
import time as t
import player
import enemy

races = {"h":"Human", "e":"Elf", "o":"Orc", "d":"Dwarf"}
classes = {"k":"Knight", "w":"Warriror", "h":"Hunter", "a":"Assassin", "m":"Mage"}

def start():
    print("Welcome Adventurer!")
    pName = input("Enter your name: ")
    pRace = chooseRace()
    plClass = chooseClass()
    return player.Player(name = pName, race = pRace, pClass = plClass)

def chooseRace():
    choice = ""
    print("Choose a race: ")
    for key, value in races.items():
        print(value + " : " + key)
    choice = input("Your choice: ")
    while (choice not in (races.keys() or races.values())):
        print("Not a valid choice, try again: ")
        choice = input()
    for i in races.keys():
        if choice == i:
            choice = races[i]

    return choice

def randRace(): #generate random race choice
    rand.choice(list(races.values()))

def chooseClass():
    choice = ""
    print("Choose a class: ")
    for key, value in classes.items():
        print(value + " : " + key)
    choice = input("Your choice: ")
    while (choice not in (classes.keys() or classes.values())):
        print("Not a valid choice, try again: ")
        choice = input()
    for i in classes.keys():
        if choice == i:
            choice = classes[i]

    return choice

def randClass(): #generate random class choice
    rand.choice(list(classes.values()))

#Establish possible locations in the game world

places = {"f":"Forest", "m":"Mountain", "v":"Village", "c":"Castle", "t":"Town", "d":"Dungeon"}

def choosePlace():
    choice = ""
    print("Choose a place: ")
    for key, value in places.items():
        print(value + " : " + key)
    choice = input("Your choice: ")
    while (choice not in (places.keys() or places.values())):
        print("Not a valid choice, try again: ")
        choice = input()
    for i in places.keys():
        if choice == i:
            choice = places[i]
    return choice

    
