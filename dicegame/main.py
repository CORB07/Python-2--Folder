#imports
from re import L
import time
import random
import os
#vars
StoredDie = [0,0,0,0,0,0]
DieRoll = [True, True, True, True, True, True]
tempDie = [0,0,0,0,0,0]
Rloss = False
Score = 0


##########
def Roll():
  global DieRoll
  global StoredDie
  global tempDie

  #clear console 
  os.system('clear')

  # reset temp die 
  for a in range (6):
    tempDie[a] = 0
  
  #print stored numbers
  print ("stored dice")
  for i in range(6):
      print ("Die ", i+1 ,": " ,StoredDie[i], )
  #
  
  print ()
  print ()
  print ()
  print ()
  print ("Score: ", Score)




  input ("hit enter to roll the dice.")
  time.sleep(1)
  
  print ("you rolled:")
  
  
  for i in range(6):
    #roll and print dice
    if DieRoll[i]:
      tempDie[i] = random.randint(1,6)
      print ("Die ", i+1 ,": " ,tempDie[i], )
  time.sleep(2)
  Check()
####end of Roll()

def Store():

  global DieRoll
  global StoredDie
  global tempDie
  global Score
  #keep dice
  keepDie = int(input ("Which Die would you like to keep? (enter 0 if none) "))
  if keepDie != 0:

    StoredDie[keepDie - 1] = tempDie[keepDie - 1]
    DieRoll[keepDie - 1] = False
    if StoredDie[keepDie - 1] == 1:
      Score += 100
    elif StoredDie[keepDie - 1] == 5:
      Score += 50
    Store()
  else:
    Roll()
##### end of Store()

def Check():
  global DieRoll
  global StoredDie
  global tempDie
  #check for 1s or 5s
  for i in range (6):
    if tempDie[i] == 1 or tempDie[i] == 5:
      Store()
    else:
      continue
  print ("Round Over, Try again")
  time.sleep(2)
  Reset()
##### end of Check()

def Reset():
  global DieRoll
  global StoredDie
  global Score

  Score = 0
  
  for i in range (6):
    DieRoll[i] = True
    StoredDie[i] = 0
  Roll()
### end of Reset


Roll()
  
    
