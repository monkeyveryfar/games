from termcolor import colored
import random

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

  coordsx = 0
  coordsy = 0
  choose = 0
  mineexploded = False

  while mineexploded == False:
  print(new_grid)

  def pick():
  coordsx = int(input("Pick x coordinate:"))
  coordsy = int(input("Pick y coordinate: "))
  choose = input("What do you want to do? (Choose new coordinates = 0, Flag: 1, Dig: 2) ")

  if choose == "0":
    pick()
  elif choose == "1":
    new_grid[coordsx][coordsy] = "F"
    pick()