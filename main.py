import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)



 
pygame.init()
pygame.font.init()
pygame.display.init()

RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SIZE = (800, 500)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500 


screen = pygame.display.set_mode(SIZE)


INTRO = 1
VIEW_RECORD = 2
MODIFY_RECORD = 3
ADD_RECORD = 4
DELETE_RECORD = 5
VIEW_REPORT = 6
EXIT = 7
WRITE_BACK = 8



nbaFile = open("nba.dat","r")
lines = []
while True:
  nba_line = nbaFile.readline()
  nba_line = nba_line.rstrip("\n") 
  nbaSplit = nba_line.split(",")
  if nba_line=="": 
    break
  lines.append(nbaSplit)

nbaFile.close()

#define intro function 
global currentState
def intro():
  running = True


  while running:
    screen.fill(WHITE)
    font = pygame.font.SysFont("Arial",30)
    #title
    text_title = font.render("NBA Top Scorers 2022-23",0,RED)
    screen.blit(text_title,(210,30))
    #creating button, rectangle, and text for view the record

    text_view = font.render("View the Data",0,RED)
    button_view = [200,100,400,40]
    pygame.draw.rect(screen,BLACK,(200,100,400,40),0)
    screen.blit(text_view,(300,100))
  
    #creating button, rectangle, and text for modify the record
    text_modify = font.render("Modify the Data",0,RED)
    button_modify = [200,170,400,40] #modify button dimensions
    pygame.draw.rect(screen,BLACK,(200,170,400,40),0)
    screen.blit(text_modify,(285,170))
  
    #creating button, rectangle, and text for add a record
    text_add = font.render("Add a Record",0,RED)
    button_add = [200,240,400,40] #add button dimensions
    pygame.draw.rect(screen,BLACK,(200,240,400,40),0)
    screen.blit(text_add,(300,240))
  
    #creating button, rectangle, and text for delete a record
    text_delete = font.render("Delete a Record",0,RED)
    button_delete = [200,310,400,40] #delete button dimensions
    pygame.draw.rect(screen,BLACK,(200,310,400,40),0)
    screen.blit(text_delete,(285,310))
  
    #creating button, rectangle, and text for view reports
    text_report = font.render("View Reports",0,RED)
    button_report = [200,380,400,40] #report button dimensions
    pygame.draw.rect(screen,BLACK,(200,380,400,40),0)
    screen.blit(text_report,(300,380))
  
    #creating button, rectangle, and text for exit program
    text_exit = font.render("Exit Program",0,RED)
    button_exit = [200,450,400,40] #exit button dimensions
    pygame.draw.rect(screen,BLACK,(200,450,400,40),0)
    screen.blit(text_exit,(300,450))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          # pygame.quit()
          running = False
  
        #button command when user clicks "View the Data" button
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          #checking if mousebuttondown is within the dimensions of the button
          if button_view[0] <= x <= button_view[0] + 400 and button_view[1] <= y <= button_view[1] + 40:
            screen.fill(WHITE)
            currentState = VIEW_RECORD
            currentState = view()

        #button command when user clicks "Modify the Data" button
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          #checking if mousebuttondown is within the dimensions of the button
          if button_modify[0] <= x <= button_modify[0] + 400 and button_modify[1] <= y <= button_modify[1] + 40:
  
            screen.fill(WHITE)
            currentState = MODIFY_RECORD
            currentState = modify()
  
         #button command when user clicks "Add a Record" button
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          #checking if mousebuttondown is within the dimensions of the button
          if button_add[0] <= x <= button_add[0] + 400 and button_add[1] <= y <= button_add[1] + 40:
       
            screen.fill(WHITE)
            currentState = ADD_RECORD
            currentState = add()
  
        #button command when user clicks "Delete a Record" button
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          #checking if mousebuttondown is within the dimensions of the button
          if button_delete[0] <= x <= button_delete[0] + 400 and button_delete[1] <= y <= button_delete[1] + 40:
           
            screen.fill(WHITE)
            currentState = DELETE_RECORD
            currentState = delete()
  
        #button command when user clicks "View Reports" button
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          #checking if mousebuttondown is within the dimensions of the button
          if button_report[0] <= x <= button_report[0] + 400 and button_report[1] <= y <= button_report[1] + 40:
        
            screen.fill(WHITE)
            currentState = VIEW_REPORT
            currentState = report()
  
        #button command when user clicks "Exit Program" button
        if event.type == pygame.MOUSEBUTTONDOWN:
          x,y = pygame.mouse.get_pos()
          #checking if mousebuttondown is within the dimensions of the button
          if button_exit[0] <= x <= button_exit[0] + 400 and button_exit[1] <= y <= button_exit[1] + 40:
            currentState = EXIT
            currentState = exit()
          
    
    pygame.display.flip()


#set currentState to global variable
global currentState
# defining view record
def view():
  #print headers 
  print("\nPlayer ID\tFirst Name\tLast Name\tTeam\tPosition\tPPG\t\tAge")
  #for loop prints data table
  for player in lines:
    print("%9s\t%-10s\t%-9s\t%-4s\t%-8s\t%-3s\t%3s" %(player[0],player[1],player[2],player[3],player[4],player[5],player[6])) 
  print ("\n")
  while True:
    for event in pygame.event.get():
      pygame.draw.rect(screen,BLACK,(0,0,150,75)) #draw back button
      font = pygame.font.SysFont("Arial",40) #font for back button
      back_button = [0,0,150,75] #dimensions of back button
      back_text = font.render("Back",0,RED)
      screen.blit(back_text,(20,10)) #display text
      pygame.display.flip()
      
      x,y = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if back_button[0] <= x <= back_button[0] + 150 and back_button[1] <= y <= back_button[1] + 75:
          #call intro function if user presses back_button
          intro()
    
          
        
      

#defining modify record
def modify():
  
  #prompt user to enter player id of the record they want to modify
  while True:
    modify_input = input("\nPlease enter the Player's ID for the record you want to modify: ")
    #error checking, if user input is an integer
    if modify_input.isdigit() == True:
      for player in lines:
        #checking each player ID, if input == player ID
          if int(modify_input) == int(player[0]):
            list_change = player #store player list in list_change
            print ("1. Player ID")
            print ("2. First Name")
            print ("3. Last Name")
            print ("4. Team")
            print ("5. Position")
            print ("6. PPG")
            print ("7. Age")
            
           
            #prompt user to enter modified field #
            modify_field = int(input("Please enter the number corresponding to the field you would like to modify: "))

            
            #checking if user input = 1
            if modify_field == 1:
              while True:
                #prompt user to input modified player ID
                modify_ID = input("Please enter the modified information for the desired field: ")
                #error checking to check if input is a digit
                if modify_ID.isdigit() == False: 
                  print("Error, please enter valid integer(s) for ID.")
                #error checking to check if input is > than 9 characters
                elif len(modify_ID) > 9:
                  print("Please enter a shorter Player ID.")
                else:
                  #replace player at index 0 (player ID) with desired user input
                  player[0] = modify_ID
                  #function call to write back the data
                  writeback()
                  return currentState
            
            elif modify_field == 2:
              while True:
                #prompt user to enter modified first name
                modify_Firstname = input("Please enter the modified information for the desired field: ")
                #error checking, if input is a digit
                if modify_Firstname.isdigit() == True:
                  print("Please enter a valid First Name, no digits.")
                #error check, checking if input is > than 10 characters
                elif len(modify_Firstname) > 10:
                  print("Player name too long, choose a shorter First Name.")
                else:
                  player[1] = modify_Firstname #replace player at index 1 with user input
                  writeback()
                  return currentState
            
            elif modify_field == 3:
              while True:
                #prompt user to input modified last name
                modify_Lastname = input("Please enter the modified information for the desired field: ")
                #checking if input is a digit
                if modify_Lastname.isdigit() == True:
                  print("Please enter a valid Last Name, no digits.")
                #error check, checking if input is > than 9 characters
                elif len(modify_Lastname) > 9:
                  print("Player name too long, choose a shorter Last Name.")
                else:
                  player[2] = modify_Lastname #replacing player at index 2 with user input
                  writeback()
                  return currentState


              
            elif modify_field == 4:
              while True:
                #prompt user to enter input for team
                modify_Team = input("Please enter the modified information for the desired field: ")
                #error check, if input is a digit
                if modify_Team.isdigit() == True: 
                  print("Please enter a valid Team Name, no digits.")
                #error check, if user inout is > than 4 digits
                elif len(modify_Team) > 4:
                      print("Team too long, choose a shorter Team.")
                else:
                  player[3] = modify_Team
                  writeback()
                  return currentState


            
            elif modify_field == 5:
              while True:
                #prompt user to enter modified input for position
                modify_Position = input("Please enter the modified information for the desired field: ")
                #error check, if user input is a digit
                if modify_Position.isdigit() == True: 
                  print("Please enter a valid Position Name, no digits.")
                #error check, if user input is > than 9 characters
                elif len(modify_Position) > 9:
                      print("Position too long, choose a shorter Position.")
                else:
                  player[4] = modify_Position #replace index 4 for player with user input
                  writeback()
                  return currentState


              
            elif modify_field == 6:
              #prompt user to enter modified input for PPG
              modify_PPG = input("Please enter the modified information for the PPG to one decimal place (Ex: 12.2): ")
              #replace index 5 for player with user input
              player[5] = modify_PPG 
              writeback()
              return currentState
              
            elif modify_field == 7:
              while True:
                #prompt user to enter modified input for Age
                modify_Age = input("Please enter the modified information for the desired field: ")
                #error check, if user input is a digit
                if modify_Age.isdigit == False:
                  print("Please enter a valid Age.")
                #error checking, if user input is > than 3 characters
                elif len(modify_Age) > 3:
                  print("Please enter a shorter Age.")
                else:
                  #replace index 6 for player with user input
                  player[6] = modify_Age
                  writeback()
                  return currentState
                       
    else:
      print("Please enter a valid Player ID.")

#defining add record
def add():
  print("\n")

  while True:
    #prompt user to enter new player ID for add record
    new_playerid = input("Enter the New Player ID: ")
    #error check, checking if user input = digit
    if new_playerid.isdigit() == False:
      print("Please enter a valid Player ID.")
    else:
      break

  while True:
    #prompt user to enter new first name for add record
    new_firstname = input("Enter the New First Name: ")
    #error check, checking if user input = digit
    if new_firstname.isdigit() == True:
      print("Please enter a string for valid First Name.\n")
      #error check, checking if user input is more than 10 characters, if so while loop continues
    elif len(new_firstname) > 10:
      print("Please enter a shorter First Name.")
    else: 
      break

  while True:
    #prompt user to enter new last name for add record
    new_lastname = input("Enter the New Last Name:")
    #error check, checking if user input = digit
    if new_lastname.isdigit() == True:
      print("Please enter a string for valid First Name.\n")
      #error check, checking if user input is more than 9 characters, if so while loop continues
    elif len(new_lastname) > 9:
      print("Please enter a shorter Last Name. ")
    else: 
      break

  while True:
    #prompt user to enter new team for add record
    new_team = input("Enter the New Team: ")
    #error check, checking if user input = digit
    if new_team.isdigit() == True:
      print("Please enter a string for valid Team.\n")
      #error check, checking if user input is more than 4 characters, if so while loop continues
    elif len(new_team) > 4:
      print("Please enter a shorter Team. ")
    else: 
      break

  while True:
    #prompt user to enter new position for add record
    new_position = input("Enter the New Position: ")
    #error check, checking if user input = digit
    if new_position.isdigit() == True:
      print("Please enter a string for valid Position. \n")
    else:
      break

  #prompt user to input new ppg to one decimal place, example provided for formatting
  new_ppg = input("Enter the New PPG to 1 Decimal Place (ex: 12.2):")

  while True: 
    #prompt user to enter new age for add record
    new_age = input("Enter the New Age: ")
    #error check, checking if user input = digit
    if new_age.isdigit() == False:
      print("Please enter a valid integer(s).\n")
    else:
      break

  new_playerid = int(new_playerid)
  print ("\n")

  #adding inputted fields into list newPlayer
  newPlayer = [new_playerid, new_firstname, new_lastname, new_team, new_position, new_ppg, new_age] 

  lines.append(newPlayer) # appending new record to end of masterlist
  currentState = writeback()
  return currentState
  
  
#defining delete record  
def delete():
  while True:
    #prompt user to enter input for the player ID they would like to delete
    player_delete = input("\nPlease enter the Player ID for the player you would like to delete: ")
    if player_delete.isdigit() == True:
      #error check, checking if user input is a digit
      for player in lines:
        #checking if input equals to player ID
        if int(player_delete) == int(player[0]):
          #removing record corresponding to player ID entered by user
          lines.remove(player)
          currentState = writeback()
          return currentState
    else:
      print("Please enter a valid Player ID.")



#defining view report
def report():

  print("\n")
  
  #report displays # of player's age > 27
  print("Reports:")
  agetotal = 0 #counter variable
  for player in lines:
    if int(player[6]) > 27: 
      agetotal+=1 
  print (agetotal,"Players are older than 27.")

  #report displays # of players with (F) position
  position_F = 0 #counter variable
  for player in lines:
    if player[4] == "f" or player[4] == "F":
      position_F+=1
  print (position_F,"Players play the forward (F) position.")

  #report displays # of players with PPG >= 20
  ppgtotal = 0 #counter variable
  for player in lines:
    if float(player[5]) >= 20:
      ppgtotal +=1
  print (ppgtotal,"Players average 20 or more points per game.")

#printing data table to display stats corresponding to reports
  print("\nPlayer ID\tFirst Name\tLast Name\tTeam\tPosition\tPPG\t\tAge")
    
  for player in lines:
    print("%9s\t%-10s\t%-9s\t%-4s\t%-8s\t%-3s\t%3s" %(player[0],player[1],player[2],player[3],player[4],player[5],player[6]))

  print ("\n")
  running = True
  while running:
    for event in pygame.event.get():
      pygame.draw.rect(screen,BLACK,(0,0,150,75))
      font = pygame.font.SysFont("Arial",40)
      back_button = [0,0,150,75]
      back_text = font.render("Back",0,RED)
      screen.blit(back_text,(20,10))
      pygame.display.flip()
      
      x,y = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if back_button[0] <= x <= back_button[0] + 150 and back_button[1] <= y <= back_button[1] + 75:
          currentState = INTRO
          running = False



  
#defining exit command
def exit():
  print("\nThank you for using our program. Goodbye!")
  
#defining writeback function
def writeback():
  nbaFile = open("nba.dat","w")
    
  for player in lines:
      nbaFile.write("%s,%s,%s,%s,%s,%s,%s\n" %(player[0],player[1],player[2],player[3],player[4],player[5],player[6]))
  nbaFile.close()
  
  while True:
    for event in pygame.event.get():
      pygame.draw.rect(screen,BLACK,(0,0,150,75)) #backbutton rectangle
      font = pygame.font.SysFont("Arial",40) #font for backbutton
      back_button = [0,0,150,75] #dimensions of back button (x,y,w,h)
      back_text = font.render("Back",0,RED) 
      screen.blit(back_text,(20,10))
      pygame.display.flip()
      
      x,y = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if back_button[0] <= x <= back_button[0] + 150 and back_button[1] <= y <= back_button[1] + 75:
          intro()
          



#traffic cop
currentState = INTRO
running = True
while running:
  if currentState == INTRO:
    intro()
  elif currentState == VIEW_RECORD:
    view()
  elif currentState == MODIFY_RECORD:
    modify()
  elif currentState == ADD_RECORD:
    add()
  elif currentState == DELETE_RECORD:
    delete()
  elif currentState == VIEW_REPORT:
    report()  
  elif currentState == EXIT:
    exit()
    running = False
  elif currentState == WRITE_BACK:
    writeback()

pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()