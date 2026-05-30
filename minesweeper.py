import random
import time
#New Change

def create_grid():

  grid = [0, 0, 0, 0, 0, 0, 0, 0]
  grid[7] = ["#", "#", "#", "#", "#", "#", "#", "#"]
  grid[6] = ["#", "#", "#", "#", "#", "#", "#", "#"]
  grid[5] = ["#", "#", "#", "#", "#", "#", "#", "#"]
  grid[4] = ["#", "#", "#", "#", "#", "#", "#", "#"]
  grid[3] = ["#", "#", "#", "#", "#", "#", "#", "#"]
  grid[2] = ["#", "#", "#", "#", "#", "#", "#", "#"]
  grid[1] = ["#", "#", "#", "#", "#", "#", "#", "#"]
  grid[0] = ["#", "#", "#", "#", "#", "#", "#", "#"]

  #grid = [["#"] * 8 for _ in range(8)]
  #grid = "\n".join([" ".join(row) for row in grid])

  mines = int(input("How many mines do you want? "))
  #print(mines)
  #print("Here 1")

  while mines > 64:
    print("Too many mines! Please choose a number less than 64.")
    mines = int(input("How many mines do you want? "))
    #print(mines)
    #print("Here 2")
  for i in range(mines):
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if grid[x][y] == "*":
      i = i - 1
    else:
      grid[x][y] = "*"

  #print("Here 3")
  return grid



def print_grid(grid):
  #print("print_grid 1")
  row = ""
  display_grid = []
  for r in grid:
    row = ""
    for e in r:
      if e == "*":
        row = row + "# "
      else:
        row = row + e + " "
    display_grid.append(row)
      
  print("\n".join(display_grid))
  #print(display_grid)
  #print(grid)

def pick(grid):
  coordsx = 0
  coordsy = 0
  choose = 0
  continuegame = ("")
  mineexploded = False
  
  while mineexploded == False:
    #turns = 0        (commoned out for debug)
    #debug 
    turns = 1
    coordsx = int(input("Pick x coordinate:"))
    coordsy = int(input("Pick y coordinate: "))
    choose = input("What do you want to do? (Choose new coordinates: 0, Flag: 1, Dig: 2) ")
    if turns == 0:
      if grid[coordsx][coordsy] == "*":
        grid[coordsx][coordsy] = "."
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        while grid [x][y] != "*":
          grid[x][y] = "*"
          
      
    else:
      if choose == "0":
        pick()
      elif choose == "1":
        grid[coordsx][coordsy] = "F"
        print_grid(grid)
        pick()
      elif choose == "2":
        if grid[coordsx][coordsy] == "*":
          continuegame = input("You lose!  Try again? (y to contine)")
          mineexploded = True
          if continuegame == "y":
            main()
        else:
          grid[coordsx][coordsy] = "."
          #print("Here before 4")
          minestouching(grid, coordsx, coordsy)
          #print("Here 4")
          print_grid(grid)
          pick()
    turns = turns + 1

    #timer
    #start_time = time.perf_counter()
    #elapsed = time.perf_counter() - start_time
    #time.sleep(0.01)
  
  #print("Time spent: " + str(elapsed) + " seconds")

def minestouching(grid, coordsx, coordsy):
  #print(grid)
  #print("\n".join(grid))
  count = 0
  for i in range(-1, 2):
    #print("i: " + str(i))
    for j in range(-1, 2):
      #print("j: " + str(j))
      if 0 <= coordsx + i < 8 and 0 <= coordsy + j < 8:
        if grid[coordsx + i][coordsy + j] == "*":
          count  = count + 1
  if count > 0:
    #print("blah2")
    grid[coordsx][coordsy] = str(count)
  else:
    grid[coordsx][coordsy] = "."
  #print("blah")
      
  return count
  return grid



def main():
  #print("main 1")
  grid = create_grid()
  #print("main 2")
  print_grid(grid)
  #print("main 3")
  pick(grid)

if __name__ == "__main__":
  main()
