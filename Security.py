# -*- coding: utf-8 -*-
"""
Room#15: Security Office
"""

import Item as I
import utils
import Hallway5

#print("You're in the Security Office.")
filename = 'Security'
utils.roomsvisited[15] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],

}

def basicDes():
    print("[Security] \n A room filled with monitors, all showing a different moving image on the screen. \n There are three employees sitting inside, they match the uniform as the Security employee I cleaned up for on the way here. \n They're all too busy watching the screen to take notice of it. \n There is a large glowing button with a label underneath: \n 'Barrier: ACTIVE'. \n Past the guards and the monitors is a large window, it's facing towards the Security Checkpoint outside. \n To the North is the door that leads back into [Hallway - Section 5].")

def fancyDes():
    print("[Security] \n The room is filled with monitors, all showing a different moving image on the screen. \n The same employees are sitting inside, too busy with their jobs to notice me inside. \n The large glowing button is still there with its label underneath. \n The window leading outside still shows a vacant Security Checkpoint. \n To the North is [Hallway - Section 5].")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    utils.x = utils.x - 1
    Hallway5.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Hallway - Section 5.")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")

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