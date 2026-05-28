import random
from termcolor import colored 

b = "b"
c = "c"
s = "s"
d = "d"
a = "a"

b_lives = 5
a_lives = 10
s_lives = 3
d_lives = 2
c_lives = 3

shots = []
tries = 25


#grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#grid[9] = [a, a, a, a, a, 0, 0, 0, 0, 0]
#grid[8] = [a, a, a, a, a, 0, 0, 0, 0, 0]
#grid[7] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#grid[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#grid[5] = [0, 0, 0, 0, b, b, b, b, b, 0]
#grid[4] = [0, 0, s, 0, 0, 0, 0, 0, 0, 0]
#grid[3] = [0, 0, s, 0, 0, d, 0, 0, 0, 0]
#grid[2] = [0, 0, s, 0, 0, d, 0, 0, 0, 0]
#grid[1] = [0, 0, 0, 0, 0, 0, c, c, c, 0]
#grid[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# input:  None
# output: New grid with 'a', 'b', 'c', 'd', 's' ships placed correctly.
#
# Use random() to place the ships in the grid.
def create_grid():
  new_grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[5] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[7] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[8] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  new_grid[9] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  place_ship('a', 5, 2, new_grid)
  place_ship('b', 4, 1, new_grid)
  place_ship('c', 3, 1, new_grid)
  place_ship('s', 3, 1, new_grid)
  place_ship('d', 2, 1, new_grid)
  return(new_grid)

def place_ship(ship, length, width, new_grid):
  ship_placed = False
  tries = 0
  while (not ship_placed):
    tries = tries + 1
    #print('tries: ' + str(tries))
    
    r = random.randint(0, 1)
    
    #print('r: ' + str(r))
    
    if r == 0:                      # horizontal
      x = random.randint(0, 10 - length)
      y = random.randint(0, 10 - width)
      # Check if all squares are empty.
      all_empty = True
      for i in range (length):
        #print(new_grid[x+i][y])
        for j in range (width):
          if new_grid[x + i][y + j] != 0:
            all_empty = False
            break
            
      # If all empty, then put ship there.
      if all_empty == True:  
        for i in range (length):
          for j in range (width):
            new_grid[x + i][y + j] = ship
        ship_placed = True
    
        
    elif r == 1:                    # vertical
      x = random.randint(0, 10 - width)
      y = random.randint(0, 10 - length)
      # Check if all squares are empty.
      all_empty = True
      for i in range (length):
        for j in range (width):
          if new_grid[x + j][y + i] != 0:
            all_empty = False
            break

      # If all empty, then put ship there.
      if all_empty == True:  
        for i in range (length):
          for j in range (width):
            new_grid[x + j][y + i] = ship
        ship_placed = True
    
def print_grid(g):
  a = 10
  z = 10
  for k in range(10):
    z = z - 1
    g_row = g[z]

    a = a - 1
    print(a, end="")
    for i in g_row:
      if i == 0:
        print(colored("~", "blue"), end=" ")
      else:
        print(colored(str(i), "grey"), end=" ")
    print()
  print("  0 1 2 3 4 5 6 7 8 9")
  z = z - 1

g2 = create_grid()
print_grid(g2)

#print_grid(grid)

def add(x, y):
  global shots
  coord = str(x) + "," + str(y)
  shots.append(coord)

def get_xy():
  x = input("Enter the x coordinates: ")
  y = input("Enter the y coordinates: ")
  x = int(x)
  y = int(y)
  return x, y

def hits(grid, x, y): 
  global b_lives
  global s_lives
  global d_lives
  global a_lives
  global c_lives
  global tries
  hit = "Hit!"
  misschek = 0
  xy = 0
  ufired = "You fired at that place already."

  def mappy():
    map = input("Do you want a new copy of the old grid? (Enter yes or no.) ")
    if map == "yes" or map == "YES":
      print_grid(grid)
    elif map == "no" or map == "NO":
      pass
    else:
      print("I don't understand you.")
      mappy()

  def check_ship(ship_type, ship_name, ship_lives, x, y):
    if grid[x][y] == ship_type:
      misschek = 1
      tries = tries + 1
    else:
      ship_lives = ship_lives - 1
      print("Hit")
      if ship_lives == 0:
        print("You sunk my " + ship_name + "!")
    add(x, y)
    mappy()
    
    return ship_lives
    
  if x < 10 and x >= 0 and y < 10 and y >= 0:
    if grid[y][x] == "a":
      a_lives = check_ship('a', 'aircraft carrier', a_lives, x, y)
      misschek = 1
      tries = tries + 1
    else:
      a_lives = a_lives - 1
      print(hit)
      if a_lives == 0:
        print("You sunk my aircraft carrier!")
        add(x, y)
        mappy()
    
    if grid[y][x] == "d":
      misschek = 1
      xy = str(x) + "," + str(y)
      if xy in shots:
        print(ufired)
        tries = tries + 1
      else:
        d_lives = d_lives - 1
        print(hit)
        if d_lives == 0:
          print("You sunk my destroyer!")
          add(x, y)
        mappy()
    if grid[y][x] == "b":
      misschek = 1
      xy = str(x) + "," + str(y)
      if xy in shots:
        print(ufired)
        tries = tries + 1
      else:
        b_lives = b_lives - 1
        print(hit)
      if b_lives == 0:
        print("You sunk my battleship!")
      add(x, y)
      mappy()
    if grid[y][x] == "s":
      misschek = 1
      xy = str(x) + "," + str(y)
      if xy in shots:
        print(ufired)
        tries = tries + 1
      else:
        s_lives = s_lives - 1
        print(hit)
      if s_lives == 0:
        print("You sunk my submarine!")
      add(x, y)
      mappy()
    if grid[y][x] == "c":
      misschek = 1
      xy = str(x) + "," + str(y)
      if xy in shots:
        print(ufired)
        tries = tries + 1
      else:
        c_lives = c_lives - 1
        print(hit)
      if c_lives == 0:
          print("You sunk my cruiser!")
          add(x, y)
          mappy()
  elif misschek == 0:
    xy = str(x) + "," + str(y)
    if xy in shots:
      print("You fired at that place already, but you missed.")
      tries = tries + 1
    else:
      print("You missed!")
    add(x, y)
    mappy()
  else:
    print("I don't understand you.")
    tries = tries + 1
  if a_lives == 0 and b_lives == 0 and c_lives == 0 and d_lives == 0 and s_lives == 0:
    print("You sunk all of my ships!!!😭")
    tries = tries - tries

new_grid = create_grid()
for i in range(tries):
  x, y = get_xy()
  hits(new_grid, x, y)
  tries = tries - 1
  