#Please press F5 to run in Shell - this is the only way to play - sorry!

#!/bin/python3
import time
def showInstructions():
    #print a main menu and the commands
    print('''
Dave's Quest: Act One
=====================

Dave is running late for college, but he needs to grab his stuff before he can go.

Objective: Get to the Bus Stop (via the Front Door) with your lunch, backpack, stationery and books!

Commands:
  go [direction]
  get [item]
  read map - shows valid directions
''')

#print ([currentRoom] direction) to get the room name in a certain direction

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print("Inventory : " + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
 
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other room positions
rooms = {

            'bedroom' : { 'west' : 'Study',
                  'south'  : 'Kitchen',
                  'item' : 'books'
                },        

            'Study' : { 'west' : 'Kitchen',
                  'item' : 'stationery',
                },
                
            'Kitchen' : { 'north'  : 'bedroom',
                  'east' : 'Study',
                  'west' : 'Porch',
                  'item' : 'lunch'
                },
            'Porch' : { 'east' : 'Kitchen',
                  'west' : 'Front Door',
                  'item' : 'backpack'
                },
            'Front Door' : { 'east' : 'Porch'}
         }

#start the player in the bedroom
currentRoom = 'bedroom'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')

#direction = ['north', 'east', 'south', 'west']

#if move == 'print ([currentRoom] direction)':
      #print ([currentRoom] direction)

  if move == 'read map':
    if 'north' in rooms[currentRoom]:
      print('north is valid')
    if 'south' in rooms[currentRoom]:
     print('south is valid')
    if 'east' in rooms[currentRoom]:
      print('east is valid')
    if 'west' in rooms[currentRoom]:
      print('west is valid')

  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  # player wins if they get to the garden with a key and a shield
  if currentRoom == 'Front Door' and 'backpack' in inventory and 'stationery' in inventory and 'lunch' in inventory and 'books' in inventory:
    print('You got to the bus stop...')
    time.sleep(2)
    print ('Dave got to college on time and learned many things about programming... You Win!')
    break
  

