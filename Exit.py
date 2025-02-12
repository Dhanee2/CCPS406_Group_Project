# -*- coding: utf-8 -*-
"""
Room#9: The Exit
"""
import Item as I
import utils
import os
import Hallway6

#print("The ultimate goal.")
filename = 'Exit'
#utils.roomsvisited[9] = 1

itemshere = []## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
}

def basicDes():
    print("[Building Exit] \n Identical to the other Security Checkpoint I walked through earlier, there is a guard desk in between two metal gates, with a set of monitors displaying different moving images. \n There is no one sitting at the desk, but there is a window that faces out to the Security Checkpoint, and one of the guards inside occasionally looks outside. \n To the North is the door that leads back into [Hallway - Section 6].")

def fancyDes():
    print("[Building Exit] \n The vacant Security Checkpoint still sits here, with no one sitting at the desk. \n The window can still be seen with the Security occasionally looking up to check on the Checkpoint. \n To the North is [Hallway - Section 6].")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    Hallway6.basicDes()
    utils.y = utils.y - 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway6!")

def movesouth():
    if utils.GPS == False and utils.disguise == True:
        print("Congrats! You're exiting the Game!")
        os.remove('save.py')
    elif utils.GPS == True and utils.disguise == True:
        print("Your disguise is great, but they can still find you because your GPS tracker is on.\n You need to find your Creator to turn off your GPS tracker.")
    elif utils.GPS == False and utils.disguise == False:
        print("Your GPS is off, but you still need a disguise to leave the building.\n Go back in the Storage Closet and find a disguise so that you won't be spotted when you leave.")
    else:
        print("Congrats! You're exiting the Game!")

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
