# -*- coding: utf-8 -*-
"""
Room#18: Hallway 2
"""
import Item as I
import utils
import Hallway1
import PrintingLab
import ProgrammingLab
import Hallway3

#print("You're in the Hallway#2.")
filename = 'Hallway2'
utils.roomsvisited[18] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],

}

def basicDes():
    print("[Hallway – Section 2] \n Written on the floor of this hallway is '#2'. \n To the North is [Hallway – Section 1]. \n To the South is [Hallway – Section 3]. \n To the West is a door with a sign that reads: \n 'Prototype Workshop' \n To the East is a door with a sign that reads: \n 'Programming Lab'")

def fancyDes():
    print("[Hallway – Section 2] \n Written on the floor of this hallway is '#2'. \n It's written in a rounded font, a lot different than the way '#1' is written, and is filled in with multiple colors as opposed to just White. \n To the North is [Hallway – Section 1]. \n To the South is [Hallway – Section 3]. \n To the West is [Prototype Workshop]. \n To the East is [Programming Lab].")

def movewest():
    utils.x = utils.x + 1
    if utils.advanced:
      PrintingLab.fancyDes()
    else:
      PrintingLab.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into 3D Printing lab!")

def movenorth():
    utils.y = utils.y - 1
    Hallway1.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway#1.")

def movesouth():
    utils.y = utils.y + 1
    Hallway3.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're  moving into Hallway#3.")

def moveeast():
    utils.x = utils.x - 1
    if utils.advanced:
      ProgrammingLab.fancyDes()
    else:
      ProgrammingLab.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Programming Lab.")

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