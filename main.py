#dit is ons project

#dit is onze functie
def start_text():
  print("\nThe Year is 1952. The axis powers have taken over over almost the entire world. Also the continental US has fallen. The only place that is still under the rule of the US army and navy, is Alcatraz. This orison has been fitted with the most advanced weapons of the time. You are a US marine, you wake up in the old cellhouses, which have been transformed into an underground bunker with sleeping facilities. \n ")
  print("If you want to stop you can always type 'q'. Every round you have to choose an action. You only need to type the first letter of the command so if you want to go west for instance you type 'w' and if you want to get something you type 'g'\n")
 
inventory = []

directions = []

seenrooms = [5]

rooms = ["x", "x", "x", ["church", "In this church the old prisoners of fort Alcatraz", "knife"], ["parade ground", "Since this is the last base of the US army, the have here their parades"], ["cellhouse", " In fort Alcatraz there where prisoners. This is the place where the prisoners lived"], ["ruins of wardens house", "Here were the prison guards"], ["restrooms", "You now what they do here ;)"], ["recreation yard", "In the past this was the place where the prisoners had their free time. Nowadays it is a place for soldiers in their spare time"], ["Army ground", "Here does the army has its parades", "binoculars"], ["cummunication center", "To make sure the communication of all the troops of the US military is good, they built this building", "Telephone"], ["dock", "This dock houses all the weaponry of the us navy."], ["pool", "Here the soldiers go to unwind.", "torch"], ["trainingscamp", "Here, the soldiers train for 8 hours a day.", "gun"], ["boat", "Here, the soldiers go out for reconnaissance"], "x", "x", "x"]
 
directions = {
  "e"or"E"  : "east",
  "s"or"S"  : "south",
  "w"or"W"  : "west",
  "n"or"N"  : "north",
  "g"or"G"  : "get"
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

  if len(rooms[roomnumber]) == 3:
    print("\nYou see a %s you can get it by chosing 'g'" % rooms[roomnumber][2])

  print("\nYou have %s in inventory" % inventory)

  print("You can choose:")
  print(directions)

  chosendirection = input("enter your way: ")



  if chosendirection == "q":
    print("\nWhy are you leaving us %s? :'(" % name)
    print("exiting")
    raise SystemExit(0)

  if chosendirection == "r":
    print("restarting")
  
  
  
  print(chosendirection)
  
  if chosendirection == "g" or chosendirection == "G":
    inventory.append(weapon)
    print("You got the %s" %weapon)
    del rooms[roomnumber][2]

  if (chosendirection not in directions) and (chosendirection.lower() not in directions):
   if chosendirection == "w" or chosendirection == "W":
     print("\nyou can not go west\n")
   elif chosendirection == "n" or chosendirection == "N":
      print("\nyou can not go north\n")
   elif chosendirection == "s" or chosendirection == "S":
    print("\nyou can not go south\n")
   elif chosendirection == "e" or chosendirection == "E":
     print("\nyou can not go east\n")
   else:
      print("\nThis direction is not available\n")
      continue
        
  if chosendirection == "w" or chosendirection == "W":
    roomnumber = roomnumber - 1
    print("\nGoing west")

  if chosendirection == "e" or chosendirection == "E":
    roomnumber = roomnumber + 1
    print("\nGoing east")

  if chosendirection == "n" or chosendirection == "N":
    roomnumber = roomnumber - 3
    print("\nGoing north")

  if chosendirection == "s" or chosendirection == "S":
    roomnumber = roomnumber + 3
    print("\nGoing south")



 #Dit is de extra opdracht. Alleen als je de eerste keer in een kamer ben krijg je de roominfo
  if roomnumber in seenrooms:
    text = name + (", you have reached the %s. " % rooms[roomnumber][0])
  else:
    text = name + (", you have reached the %s. " % rooms[roomnumber][0]) + (rooms[roomnumber][1])
    seenrooms.append(roomnumber)


  print(text)


