directions = []
rooms = ["x", "x", "x", "church", "parade ground", "cellhouse", "ruins of wardens house", "restrooms", "recreation yard", "Army ground", "cummunication center", "dock", "x", "x", "x"]

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
}

directions = {
  "e"  : "east",
  "s"  : "south",
  "w"  : "west",
  "n"  : "north"
}

roomnumber = 5



print("\nThe Year is 1952. The axis powers have taken over over almost the entire world. Also the continental US has fallen. The only place that is still under the rule of the US army and navy, is Alcatraz. This orison has been fitted with the most advanced weapons of the time. You are a US marine, you wake up in the old cellhouses, which have been transformed into an underground bunker with sleeping facilities. \n ")

print("You are in the cellhouse")

while True:
  directions = []

  if roomnumber > 5:
    directions.append("n")

  if roomnumber < 9:
    directions.append("s")

  if not roomnumber % 3 == 0:
    directions.append("w")

  if not (roomnumber - 2) % 3 == 0:
    directions.append("e")

  print("You can go to:")
  print(directions)

  chosendirection = input("enter your way: ")



  if chosendirection not in directions:
    if chosendirection == "w":
      print("\nyou can not go west\n")
    if chosendirection == "n":
      print("\nyou can not go north\n")
    if chosendirection == "s":
      print("\nyou can not go south\n")
    if chosendirection == "e":
      print("\nyou can not go east\n")
    continue
        
  if chosendirection == "w":
    roomnumber = roomnumber - 1
    print("\ngoing west")

  if chosendirection == "e":
    roomnumber = roomnumber + 1
    print("\ngoing east")

  if chosendirection == "n":
    roomnumber = roomnumber - 3
    print("\ngoing north")

  if chosendirection == "s":
    roomnumber = roomnumber + 3
    print("\ngoing south")


  print("\nYou have reached the %s." % rooms[roomnumber])
  print(locationinfo[roomnumber])

