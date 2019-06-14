#dit is ons project

def start_text():
  print("\nThe Year is 1952. The axis powers have taken over over almost the entire world. Also the continental US has fallen. The only place that is still under the rule of the US army and navy, is Alcatraz. This orison has been fitted with the most advanced weapons of the time. You are a US marine, you wake up in the old cellhouses, which have been transformed into an underground bunker with sleeping facilities. \n ")


directions = []
rooms = ["x", "x", "x", "church", "parade ground", "cellhouse", "ruins of wardens house", "restrooms", "recreation yard", "Army ground", "cummunication center", "dock", "pool", "trainingscamp", "boat" "x", "x", "x"]
 

locationinfo = {
  3  : "This is an old church",
  4  : "Where the army has it's parades",
  5  : "Here are the old cells",
  6  : "This is a room",
  7  : "This is a room",
  8  : "This is a room",
  9  : "This is a room",
  10 : "This is a room",
  11 : "This is a room",
  12 : "This is a room",
  13 : "This is a room",
  14 : "This is a room",
}

directions = {
  "e"or"E"  : "east",
  "s"or"S"  : "south",
  "w"or"W"  : "west",
  "n"or"N"  : "north"
}

roomnumber = 5

start_text()



print("You are in the cellhouse")

name = input("What's your name? ")

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

  print("You can go to:")
  print(directions)

  chosendirection = input("enter your way: ")

  if chosendirection == "q":
    print("exiting")
    raise SystemExit(0)

  if chosendirection == "r":
    print("restarting")
    

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
    print("\ngoing west")

  if chosendirection == "e" or chosendirection == "E":
    roomnumber = roomnumber + 1
    print("\ngoing east")

  if chosendirection == "n" or chosendirection == "N":
    roomnumber = roomnumber - 3
    print("\ngoing north")

  if chosendirection == "s" or chosendirection == "S":
    roomnumber = roomnumber + 3
    print("\ngoing south")

  text = "\nYou have reached the %s. " % rooms[roomnumber] + locationinfo[roomnumber] + "."
  print(text)




