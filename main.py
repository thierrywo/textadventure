#dit is ons project

#dit is onze functie
def start_text():
  print("\nThe Year is 1952. The axis powers have taken over over almost the entire world. Also the continental US has fallen. The only place that is still under the rule of the US army and navy, is Alcatraz. This orison has been fitted with the most advanced weapons of the time. You are a US marine, you wake up in the old cellhouses, which have been transformed into an underground bunker with sleeping facilities. \n ")
  print("If you want to stop you can always type 'q' and if you want to see your invetory type 'i'. Every round you have to choose an action. You only need to type the first letter of the command so if you want to go west for instance you type 'w' and if you want to get something you type 'g'\n")
 
inventory = []

directions = []

seenrooms = [5]

rooms = ["x", "x", "x", ["church", "In this church the old prisoners of fort Alcatraz", "knife"], ["parade ground", "Since this is the last base of the US army, the have here their parades"], ["cellhouse", " In fort Alcatraz there where prisoners. This is the place where the prisoners lived"], ["ruins of wardens house", "Here were the prison guards"], ["restrooms", "You now what they do here ;)"], ["recreation yard", "In the past this was the place where the prisoners had their free time. Nowadays it is a place for soldiers in their spare time"], ["Army ground", "Here does the army has its parades", "binoculars"], ["cummunication center", "To make sure the communication of all the troops of the US military is good, they built this building", "phone"], ["dock", "This dock houses all the weaponry of the us navy."], ["pool", "Here the soldiers go to unwind.", "torch"], ["trainingscamp", "Here, the soldiers train for 8 hours a day.", "gun"], ["boat", "Here, the soldiers go out for reconnaissance"], "x", "x", "x"]
 
objects = {
  "k"  : "knife",
  "t"  : "torch",
  "b"  : "binoculars",
  "p"  : "phone",
  "g"  : "gun"
}

roomnumber = 5



#Nu start de game
start_text()

name = input("What's your name? ")

print("\nYou are in the %s." % (rooms[roomnumber][0]) + (rooms[roomnumber][1]))



while True:

  directions = []

  if roomnumber > 5:
    directions.append("n")

  if roomnumber < 12:
    directions.append("s")

  if not roomnumber % 3 == 0:
    directions.append("w")

  if not (roomnumber - 2) % 3 == 0:
    directions.append("e")

  if len(rooms[roomnumber]) == 3:
   directions.append("g")
   weapon = rooms[roomnumber][2]

  if len(rooms[roomnumber]) >= 3:
    print("You see a %s you can get it by chosing 'g'" % rooms[roomnumber][2])

  if inventory:
    directions.append("d")
  



  print("You can choose:")
  print(directions)

  chosendirection = input("enter your one letter command: ").lower()



  if chosendirection == "q":
    print("\nWhy are you leaving us %s? :'(" % name)
    print("exiting")
    raise SystemExit(0)

  if chosendirection == "r":
    print("restarting")
  
  
  
  
  print(chosendirection)
  
  alreadygotcommand = False

  if (chosendirection == "g") and len(rooms[roomnumber]) == 3:
    inventory.append(weapon)
    print("You got the %s" %weapon)
    del rooms[roomnumber][2]
    alreadygotcommand = True
  elif (chosendirection == "g") and not len(rooms[roomnumber]) >= 3:
    print("There is nothing to get\n")
    alreadygotcommand = True
  elif chosendirection == "i":
    print("\nYou have %s in inventory\n" % inventory)
    alreadygotcommand = True
  elif chosendirection == "d":
    if not inventory:
      print("You don't have inventory to drop")
      alreadygotcommand = True
    else:
      print("You can drop %s. What do you want to drop (type first letter" % inventory)
      dropobject = input("What to drop?").lower()
      inventoryoneletter = []
      for x in range(0, len(inventory)):
        inventoryoneletter.append(inventory[x][0])
      if dropobject in inventoryoneletter:
        print("You dropped %s\n" % objects[dropobject])
        inventory.remove(objects[dropobject])
        rooms[roomnumber].append(objects[dropobject])
      else:
        if len(dropobject) == 1:
         print("\nYou can't drop that\n")
        else:
          print("\nYou have to use just one letter\n")
  elif chosendirection == "w" and not chosendirection in directions:
    print("\nyou can not go west\n")
  elif chosendirection == "n" and not chosendirection in directions:
    print("\nyou can not go north\n")
  elif chosendirection == "s" and not chosendirection in directions:
   print("\nyou can not go south\n")
  elif chosendirection == "e" and not chosendirection in directions:
    print("\nyou can not go east\n")
  elif not chosendirection in directions and not chosendirection in directions:
   print("\nThis direction is not available\n")
   continue
  elif chosendirection == "w":
    roomnumber = roomnumber - 1
    print("\nGoing west\n")
  elif chosendirection == "e":
    roomnumber = roomnumber + 1
    print("\nGoing east\n")
  elif chosendirection == "n":
    roomnumber = roomnumber - 3
    print("\nGoing north\n")
  elif chosendirection == "s":
    roomnumber = roomnumber + 3
    print("\nGoing south\n")



 #Dit is de extra opdracht. Alleen als je de eerste keer in een kamer ben krijg je de roominfo
  if roomnumber in seenrooms:
    text = name + (", you are in the %s. " % rooms[roomnumber][0])
  else:
    text = name + (", you are in the %s. " % rooms[roomnumber][0]) + (rooms[roomnumber][1])
    seenrooms.append(roomnumber)


  print(text)



