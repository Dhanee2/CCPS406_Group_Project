import utils
import CreatorOffice
import time

class oriBot:
    def __init__(self):
      self.name = "origamibot"
      self.awake = False
      self.inInventory = False

    def take(self, filename):
        if not self.inInventory:
          if not self.awake:
            print("Oh! It woke up at my touch!")
          self.inInventory = True
          self.awake = True
          utils.inventory[self.name] = filename
          print("I set it on my shoulder. It's hard to tell, but it seems my new little friend is happy to come along for the ride")
        else:
            print("The origami bot is already on my shoulder.")

  #For puzzle 7
    def use(self):
      if utils.x == 5 and utils.y == 3:
        if CreatorOffice.ventOpen == True:
          print("I open a connection with my tiny friend, then put the origami bot in the open vent. It flutters around, then dives in. I can now see what it sees.")
          time.sleep(1)
          print("It scurries along the vents, south, east, and south again")
          time.sleep(1)
          print("It looks down at Dr Omi Yami's office, curiously")
          time.sleep(1)
          print("It hurries along its way East. The vent grates are larger here.")
          time.sleep(1)
          print("Careful to stay out of sight of the guards, it scuttles along to an empty computer")
          time.sleep(1)
          print("Moving carefully up and down the keyboard, it navigates its way to the controls for the electro-magnetic gate around the lab. ")
          time.sleep(1)
          print("With a final button press, the gate is down! The tiny bot hurries back to vents")
          utils.EMgate = False
          time.sleep(3)
          print("The origamibot pops out of the open vent in front of me, and climbs back onto my shoulder.")
        else: 
          print("The little origami bot looks like it wants to squeeze through the vent, but it can't quite fit")
      else:
        print("I'm not quite sure what do with the origami bot here")

    def examine(self):
      if not self.awake:
        print("A small white square with creases running through it. It's hard to believe it can actually move on its own. I nudge it and... oh! It appears to have woken up!")
        self.awake = True
      else: print("A small white square with creases running through it. It folds and unfurls itself to skitter around.")
