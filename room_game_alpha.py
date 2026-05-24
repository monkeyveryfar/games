def roomgame():
  print("This is a room game using your keyboard.")
  print("Please answer in all lowercase letters.")
  dont = ("I don't understand you.")
  exit = ("You have exited the game.")
  inventory = []
  knife = "knife"
  joe = "book about Joe Biden"
  print("You are in a dark room with a door to the west.")
  darkroom = input("What will you do? (Open The Door, to exit the game, type Commit Suicide.) ")
  while darkroom == "open door" or darkroom == "open the door":
    print("You are now in the west room.")
    print("There, you found a knife, a used napkin, a rock, and a book.")
    otherroom = input("What will you do? (Pick up knife, pick up rock, pick up book, pick up used napkin.) ")
    while otherroom == "pick up knife" or otherroom == "knife":
      print("You pick up the knife and put it in your inventory.")
      inventory.append(knife)
      print("You keep walking.  There is another door to the east.")
      notherroom = input("What will you do?(Open Door, Exit Game) ")
      while notherroom == "open door" or "open the door":
        print("You are now in the east room.")
        print("There is a bookshelf there.")
        print("You check out the bookshelf. (There is a book about animals, a book about Joe Biden, and a book about monsters.")
        whatwilldo = input("What will you do? ")
        if whatwilldo == "book about animals" or whatwilldo == "book of animals":
          print("You pick up the book.  The animals in the book come alive and eats you.  You die.")
          retry = input("Retry, Exit ")
          if retry == "retry":
            roomgame()
          if retry == "exit":
            print(exit)
          else:
            print(dont)
        else:
          print(dont)
        if whatwilldo == "book about joe biden" or whatwilldo == "joe biden book" or whatwilldo == "joe biden":
          print("You put the book about Joe Biden in your inventory.")
          inventory.append(joe)
          print("Inventory: " + str(inventory))
          print("There is a door.  You open it.  You are now in the south room. Inside the south room, there is a toilet paper monster.")
          tp = input("What will you do? ")
          if tp == "kill toilet paper monster" or tp == "kill giant toilet paper monster":
            print("You use the knife from you inventory to kill the toilet paper monster.")
            print("You successfully kill the toilet paper monster, but your knife breaks.")
            inventory.remove(knife)
            door = input("There is a door(Open Door, Exit Game). ")
            if door == "open the door" or door == "open door":
              print("Congrats! You survived!")
              print("End of game.")
              break
            elif door == "exit game":
              print(exit)
            else:
              print(dont)
        if whatwilldo == "book about monsters" or whatwilldo == "monsters book":
          print("The monsters in the book come alive and eat you.  You die.")
          retry = input("Retry, Exit")
          if retry == "retry":
            roomgame()
          if retry == "exit":
            print(exit)
          else:
            print(dont)
        else:
          print(dont)
      if otherroom == "used napkin" or otherroom == "pick up used napkin":
        print("The napkin has snot on it.  The snot is poisonious.  You die.")
        retry = input("Retry, Exit ")
        if retry == "retry":
          roomgame()
        if retry == "exit":
          print(exit)
        else:
          print(dont)
    if otherroom == "rock" or otherroom == "pick up rock":
      print("You pick up the rock.  There is poison on the rock.  You die.")
      retry = input("Retry, Exit ")
      if retry == "retry":
        roomgame()
      else:
        print(exit)
    else:
      print(dont)
  if darkroom == "commit suicide":
    print("You died.")
    print(exit)
  else:
    print(dont)
    if otherroom == "book" or otherroom == "pick up book":
      print("The book is alive.  It eats you.  You die.")
      retry = input("Retry, Exit ")
      if retry == "retry":
        roomgame()
      else:
         print(exit)    
    else:
      print(dont)
roomgame()