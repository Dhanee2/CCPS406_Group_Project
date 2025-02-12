# -*- coding: utf-8 -*-
"""
Room#24: 3D Printing Lab
"""
import Item as I
import utils
import Hallway2

#print("You're in the 3D Printing Lab.")
filename = 'PrintingLab'
#utils.roomsvisited[24] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
  'terminal':  [terminal1     , None ]    
}

def basicDes():
    print("[3D Printing Lab] \n I walk into a very bright room with plenty of tables and chairs organized all throughout. \n The sun is coming in through the large windows that touch both the ceiling and the floor. \n On each of the tables is a 3D Printer accompanied by clear plastic bins underneath them, containing discarded printing projects. \n At the other end of the room, behind thick walls of glass, sits 3D Printers that are almost as tall as the room itself. \n To the East is the door that leads back into [Hallway - Section 2]")

def fancyDes():
    print("[3D Printing Lab] \n The bright yellow sun is still beaming in through the tall, wall length windows. \n At the other end of the room, the massive 3D Printers are still slowly buzzing away, working on their project. \n In the clear plastic bins below each table, I notice all the differently colored discarded projects; when I first came in here I could have sworn all these pieces were gray… \n To the East is [Hallway - Section 2]")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[18] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway2.basicDes()
            utils.roomsvisited[18] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[18] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway2.fancyDes()
            utils.roomsvisited[18] = 1
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