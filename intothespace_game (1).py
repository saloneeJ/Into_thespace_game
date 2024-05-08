#!/usr/bin/env python
# coding: utf-8

# In[2]:


import datetime #1
potion = False 

def create_file(filename):  #2
    try:
        with open(filename, 'w') as f:
            b= datetime.datetime.now().strftime("%B %d, %Y %H:%M:%S")
            str_current_datetime = str(b)
            f.write(str_current_datetime+ P+T+ ' logged into the game \n')
    except IOError:
        print("Error: could not create file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
    except IOError:
        print("Error: could not append to file " + filename)
        
        

import datetime   
def action_performed(func):
  def wrapper(*args, **kwargs):
   action_name = func.__name__
   timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
   print(f'[{timestamp}] Player chose the option: {action_name}')
   return func(*args, **kwargs)
  return wrapper


def Aircraft(): #4
  append_file(filename,P+T+ " is in the Aircraft \n")
  directions = ["left","right","forward"]
  print("You are flying in the space, and can choose to go down any of the four directions. Where would you like to fly the aircraft?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      PlanetB63() #the blue planet is slowly falling into the blackhole -> it will lead to safely landed()
      #and will find a space portal which will lead to the best imaginable habitual planet.
    elif userInput == "right":
      AbandonedAirstation() # will find a potion which will give humans the ability to evolve to higher beings in just seconds.
    elif userInput == "forward":
      PlanetG8X()   #will find the planet is habitual but lies in comet belt so theres a risk
    elif userInput == "backward":
      print("Vast and lifeless space awaits you. ")
      print("You get last chance to play again choose wisely! ")
    else:
      print("Please enter a valid option.")


@action_performed #5
def PlanetB63():
  append_file(filename,P+T+ " Reached PlanetB63 \n")
  directions = ["planet","backward"]
  print("You see a blue planet similar to earth but the planet is near a blackhole.")
  print("You see the planet slowly falling into the massive blackhole. There still can be useful resources available on the planet. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: planet/left/backward")
    userInput = input()
    if userInput == "planet":
      Safely_landed()
    elif userInput == "left":
        print("the aircraft got sucked into the blackhole. Human race is doomed.GAME OVER")
        append_file(filename,P+T+ " and all other huamns got sucked into the blackhole \n")
        break
    elif userInput == "backward":
      Aircraft()
    else:
      print("Please enter a valid option.") 

@action_performed #6
def Safely_landed():
  append_file(filename,P+T+" safely landed on PlanetB63 \n")
  directions = ["torwards portal", "backward","The event horizon","event horizon"]
  print("The aircraft safely landing on PlanetB63")
  print("You see space portal created by higher beings which can lead to anywhere in the universe. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options:towards portal/backward")
    userInput = input()
    if userInput == "towards portal":
      print("To use the portal , you first have to solve a riddle")
      print("THE RIDDLE: I am a black hole’s equivalent of a one-way street. What am I?")
      userInputs = input()
      if userInputs == " The event horizon" or userInputs == "event horizon":
        print("Correct Answer !!")
        print("You travelled through the space portal and landed on the PlanetB77 exact replica of earth! You saved humankind!!")
        print("Thank you for playing the game Captain !!")
        append_file(filename,P+T+ " solved the riddle correctly ! \n")
        append_file(filename,P+T+ " won the game \n")
        break
      else:
        print("You cant use the Portal try again")
    elif userInput == "backward":
      PlanetB63()
    else:
      print("Please enter a valid option")

@action_performed #7
def PlanetG8X():
  append_file(filename,P+T+" is entering planet G8X \n")
  directions = ["planet", "left", "backward"]
  print("You see planet G8X. It is beyond the comet belt.")
  print("You see comet shower everywhere.It is a risk to land on G8X. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: planet/left/backward")
    userInput = input()
    if userInput == "planet":
        print("Multiple comet hit the aircraft. You failed. Human race is doomed.")
        print("Game Over")
        append_file(filename,P+T+" failed to save humanity\n")
        break
    elif userInput == "left":
        print("Vast and lifeless dark space awaits you.")
        print("You Lost")
        append_file(filename,P+T+" Pushed the humanity into extinction \n")
        break
    elif userInput == "backward":
      Aircraft()
    else:
      print("Please enter a valid option")

@action_performed #8
def AbandonedAirstation():
  append_file(filename,P+T+" is approaching abandoned airstation \n")
  directions = ["backward", "forward"]
  global potion
  print("You see a Abandoned Airstation.You need Supplies. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: airstation/backward/forward")
    userInput = input()
    if userInput == "airstation": 
        print("You are exploring airstation. You open one of the door to discover a room full of mystery potion.")
        potion  = True
        append_file(filename, "The whole crew on the aircraft consumed mystry potion \n")
        AdvancedBeings()
        break
    elif userInput == "backward":
        Aircraft()
    elif userInput == "forward":
        print("vast and lifeless space awaits you, you got lost. GAME OVER")
        append_file(filename,P+T+" Pushed the humanity into extinction \n")
        break
    else:
        print("Please enter a valid option")


import random #9
def generate_power():
  potion = ['Super Human Strength', ' Super Human Intellegence', 'super human abilities']
  yield random.choice(potion)


@action_performed #10
def AdvancedBeings():
  append_file(filename, P+T+" encountered aliens \n")
  actions = ["fight", "flee"]
  global potion
  print("An alien spaceship appeared out of nowhere. You can either run or fight it. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
        if potion:
            Mystry_potion = generate_power()
            print("All the humans on aircraft consumed the mystery potion")
            print('The mystery potion gave the ability :',list(Mystry_potion))
            print("It sped up the process of evolution in human beings making them equal to the advanced civilization")
            print("Advanced Humans defeated the aliens")
            print("Due to the evoluation and the advance technology founded in alien spaceship human race is not endangered")
            print('Thanks for playing! Goodbye!')
            append_file(filename,P+T+" won the game by defeating the aliens \n")
            break
        break
    elif userInput == "flee":
        print("As you tried to run away, a neuclear weapon launched by enemy hit your aircraft. EVERYONE IS DEAD")
        print("GAME OVER")
        append_file(filename,P+T+" lost the game \n")
        break
    else:
      print("Please enter a valid option")


if __name__ == "__main__": #11
    while True:
        class PLAYER:
             def __init__(self, Name,Username):
                self.name = Name
                self.username=Username
        print("In the year 2344 with an astrioid size of moon approaching earth, the remaining mankind left earth in search for new home")
        print("However, during the exploration,mankind found itself lost into the space.")
        print("You being the leader can choose to fly the aircraft in multiple directions to find a habitable planet.")
        print("Let's start with your name: ")
        name = input()
        print("Please provide a username of your choice: ")
        username=input()
        p1= PLAYER(name,username)
        P=p1.name
        if len(name)==0 or name.isalpha() == False:
            raise Exception("Do not keep name empty and use alphabets only. ")
        p1=PLAYER(name,username)
        T=p1.username
        if len(username)==0:
            raise Exception("Do not keep name empty.")
        print("Good luck captain" ,name, "!!")
        filename = "log_time.txt"
        create_file(filename)
        print("Welcome to ""INTO THE SPACE"" game!, The future of mankind depends upon you!! ")
        my_list = ["The aircraft is leaving the earth in:",3,2,1]
        iterator = iter(my_list)
        for element in iterator:
            print(element)
        Aircraft()
        break


# In[ ]:




