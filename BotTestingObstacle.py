# -*- coding: utf-8 -*-
"""
Room#22: A lab for testing robots.
"""
import Item as I
import utils
import BotTesting
import Puzzle4

#print("You're in the Bot Testing - Obstacle Room.")
filename = 'BotTestingObstacle'
#utils.roomsvisited[22] = 1


## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}


def basicDes():
    print("[Robotics Testing Facility – Obstacle Course] /nThe lights in the room turn on after I step through the door; this room looks a lot bigger on the inside than it does on the outside.\nLooking around the room, there are areas that are sectioned off; it appears as if there are separate tasks in this room.\nThere are beams and platforms organized all around the room, it appears to be a room for testing one's ability to move effectively.\nTo the East is the door that leads back to [Robotics Testing Facility - Basic Functions]")
    if utils.puzzle4 == False:
        Puzzle4.puzzle4()
        utils.puzzle4 == True

def fancyDes():
    print("[Robotics Testing Facility – Obstacle Course]\nThe beams and platforms organized all around the room are still here, but there's so much more to this room than I originally noticed.\nThe beams and platforms all  around the room have different colors marked on them, as if to indicate the varying levels of skills; there are paths with a Green line through it, some have Yellow lines, and a rare few have Red colored lines.\nThe Red colored paths look like they have the most difficult paths to go through.\nTo the East is the door that leads back to [Robotics Testing Facility - Basic Functions]")
    if utils.puzzle4 == False:
        Puzzle4.puzzle4()
        utils.puzzle4 == True

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():  
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[16] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            BotTesting.basicDes()
            utils.roomsvisited[16] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[16] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            BotTesting.fancyDes()
            utils.roomsvisited[16] = 1
        else:
            print("The door is locked.") 

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def itemsInInventory():
    inventorylist = []
    if len(utils.inventory) == 0 : 
        return inventorylist
    else:
        for each in utils.inventory.keys():
            inventorylist.append(each)
        return inventorylist
    
def listItems():
    lst = itemsInhere()
    for each in lst:
        print(each)
    
def examine(obj):
    lst = itemsInhere()
    #print(obj)
    if obj in lst:
        if itemdictionary[obj][1] == True or itemdictionary[obj][1] == None:
            itemdictionary[obj][0].examine()
    else:
        print("Hmm... {} doesn't seem to be in this room!".format(obj))

def use(obj):
    lst = itemsInhere()
    lst2 = itemsInInventory()
    #print(lst2)
    if obj in lst and obj not in lst2:
        itemdictionary[obj][0].use()
    elif obj in lst2 and obj not in lst:
        where = utils.inventory[obj]
        __import__(where).use(obj)
    elif obj in lst and obj in lst2:
        itemdictionary[obj][0].use()
    else:
        print("Hmm... {} can't use an object that's not in this room! You can check your inventory to look for items to use".format(obj))
 
def take(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].take(filename)
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))

def unlock(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].unlock()
    else:
        print("Hmm... {} cannot be unlocked!".format(obj))

def removeInventory(obj):
    lst = itemsInhere()
    if obj in lst:
        (utils.inventory).remove(obj)
    else:
        print("Hmm... {} is not in inventory!".format(obj))
