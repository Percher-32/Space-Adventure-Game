#!/usr/bin/env python
# coding: utf-8

# # SPACE ADVENTURE

# In[ ]:


import time
import random
import math
import sys
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100%  !important; }</style>"))




Ob_list = []
Ob_list_x = []
Ob_list_y = []
empires = []
planet_names = ["Mentor","Apollo","Ganymede","Penates","Midas","Eurydice","Aquilo","Favonius","Nemesis","Dryads","Iphigenia","Rhe","Satyrs","Rhadamanthus","Merope","Phlegethon","Aegyptus","Pandora","Scylla","Polynices","Eos","Thisbe","nunraunia","xucury","uhiri","droth P9J","vars HZZ","bora DG6","taotis","Duaroid","Intorkon","Clofiner","Dunt","Betpid","Coldbongo","Plotania XI","amogli","baka","sussy","snata","amogos","negadecimal","fyrengl","C6_ligma","The Sacred" ]                                           
alien_names = ["Worn-pans","Klazuc","Blonals","Straato","Adrirans","Catcers-engi","Va'sian","Boseds-pons","Adrbon","Trekruts","Nirqun","Abertoni","Globturian"]
missile_names = ["Midnight Plasma Sphere","Defender's Smoke Shell","Amnesia","Fancy Anti-Matter Launcher","Orbit","Epilogue","Apocalypse"]
ship_names = ["The Amanda","The Raven","The SC Lifebringer","The Rafaela"]
empire_names = ["The Auroria Republic Empire","The Nalorium Empire","The Valaris Empire","The Auroria Republic Empire"]
mission_list = []









class Identification:
    def __init__(self,num):
        self.num = num


class Turn:
    def __init__(self,num):
        self.num = num        
        

IDE = Identification(0)
turn = Turn(0)



def dist(a,b,c,d):
    return abs(round((((a - b) ** 2) + ((c - d) ** 2) ** 0.5)/100))








class Spaceship:
    def __init__(self,name,empire,x,y,thrusters,mechs,energy,money,vx,vy,AI):
        self.empire = empire
        self.x = x
        self.y = y
        self.thrusters = thrusters
        self.mechs = mechs
        self.energy = energy
        self.vx = vx
        self.vy = vy
        self.AI = AI
        Ob_list.append(self)
        Ob_list_x.append(self.x)
        Ob_list_y.append(self.y)
        empires.append(self)
        self.money = money
        self.name = name
            
    
    def run(self,xs,ys,d):
            self.x += (xs - self.x)/d
            self.y += (ys - self.y)/d
            self.energy -= ((((xs/d) ** 2) + ((ys/d) ** 2)) ** 0.5)
            sys.stdout.write(f'position = {round(self.x),round(self.y)}  energy = {self.energy}\r')
            sys.stdout.flush()
      
    def thrust_list(self):
        for i in range(len(self.thrusters)):
            print("")
            print(f"Id {i} = thruster {self.thrusters[i].name} health = {self.thrusters[i].health} ")
            
    def move(self):
        if self.AI == 0:
            print(f"position = ({round(self.x)},{round(self.y)})")
            print("where do you want to go (x)")
            a = int(input())
            print("where do you want to go  (y)")
            b = int(input())
            c = round((abs(self.x - a) + abs(self.y - b)))
            Robx = self.x
            Roby = self.y
            work = 0
            for i in range(len(self.thrusters) - 1):
                if self.thrusters[i].health > 0:
                    work = 1
            
            if work == 1:
                for i in range(c):
                    if self.energy > 0:
                        self.energy -= round((((self.x - a) ** 2) + ((self.y - b) ** 2)) ** 0.5) / 700
                        self.x -= (Robx - a) / c
                        self.y -= (Roby - b) / c
                        sys.stdout.write(f'position = {round(self.x),round(self.y)}  energy = {round(self.energy)} time in journey = {i + 1}  time_needed = {c}  DO NOT INTERRUPT \r')
                        sys.stdout.flush()
                    else:
                        print("")
                        print("")
                        print("You have 0 energy left")
                        time.sleep(0.1)
                        print("Auto stop engaged")
                        time.sleep(0.5)
                        break
            else:
                print("unable to move")
                time.sleep(1)
                print("all thrusters are broken")
                time.sleep(1)
            self.hub()
                    
        else:
            self.vx = self.x - empires[random.randint(0,len(empire) - 1)].x  + random.randint(-500,500)
            self.vy = self.y - empires[random.randint(0,len(empire) - 1)].y  + random.randint(-500,500)
            self.x += self.vx
            self.y += self.vy
            self.energy -= ((((self.vx) ** 2) + ((self.vy) ** 2)) ** 0.5) 
              
        self.hub()
       
    def landinit(self):
        for i in range(len(Ob_list)):
            if type(Ob_list[i]).__name__ == "Planet":
                Ob_list[i].keg()
                print("")
                print(f"Id:{i} = planet name = {Ob_list[i].name} position = ({Ob_list[i].x},{Ob_list[i].y})   recources = {Ob_list[i].resources}  distance = {dist(self.x,Ob_list[i].x,self.y,Ob_list[i].y)}")                        
                print("")
        print("input the id of the planet you want to land on")    
        a = int(input())
        self.land(Ob_list[a])
            
            
    
     
    
    
    def land(self,desired_planet):
        if dist(self.x,desired_planet.x,desired_planet.y,self.y) < 800:
            print("")
            if not dist(self.x,desired_planet.x,desired_planet.y,self.y) < 1:
                sys.stdout.write(f'landing on planet {desired_planet.name}\r')
                sys.stdout.flush()
                time.sleep(0.5)
                sys.stdout.write(f'landing on planet {desired_planet.name}.\r')
                sys.stdout.flush()
                time.sleep(0.5)
                sys.stdout.write(f'landing on planet {desired_planet.name}..\r')
                sys.stdout.flush()
                time.sleep(0.5) 
                sys.stdout.write(f'landing on planet {desired_planet.name}...\r')
                sys.stdout.flush()
                time.sleep(0.5)
                sys.stdout.write(f'landing on planet {desired_planet.name}....\r')
                sys.stdout.flush()
                time.sleep(0.5)
                sys.stdout.write(f'landing on planet {desired_planet.name}.....\r')
                sys.stdout.flush()
                time.sleep(0.5)
                sys.stdout.write(f'landing on planet {desired_planet.name}......\r')
                sys.stdout.flush()
                time.sleep(0.5)
            print("")
            self.x = desired_planet.x
            self.y = desired_planet.y
            print(f"you are now on the planet {desired_planet.name}")
            if desired_planet.life == 0:
                if not desired_planet.empire == self.empire:
                    print("there is no life here")
                    print("press 1 to extract the minerals")
                    print("press 2 to take off")
                    print("press 3 to back into the spaceship")
                    print("press 4 to take over this colony")
                    desired = input()
                    if desired == "1":
                        self.extract(desired_planet)
                    elif desired == "2":
                        self.move()
                    elif desired == "4":
                        self.colonise(desired_planet)
                    else:
                        self.hub()
                else:
                    desired_planet.Do()
                    print("there is no life here")
                    print("press 1 to extract the minerals")
                    print("press 2 to take off")
                    print("press 3 to back into the spaceship")
                    print("press 4 to help this colony")
                    desired = input()
                    if desired == "1":
                        self.extract(desired_planet)
                    elif desired == "2":
                        self.move()
                    elif desired == "4":
                        desired_planet.welp()
                    else:
                        self.hub()
                
            elif desired_planet.life == 1:
                print("")
                print("")
                print("GreEtInGs.")
                time.sleep(1)
                print(f"We ArE ThE {desired_planet.empire} Of ThE PlAnEt {desired_planet.name} ?")
                time.sleep(1)
                print("AnD WE wOnT Let You TaaKe OuR rEsOurCeS")
                time.sleep(0.5)
                print("press 1 to fly away from this wierd planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to go into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
            elif desired_planet.life == 2:
                print("")
                print("")
                print("")
                print(f"oh, guys there's another one trying to invade us {desired_planet.empire}s")
                time.sleep(1.6)
                print(f"lets just let him take over our feeble weak little planet {desired_planet.name}.")
                time.sleep(2)
                print("its not like we need food, shelter or water anyways.")
                time.sleep(2)
                print("we will just have to survive on tonail clippings...")
                time.sleep(2)
                print("its ok, we understand.")
                time.sleep(1)
                print("you just need more unimaginable wealth to statisfy your insatiable greed.")
                time.sleep(2)
                print("press 1 to fly away from this planet")
                print("press 2 to deploy the mechs (not like they said otherwise) ")
                print("or press 3 to go into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
            elif desired_planet.life == 3:
                print("")
                print("")
                print("")
                print("HALT!")
                time.sleep(0.6)
                print(f"who dareth enter our sacred planet {desired_planet.name}?")
                time.sleep(0.6)
                print("Leave. or else...")
                time.sleep(0.5)
                print("press 1 to just do what he said and leave")
                print("press 2 to deploy the mechs")
                print("or press 3 to go into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
            elif desired_planet.life == 4:
                print("")
                print("")
                print("Uh, guys?")
                time.sleep(1)
                print("yeah?")
                time.sleep(1.4)
                print("...we have an intruder.")
                time.sleep(1.5)
                print("oh no.")
                time.sleep(1)
                print("hello, uhh...")
                time.sleep(1)
                print("whatever your name is...")
                time.sleep(2)
                print("could you please leave our frail little planet alone?")
                time.sleep(2)
                print("thanks")
                time.sleep(1)
                print("press 1 to fly away from this planet and give them peace")
                print("press 2 to deploy the mechs and hurt their frail little planet")
                print("or press 3 to go into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()  
                else:
                    self.hub()
                    
                    
                    
                    
            elif desired_planet.life == 5:
                print("")
                print("")
                print("...")
                time.sleep(2)
                print("get off my planet.")
                time.sleep(1)
                print(f"you are not a {desired_planet.empire}ian.")
                time.sleep(1)
                print("press 1 to get off this planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to go into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
                    
            elif desired_planet.life == 6:
                print("")
                print("")
                print("Hello")
                time.sleep(1)
                print(f"welcome to our humble planet, {desired_planet.name}.")
                time.sleep(1)
                print(f"its not much, but it keeps us {desired_planet.empire}ers alive.")
                time.sleep(2)
                print("so, what do you want to do?")
                time.sleep(1)
                print("we can play games here...")
                time.sleep(1)
                print("have sleepovers...")
                time.sleep(1)
                print("truth or dare...")
                time.sleep(1)
                print("go trick or treating...")
                time.sleep(1)
                print("...we even have icecream!")
                time.sleep(0.8)
                print("press 1 to fly away from this planet")
                print("press 2 to deploy the mechs...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...or press 3 to go into the ship")
                dt = input()
                if dt == "1":
                    print("NOO!")
                    time.sleep(1)
                    print("please, dont leave...")
                    time.sleep(1)
                    print(f"us {desired_planet.empire}s dont get many visitors on this side of the universe...")
                    time.sleep(1)
                    self.move()
                elif dt == "2":
                    print("guys, dont worry.")
                    time.sleep(0.5)
                    print("theyre using the mech to protect us.")
                    time.sleep(2)
                    print(f"...right?")
                    time.sleep(0.5)
                    self.mecher()
                else:
                    self.hub()
                
                
            elif desired_planet.life == 7:
                print("")
                print("")
                print("auhdcg a dcacvu ")
                time.sleep(1)
                print(f"<Jvu JYtf fFf {desired_planet.name}")
                time.sleep(1)
                print(f"relaITU (7trF) zouyJHy {desired_planet.empire}?")
                time.sleep(1)
                print("ceajegf aekrfyV jyYTEDCuygw IytrBT FvutRvy rcud djdjddjtr stzsedrtg yhjnbhvg ceias")
                time.sleep(1)
                print("press 1 to fly away from this... odd planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to retreat back into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
                    
                    
            elif desired_planet.life == 9:
                print("")
                print("")
                print("NOOOOO!")
                time.sleep(1)
                print(f"They found us {desired_planet.empire}ians! the SPACE POLICE!")
                time.sleep(1)
                print(f"HOW DID YOU EVEN FIND US HERE? ON {desired_planet.name}?!")
                time.sleep(1)
                print("PLEEEEZE DONT HURT US!")
                time.sleep(1)
                print("Oh, who am i kidding?! THEYRE GONNA KILL US ANYWAYYYS!")
                time.sleep(1)
                print("WWWWWWWWWWWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHAHAHAH!")
                time.sleep(1)
                print("press 1 to fly away from this... odd planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to retreat back into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
                    
                    
            elif desired_planet.life == 10:
                print("")
                print("")
                print("Wait... is that...")
                time.sleep(1)
                print(f"oh my gosh. OH MY GOSH I KNEW IT!")
                time.sleep(1)
                print(f"ALIENS! ON OUR VERY OWN LITTLE PLANET{desired_planet.name}! and IM THE FIRST {desired_planet.empire}IAN TO SEE IT!")
                time.sleep(1)
                print("Jeremy, we talked about this already. there ARE no aliens.")
                time.sleep(1)
                print("Please, go back to sle--")
                time.sleep(1)
                print("WHAT")
                time.sleep(1)
                print("ALIENS? but-- but i thought...")
                time.sleep(1)
                print("OHOHOHOHO! SEE FATHER? YOU THOUGHT I WAS CRAZY.")
                time.sleep(1)
                print("YOU ALL THOUGHT I WAS CRAAAZZZY!!!.")
                time.sleep(1)
                print("hehehehhohohoHAHAHAHAHA!!!")
                time.sleep(1)
                print("press 1 to fly away from this planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to retreat back into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
                    
            elif desired_planet.life == 11:
                print("")
                print("")
                print("Wait... is that...")
                time.sleep(1)
                print(f"oh my gosh. OH MY GOSH!")
                time.sleep(1)
                print(f"The rescue team have come to save me on this stupid planet called {desired_planet.name}")
                time.sleep(1)
                print(f"Please TAKE ME BACK to my fellow {desired_planet.empire}ians")
                time.sleep(1)
                print("ive neen here for...")
                time.sleep(1)
                print("WHAT")
                time.sleep(1)
                print(f"{random.randint(10,4000)} LIGHT YEARS?!")
                time.sleep(1)
                print("That cant be right?!")
                time.sleep(1)
                print("press 1 to fly away from this planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to retreat back into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
                    
            elif desired_planet.life == 12:
                print("")
                print("")
                print("Hi im bob")
                time.sleep(1)
                print(f"welcome to my planet")
                time.sleep(1)
                print(f"Bob's planet")
                time.sleep(1)
                print(f"You got any orange juice for me")
                time.sleep(1)
                print("i would love some right about now")
                time.sleep(1)
                print("or some video games")
                time.sleep(1)
                print(f"i running pretty low on those")
                time.sleep(1)
                print("All i have left is some dumb video game called space aventure")
                time.sleep(1)
                print("press 1 to fly away from this planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to retreat back into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
                    
                    
            elif desired_planet.life == 13:
                print("")
                print("")
                print("JUST TAKE IT!")
                time.sleep(1)
                print(f"I HATE THIS ")
                time.sleep(1)
                print(f"I have to pay {random.randint(100,5000)}% of what i earn just for mortgage")
                time.sleep(1)
                print(f"Dont enve get me startted on POLITICS!!")
                time.sleep(1)
                print("trust i would rather be ENSLAVED")
                time.sleep(1)
                print("than CONTINUE to LIVE HERE")
                time.sleep(1)
                print(f"But despite that the one thing i truly depise is my niegbour")
                time.sleep(1)
                print(f"he is a disgrace to the people of {desired_planet.name}")
                time.sleep(1)
                print(f"please can you destroy him first")
                time.sleep(1)
                print("press 1 to fly away from this planet")
                print("press 2 to deploy the mechs")
                print("or press 3 to retreat back into the ship")
                dt = input()
                if dt == "1":
                    self.move()
                elif dt == "2":
                    self.mecher()
                else:
                    self.hub()
                    
            elif desired_planet.life == 14:
                if not desired_planet in self.visited:
                    bonker = random.randint(40,500)
                    print("")
                    print("")
                    print("HEy there alien dude")
                    time.sleep(1)
                    print(f"I have a deal for you")
                    time.sleep(1)
                    print(f"Ine heard about your little empire")
                    time.sleep(1)
                    print(f"{self.empire} or something like that")
                    time.sleep(1)
                    print("and I know what you really want...")
                    time.sleep(1)
                    print("COLD HARD CASH")
                    time.sleep(1)
                    print(f"so tell you what i got about {bonker}$ with me right now")
                    time.sleep(1)
                    print(f"Ill give you this if you leave us alone")
                    time.sleep(1)
                    print(f"Do we have a deal")
                    time.sleep(1)
                    print("press 1 to fly away from this planet")
                    print("press 2 to deploy the mechs")
                    print("or press 3 to retreat back into the ship")
                    dt = input()
                    if dt == "1":
                        print("ok dude here's your money now LEAVE")
                        self.money += bonker
                        self.visited.append(desired_planet)
                        self.move()
                    elif dt == "2":
                        self.mecher()
                    else:
                        self.hub()    
                else:
                    bonker = random.randint(200,5000)
                    print("")
                    print("")
                    print("HEY I thought we had a deal")
                    time.sleep(1)
                    print(f"No fair")
                    time.sleep(1)
                    print(f"I said leave us alone")
                    time.sleep(1)
                    print(f"You know what ive had enough of this")
                    time.sleep(1)
                    self.energy -= bonker
                    print("(the alien punches your ship)")
                    time.sleep(1)
                    print(f"He did {bonker} damage to your engine")
                    time.sleep(1)
                    print(f"You know have {self.energy} left")
                    time.sleep(1)
                    print("GET")
                    time.sleep(1)
                    print("OFF")
                    time.sleep(1)
                    print("MY")
                    time.sleep(1)
                    print("PLANET")
                    time.sleep(1)
                    print("press 1 to fly away from this planet")
                    print("press 2 to deploy the mechs")
                    print("or press 3 to retreat back into the ship")
                    dt = input()
                    if dt == "1":
                        print("GET OFF")
                        self.move()
                    elif dt == "2":
                        print("I DARE YOU TO SHOOT ME")
                        time.sleep(1)
                        print("I DARE YOU TO TRY")
                        time.sleep(1)
                        self.mecher()
                    else:
                        print("yeah thats right run away in cowardice")
                        self.hub()
                    



            
        else:
            print("too far to land on")
            time.sleep(0.4)
            print(f"your distance to the planet is {dist(self.x,desired_planet.x,self.y,desired_planet.y)}")
            time.sleep(0.4)
            print(f"you have to a distance of atmost 800 to land on it")
            time.sleep(0.4)
            print(f"press enter to go back into the ship")
            uuuuuu = input()
            self.hub()
            
            
    def extract(self,d_p):
        print(f"the planet {d_p.name} has {d_p.resources} resources")
        time.sleep(0.4)
        print("how many resources do you want to take from this planet ")
        want = int(input())
        if not 0 <= want <= d_p.resources:
            print("invalid command")
            self.extract(d_p)
        sys.stdout.write(f'extracting resources from {d_p.name}\r')
        sys.stdout.flush()
        time.sleep(0.78)
        sys.stdout.write(f'extracting resources from {d_p.name}.\r')
        sys.stdout.flush()
        time.sleep(0.78)
        sys.stdout.write(f'extracting resources from {d_p.name}..\r')
        sys.stdout.flush()
        time.sleep(0.78)
        sys.stdout.write(f'extracting resources from {d_p.name}...\r')
        sys.stdout.flush()
        time.sleep(0.78)
        sys.stdout.write(f'extracting resources from {d_p.name}....\r')
        sys.stdout.flush()
        print("")
        time.sleep(0.5)
        self.money += want
        d_p.resources -= want
        print("Ok All done")
        time.sleep(0.5)
        print("press enter to go back to the spaceship")
        ggggg = input()
        self.hub()
        
    def colonise(self,d_p):
        d_p.dominate(self)
        print("press enter to go back to ship")
        print("press 1 to help this colony")
        a = input()
        
        if a == "1":
            d_p.welp()
        else:
            self.hub()
        
        
        
        
        
        
    def hub(self):
        if self.energy > 0:
                for i in range(len(self.mechs)):
                    g = self.mechs[i]
                    g.x = self.x
                    g.y = self.y
                #for i in range(len(Ob_list)):
                    #if type(Ob_list[i]).__name__ == "Robot":
                        #if Ob_list[i].AI == 1:
                            #Ob_list[i].attack() 
                for i in range(len(Ob_list)):
                    if type(Ob_list[i]).__name__ == "Planet":
                        if Ob_list[i].empire == self.empire:
                            Ob_list[i].note()  
                    if type(Ob_list[i]).__name__ == "Missile":
                            Ob_list[i].inch(self)   
                            
                            
                print("")
                print("")
                print("")
                print(f"This is the spaceship centre")
                time.sleep(0.1)
                print(f"stats:")
                time.sleep(0.1)
                print(f"empire = {self.empire}")
                time.sleep(0.1)    
                print(f"position = ({round(self.x)} ,{round(self.y)})")
                time.sleep(0.1)
                print(f"energy = {round(self.energy)} megajoules")
                time.sleep(0.1)
                print(f"money = ${self.money}")
                time.sleep(0.1)
                print(f"number of mechs  = {len(self.mechs)}")
                print("")
                print("")
                self.thrust_list()
                time.sleep(0.3)
                print("")
                print("")
                print("")
                print("press 1 to move")
                print("press 2 to go to the map")
                print("press 3 to deploy mechs")
                print("press 4 to land the ship")
                print("press 5 to purchase energy")
                print("press 6 to recharge mechs")
                grand_need = input()
                if grand_need == "1":
                    self.move()
                elif grand_need == "2":
                    self.map()
                elif grand_need == "3":
                    self.mecher()
                elif grand_need == "4":
                    self.landinit()     
                elif grand_need == "5":
                    self.enemon() 
                else:
                    self.recharge() 
                    
        elif self.money > 0:
            print("automatic recharge activated")
            self.recharge()
                
        else:
            print("")
            print("")
            print("")
            print("")
            time.sleep(1)
            print(f"I am sorry to say this but..")
            time.sleep(1)
            print(f"the {self.empire} has fallen")
            time.sleep(1)
            print(f"they have no energy nor money")
            time.sleep(1)
            print(f"and are unable to get any help")
            time.sleep(1)
            print(f"This is the end of {self.empire}.")
            time.sleep(1)
            
            
    def map(self):
        for i in range(len(Ob_list)):
            print("")
            print("")
            print(f"there is a {type(Ob_list[i]).__name__} called {Ob_list[i].name} located at ({Ob_list[i].x},{Ob_list[i].y}) distance = {dist(self.x,Ob_list[i].x,self.y,Ob_list[i].y)}")
        print("press enter to exit")
        usyless = input()
        self.hub()
        
        
    def enemon(self):
        print("")
        print("")
        print(f"$money = {self.money}")
        print(f"energy = {self.energy} megajoules")
        print("how much money are you going to spend on energy")
        demand = int(input())
        
        if not 0 <= demand <= self.money:
            print("invalid request")
            time.sleep(0.5)
            print("try again")
            time.sleep(0.5)
            self.enemon()
            
        self.money -= demand
        self.energy += demand * 10
        time.sleep(0.5)
        print("Okedoke")
        time.sleep(1)
        print(f"you now have {round(self.energy)} megajoules of energy stored up")
        self.hub()    
        
    def mecher(self):
        for i in range(len(self.mechs)):
            g = self.mechs[i]
            print("")
            print(f"Id {i} = {g.name}  energy = {g.energy}")
            print("")
            g.empire = self.empire
            g.x = self.x
            g.y = self.y
        print("")
        print("Input the id of the mech that you want to use")
        mech_to_use = int(input())
        self.mechs[mech_to_use].attack()
        self.hub()  
            
    def recharge(self):
        for i in range(len(self.mechs)):
            g = self.mechs[i]
            print("")
            print("")
            print(f"Id {i} = {g.name}  energy = {g.energy}")
            g.x = self.x
            g.y = self.y
        print("")
        print("")
        print("Input the id of the mech that you want to recharge")
        mech_to_use = int(input())
        print("how much energy do you want to put into the mech (max = 10000)")
        amounted = int(input())
        if 0 <= amounted <= self.energy:
            self.mechs[mech_to_use].energy += amounted
            self.energy -= amounted
        self.hub()  
            
            
            
class Thruster:
    def __init__(self,power,health,name):
        self.power = power/100000
        self.health = health
        self.name = name
      
    
    
    
class Planet:
    def __init__(self):
        self.name = planet_names[random.randint(0,len(planet_names) - 1)] + " " + planet_names[random.randint(0,len(planet_names) - 1)]
        self.x = random.randint(-6000,6000)
        self.y = random.randint(-6000,6000)
        self.resources = random.randint(10,10000)
        Ob_list.append(self)
        Ob_list_x.append(self.x)
        Ob_list_y.append(self.y)
        self.life = random.randint(0,14)
        self.health = 100
        self.change = 0
        if self.life == 0:
            self.empire = "none"
        else:
            self.empire = alien_names[random.randint(0,len(alien_names) - 1)] + " " + alien_names[random.randint(0,len(alien_names) - 1)]
          
        
    def info(self):
        print(f"planet ID:{self.planet_id} = {self.name}    position = ({self.x},{self.y})   recources = {self.resources}")
        
    def keg(self):
            if self.resources == 0:
                pass
            
    def dominate(self,overlords):
        self.lod = overlords
        self.change = 1
        self.empire = self.lod.empire
        print(f"the planet {self.name} has just been colonised by {self.lod.empire}")
        self.water = random.randint(20,50)
        self.food = random.randint(20,50)
        self.entertainment = random.randint(20,50)
        time.sleep(0.6)
        print(f"this planet has {self.food} food,{self.water} water and {self.entertainment} entertainment for its inhabitants")
        
        
    def Do(self):
        if  0 <= self.water <= 10:
            print("we are soo thirsty here")
            time.sleep(1)
            print("please just give us water")
        elif  10 <= self.water <= 50:
            print("we are pretty thirsty here")
            time.sleep(1)
            print("could do with some more water though")
            time.sleep(1)
            print("were close to running out")
        else:
            print("we have no problems with water ")
        
        time.sleep(1)
            
        if  0 <= self.food <= 10:
            print("I NEED FOOD")
            time.sleep(1)
            print("WE ARE SUFFERING FROM HUNGER")
            time.sleep(1)
            print("IVE FORGOTTEN HOW TO EAT")
        elif  10 <= self.water <= 50:
            print("")
            time.sleep(1)
            print("i pwetty hungr riht now")
            time.sleep(1)
            print("almost out of fud")
        else:
            print("we have no problems with food")
            
        time.sleep(1)
            
        if  0 <= self.entertainment <= 10:
            print("Every Single Day its the SAME DANG THING")
            time.sleep(1)
            print("Wake up")
            time.sleep(1)
            print("Work")
            time.sleep(1)
            print("and Sleep")
            time.sleep(1)
            print("We NEED something fun to do Please")
        elif  10 <= self.water <= 50:
            print("")
            time.sleep(1)
            print("we get pretty bored around here")
            time.sleep(1)
            print("we could do with a few games or movies around here")
        else:
            print("we have no problems with entertainment")
            
    def note(self):
        prof = ((self.water * self.food)/100 + self.entertainment)
        print("")
        print("")
        print(f"your colony on planet {self.name} has made you ${prof}")
        self.lod.money += prof
        if self.food > 0:
            self.food -= 5
        if self.water > 0:
            self.water -= 10
        if self.entertainment > 0:
            self.entertainment -= 10
        
        
    def welp(self):
        print("press 1 to send water")
        print("press 2 to send food")
        print("press 3 to send entertainmet")
        otu = input()
        
        print(f"you have ${self.lod.money}")
        if otu == "1":
            print("how much money are you going to spend on this delivery?")
            mon = int(input())
            if not 0 <= mon <= self.lod.money:
                print("Invalid amount")
            self.water += mon/100
            self.lod.money -= mon
            print(f"this colony now has {self.water}kg of water")
                
            
            
        elif otu == "2":
            print("how much money are you going to spend on this delivery?")
            mon = int(input())
            if not 0 <= mon <= self.lod.money:
                print("Invalid amount")
            self.food += mon/200
            self.lod.money -= mon
            print(f"this colony now has {self.food}kg of food")
        
        else:
            print("how much money are you going to spend on this delivery?")
            mon = int(input())
            if not 0 <= mon <= self.lod.money:
                print("Invalid amount")
            self.entertainment += mon/200
            self.lod.money -= mon
            print(f"this colony now has {self.entertainment} entertainment")
            
        print("press enter to continue")
        print("press 1 to go back to the ship")
        a = input()
        if a == "1":
            self.lod.hub()
        else:
            self.welp()
        
    
          

        
        
        
        
        
        
        
class Missile:
    def __init__(self):
        self.x = random.randint(-6000,6000)
        self.y = random.randint(-6000,6000)
        self.health = random.randint(20,70)
        Ob_list.append(self)
        Ob_list_x.append(self.x)
        Ob_list_y.append(self.y)
        self.empire = "delta"
        self.speed = random.randint(10,100)
        self.name = missile_names[random.randint(0,len(missile_names) - 1)] + " " + missile_names[random.randint(0,len(missile_names) - 1)]
        
    def inch(self,em):
        if self.x - em.x > 0:
            self.x -= self.speed
        else:
            self.x += self.speed
        if self.y - em.y > 0:
            self.y -= self.speed
        else:
            self.y += self.speed
            
        if dist(self.x,em.x,self.y,em.y) < 300:
            print("")
            time.sleep(0.1)
            print("")
            time.sleep(0.1)
            print("Warning!")
            time.sleep(0.1)
            print("")
            time.sleep(0.1)
            print("")
            time.sleep(0.1)
            print("Warning!")
            time.sleep(0.1)
            print("")
            time.sleep(0.1)
            print("")
            time.sleep(0.1)
            print(f"WARNING! There is a missile on course to {em.name}  {dist(self.x,em.x,self.y,em.y)}km away from you! ")
        
        
        if dist(self.x,em.x,self.y,em.y) < 100:
            print("")
            print("")
            print("")
            print(f"BOOM")
            time.sleep(0.6)
            print(f"The missile named {self.name} has hit you")
            em.energy -= self.speed * 90
            print(f"you now have {em.energy} megajoules of energy stored up")
            self.x = random.randint(-9000,9000)
            self.y = random.randint(-9000,9000)
            self.health = random.randint(20,70)
            Ob_list.append(self)
            Ob_list_x.append(self.x)
            Ob_list_y.append(self.y)
            self.empire = "delta"
            self.speed = random.randint(50,200)
            self.name = missile_names[random.randint(0,len(missile_names) - 1)] + " " + missile_names[random.randint(0,len(missile_names) - 1)]
            
        if self.health < 1:
            self.x = random.randint(-9000,9000)
            self.y = random.randint(-9000,9000)
            self.health = random.randint(20,70)
            Ob_list.append(self)
            Ob_list_x.append(self.x)
            Ob_list_y.append(self.y)
            self.empire = "delta"
            self.speed = random.randint(50,200)
            self.name = missile_names[random.randint(0,len(missile_names) - 1)] + " " + missile_names[random.randint(0,len(missile_names) - 1)]
            
    
        



class Robot:
    def __init__(self,name,head,chest,arm,leg,energy,x,y,AI,empire):
        self.name = name
        self.head = head
        self.chest = chest
        self.arm = arm
        self.leg = leg   
        self.energy = energy
        self.x = x
        self.y = y
        self.AI = AI
        self.empire = empire
        Ob_list.append(self)
        Ob_list_x.append(self.x)
        Ob_list_y.append(self.y)
        
    
    def info(self):
        print("")
        print("")
        print(f"Mech name = {self.name}")
        print("")
        print(f"Mech energy = {self.energy}")
        print("")
        print(f"Mech position = ({self.x}, {self.y})")
        print("")
        print(f"head functionality = {self.head.status}%")
        print("")
        print(f"chest functionality = {self.chest.status}%")
        print("")
        print(f"arm functionality = {self.arm.status}%")
        print("")
        print(f"leg functionality = {self.leg.status}%")
        print("")
        self.head.Attacked()
        self.chest.Attacked()
        self.arm.Attacked()
        self.leg.Attacked()
        
    
    def attack(self):
        battery = self.head.status + self.chest.status + self.arm.status + self.leg.status
        if self.energy < 10000:
            if self.energy > 0:
                if battery > 0:
                    if self.AI == 0:
                        time.sleep(0.6)
                        print("")
                        print("")
                        print("")
                        print(f"Mech Name: {self.name}")
                        time.sleep(0.6)
                        print("")
                        print("")
                        print(f"{self.name} has {self.energy} megajoules of energy")
                        print("")
                        print("")
                        time.sleep(0.6)
                        print(f"{self.name}'s position: ({self.x}, {self.y})")
                        print("")
                        print("")
                        time.sleep(0.6)
                        print(f"head functionality = {self.head.status}%")
                        print("")
                        print(f"chest functionality = {self.chest.status}%")
                        print("")
                        print(f"arm functionality = {self.arm.status}%")
                        print("")
                        print(f"leg functionality = {self.leg.status}%")
                        print("")
                        print("")
                        print("")
                        print("")



                    if self.AI == 0:
                        for i in range(len(Ob_list)):
                            print("")
                            print(f"Id:{i} = {Ob_list[i].name}  Empire = {Ob_list[i].empire}")

                        print("")
                        print("")
                        print("")
                        time.sleep(0.6)
                        print("what is the Id of the Object that you want to attack")

                    if self.AI == 0:
                        pref_robot_ID = int(input())
                    else:
                        pref_robot_ID = random.randint(0,len(Ob_list) - 1)
                            


                    if 0 <= pref_robot_ID <= len(Ob_list) - 1:
                        pref = Ob_list[pref_robot_ID]
                        self.distance = (((self.x - pref.x) ** 2) + ((self.y - pref.y) ** 2)) ** 0.5
                        print("")
                        print("")
                        print("")
                        if self.AI == 0:
                            time.sleep(0.6)
                            print(f"Your opponent's name is {pref.name}")
                            print("")
                            time.sleep(0.6)
                            print(f"opponent position = ({pref.x}, {pref.y})")
                            print("")
                            time.sleep(0.6)
                            print(f"Distance = {self.distance} ")
                    else:
                        print("sorry thats not an available ID. try again")
                        time.sleep(1)
                        self.attack()

                    time.sleep(0.6)


                    if self.AI == 0:
                        if self.head.status > 0:
                            print("press 1 for HEAD attacks")
                        else:
                            print("Your HEAD is damaged you are unable to use any attacks here")

                        print("")
                        print("")
                        print("")    
                        if self.chest.status > 0:    
                            print("press 2 for CHEST attacks")
                        else:
                            print("Your CHEST is damaged you are unable to use any attacks here")

                        print("")
                        print("")
                        print("")    
                        if self.arm.status > 0:
                            print("press 3 for ARM attacks") 
                        else:
                            print("Your ARM is damaged you are unable to use any attacks here")

                        print("")
                        print("")
                        print("")
                        if self.leg.status > 0:
                            print("press 4 for LEG attacks") 
                        else:
                            print("Your LEG is damaged you are unable to use any attacks here")

                        body_part = int(input())

                    else:
                        body_part = random.randint(1,4)

                    if body_part == 1:
                        if self.head.status > 0:
                            self.head.mattack(self,self.distance,pref,self.AI)
                        else:
                            if self.AI == 0:
                                print("sorry you cant use this module because its fully damaged")
                            self.attack()

                    elif body_part == 2:
                        if self.chest.status > 0:
                            self.chest.mattack(self,self.distance,pref,self.AI)
                        else:
                            if self.AI == 0:
                                print("sorry you cant use this module because its fully damaged")
                            self.attack()

                    elif body_part == 3:
                        if self.arm.status > 0:
                            self.arm.mattack(self,self.distance,pref,self.AI)
                        else:
                            if self.AI == 0:
                                print("sorry you cant use this module because its fully damaged")
                            self.attack()

                    elif body_part == 4:
                        if self.leg.status > 0:
                            self.leg.mattack(self,self.distance,pref,self.AI)
                        else:
                            if self.AI == 0:
                                print("sorry you cant use this module because its fully damaged")
                            self.attack()

                    else:
                        if self.AI == 0:
                            print("sorry thats not an available number. try again")
                        self.attack()
                else:
                    print("All limbs are dysfunctional")
                    
            else:
                print("This mech has no more energy left")
                
        else:
            print("OVERLOAD TOO MUCH ENERGY")


    def Checkup(self,AI):
        if AI == 0:
            print("")
            print("")
            print("")
            if self.head.status > 0:
                print(f"press 1 to attack the HEAD, which has a functionallity of {self.head.status}%")
            else:
                print(f"{self.name}'s HEAD alredy damaged")

            print("")
            print("")
            print("")    
            if self.chest.status >  0:    
                print(f"press 2 to attack the CHEST, which has a functionallity of {self.chest.status}%")
            else:
                print(f"{self.name}'s CHEST is already damaged")

            print("")
            print("")
            print("")    
            if self.arm.status > 0:
                print(f"press 3 to attack the ARM, which has a functionallity of {self.arm.status}%") 
            else:
                print(f"{self.name}'s ARM is already damaged")

            print("")
            print("")
            print("")
            if self.leg.status > 0:
                print(f"press 4 to attack the LEG, which has a functionallity of {self.leg.status}%") 
            else:
                print(f"{self.name}'s LEG is already damaged")
            
            
            
class Module:
    def __init__(self,part,status,attacks):
        self.part = part
        self.status = status
        self.attacks = attacks
        

    def mattack(self,robot_name,disty,pref_r,AI):
        if AI == 0:
            time.sleep(1)
            print("")
            print("")
            print("")
            print(f"This is the {self.part} module")
            print("")
            if self.status < 20:
                print("")
                print("WARNING")
                print("")
                time.sleep(0.4)
                print("WARNING")
                print("")
                time.sleep(0.4)
                print("WARNING")
                time.sleep(0.4)
                print("low functionallity")
            print(f"functionallity = {self.status}% ")
            print("")
            print("must have over 0% functionality to access")
        
        if AI == 0:
            for i in range(len(self.attacks)):
                print("")
                print("")
                print(f"ID: {i} = {self.attacks[i].state(disty)}")
            
        if AI == 0:
            print("")
            print("")
            print("input the id of the attack that you want to use")
            Idvt = int(input())
        else:    
            Idvt = random.randint(0,len(self.attacks) - 1)
        
        
        if 0 <= Idvt <= (len(self.attacks) - 1):
            self.attacks[Idvt].Use(robot_name,disty,pref_r,self,AI)
        else:
            print("")
            print("")
            print("")
            print("")
            print("")
            print("invalid id try again")
            self.mattack(robot_name,disty,pref_r)
            
    def Attacked(self):
        for i in range(len(self.attacks)):
            print("")
            print("")
            print(f"ID: {i} = {self.attacks[i].stated()}")
            
        
        
class Attacks:
    def __init__(self,name,damage,energy,prob,l_dist,h_dist,Run):
        self.name = name
        self.damage = damage
        self.energy = energy
        self.prob = prob
        self.l_dist = l_dist
        self.h_dist = h_dist
        self.Run = Run
        
    def state(self,Cdist):
        
    
        
        if self.Run == 0:
            if self.l_dist <=  Cdist <= self.h_dist:
                return f"Name:{self.name}    Attack Damage:{self.damage}    Energy used:{self.energy} megajoules    Probability of Success {self.prob}  Range:{self.l_dist} - {self.h_dist}"
                
            else:
                return f"Name:{self.name}    Attack Damage:{self.damage}    Energy used:{self.energy} megajoules    Probability of Success {self.prob}  Range:{self.l_dist} - {self.h_dist}                            UNABLE TO USE THIS ATTACK DUE TO DISTANCE"
            
        else:
            return "fly around"
        
        
        
    def stated(self):
        if self.Run == 0:
                return f"Name:{self.name}    Attack Damage:{self.damage}    Energy used:{self.energy} megajoules    Probability of Success {self.prob}  Range:{self.l_dist} - {self.h_dist}"
        else:
            return "fly around"
        
                
    def Use(self,Rob_obj,Cdist,Op_obj,moduled,AI):
        if self.Run == 0:
            typo = type(Op_obj).__name__
            if typo == "Robot":
                if self.l_dist <=  Cdist <= self.h_dist:
                    Op_obj.Checkup(AI)

                    if AI == 0:
                        limb = int(input())
                    else:
                        limb = random.randint(1,4)


                    if 1 <= limb <= 4:
                        Rob_obj.energy -= self.energy
                        success = random.randint(0,100)

                        if success <= self.prob:
                            if AI == 0:
                                print("BOOM")
                                time.sleep(2)
                                if limb == 1:
                                    Op_obj.head.status -= self.damage
                                    print("")
                                    print("")
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s head with thier {moduled.part}")

                                if limb == 2:
                                    print("")
                                    print("")
                                    Op_obj.chest.status -= self.damage
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s chest with thier {moduled.part}")

                                if limb == 3:
                                    Op_obj.arm.status -= self.damage
                                    print("")
                                    print("")
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s arm with thier {moduled.part}")

                                if limb == 4:
                                    print("")
                                    print("")
                                    Op_obj.leg.status -= self.damage
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s leg with thier {moduled.part}")

                                time.sleep(0.5)
                                print("")
                                print("")
                                print("")
                                print(f"this used {self.energy} from the {Rob_obj.empire} megajoules and did {self.damage} damage to thier opponent {Op_obj.name}")
                            else:   
                                print("BOOM")
                                if limb == 1:
                                    Op_obj.head.status -= self.damage
                                    print("")
                                    print("")
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s head with thier {moduled.part}")

                                if limb == 2:
                                    print("")
                                    print("")
                                    Op_obj.chest.status -= self.damage
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s chest with thier {moduled.part}")

                                if limb == 3:
                                    Op_obj.arm.status -= self.damage
                                    print("")
                                    print("")
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s arm with thier {moduled.part}")

                                if limb == 4:
                                    print("")
                                    print("")
                                    Op_obj.leg.status -= self.damage
                                    print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s leg with thier {moduled.part}")


                        else:
                            print("")
                            print("")
                            print("")
                            print(f"{Rob_obj.name} from the {Rob_obj.empire} tried to use {self.name}")
                            print("")
                            print("")
                            print(f"but {Op_obj.name} from the {Rob_obj.empire} was able to dodge")

                    else:
                            print("invalid limb")
                            time.sleep(0.5)
                            moduled.mattack(Rob_obj,Cdist,Op_obj,AI)

                    time.sleep(1) 
                else:
                    if AI == 0:
                        print("")
                        print("")
                        print("")
                        print(f"Unable to use this attack,You need to have a {Cdist} distance between you and your opponent. You currently have a distance of {Cdist} between you")
                    moduled.mattack(Rob_obj,Cdist,Op_obj,AI)
                    
            elif typo == "Spaceship":
                if AI == 0:
                    print("press 1 to attack the thrusters")
                    print("press 2 to attack the engines")

                if AI == 0:
                    limb = int(input())
                else:
                    limb = random.randint(1,2)


                if 1 <= limb <= 2:
                    Rob_obj.energy -= self.energy
                    success = random.randint(0,100)

                    if success <= self.prob:
                        if AI == 0:
                            if limb == 1:
                                Op_obj.thrust_list(self)
                                print("input the id of the thruster that you want to damage")
                                thruster_to_damage = int(input())
                                if not 0 <= thruster_to_damage <= len(Op_obj.thrusters):
                                    print("INVALID THRUSTER")
                                    self.Use(Rob_obj,Cdist,Op_obj,moduled,AI)
                                print("BOOM")
                                time.sleep(0.6)
                                Op_obj.thrusters[thruster_to_damage].health -= self.damage 
                                print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s thrusters with thier {moduled.part}")

                            if limb == 2:
                                print("")
                                print("")
                                Op_obj.energy -= self.damage
                                print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s engine with thier {moduled.part}")


                            time.sleep(0.5)
                            print("")
                            print("")
                            print("")
                            print(f"this used {self.energy} megajoules and did {self.damage} damage to thier opponent {Op_obj.name}")
                        else:   
                            print("BOOM")
                            if limb == 1:
                                Op_obj.energy -= self.damage
                                print("")
                                print("")
                                thruster_to_damage = random.randint(0,len(Op_obj.thrusters) -1)
                                Op_obj.thrusters[thruster_to_damage].health -= self.damage
                                print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s thrusters with thier {moduled.part}")

                            if limb == 2:
                                print("")
                                print("")
                                Op_obj.energy -= self.damage
                                print(f"{Rob_obj.name} from the {Rob_obj.empire} succesfully used {self.name} on {Op_obj.name}'s engine  with thier {moduled.part} ")
                            print("")
                            print("")
                            print("")    

                    else:
                        print(f"{Rob_obj.name} from the {Rob_obj.empire} was unsuccsesfull in trying to attack the {Op_obj.name} spaceship")
                            
                            
                            
                            
            elif typo == "Planet":
                print("BOOM")
                Rob_obj.energy -= self.energy
                success = random.randint(0,100)
                if success <= self.prob:
                    Op_obj.life = 0
                    print((f"{Rob_obj.name} from the {Rob_obj.empire} empire succesfully used {self.name} on the planet {Op_obj.name} with thier {moduled.part} to exterminate the life there"))
                    
                else:
                    print(f"{Rob_obj.name} from the {Rob_obj.empire} empire was unsuccsesfull in trying to attack the planet {Op_obj.name}")
                    
            elif typo == "Missile":
                print("BOOM")
                Rob_obj.energy -= self.energy
                success = random.randint(0,100)
                
                if success <= self.prob:
                    print((f"{Rob_obj.name} from the {Rob_obj.empire} empire succesfully used {self.name} on the missile {Op_obj.name} with thier {moduled.part} to do {self.damage} to it"))
                    Op_obj.health -= self.damage
                    print(f"This missile now has {Op_obj.health} health left")
                    
                else:
                    print(f"{Rob_obj.name} from the {Rob_obj.empire} empire was unsuccsesfull in trying to attack the planet {Op_obj.name}")
                    
                
                
            
            
            
        else:
            if AI == 0:
                print("")
                print("")
                print(f"you are at X{Rob_obj.x} Y:{Rob_obj.y}")
                print(f"your opponent is at X{Op_obj.x} Y:{Op_obj.y}")
                print("")
                print("")
                print("where would you like to go in x? ")
                desired_x = int(input())
                print("where would you like to go in y?")
                desired_y = int(input())
                c = round((abs(Rob_obj.x - desired_x) + abs(Rob_obj.y - desired_y)))
                Robx = Rob_obj.x
                Roby = Rob_obj.y
                for i in range(c):
                    if Rob_obj.energy > 100:
                        Rob_obj.energy -= round((((Rob_obj.x - desired_x) ** 2) + ((Rob_obj.y - desired_y) ** 2)) ** 0.5) / 10000
                        Rob_obj.x -= (Robx - desired_x) / c
                        Rob_obj.y -= (Roby - desired_y) / c
                        sys.stdout.write(f'position = {round(Rob_obj.x),round(Rob_obj.y)}  energy = {round(Rob_obj.energy)} time in journey = {i}  time_needed = {c}  DO NOT INTERRUPT \r')
                        sys.stdout.flush()
                    else:
                        print("")
                        print("")
                        print("not enough energy to finish trip")
                        time.sleep(0.8)
                        print(f"Mech position = {round(Rob_obj.x),round(Rob_obj.y)}")
                        time.sleep(0.6)
                        break
                
            else:
                desired_x = Op_obj.x + random.randint(-1000,1000)
                desired_y = Op_obj.y + random.randint(-1000,1000)
                Rob_obj.energy -= round((((Rob_obj.x - desired_x) ** 2) + ((Rob_obj.y - desired_x) ** 2)) ** 0.5) / 6
                Rob_obj.x = desired_x
                Rob_obj.y = desired_y
                
                print(f"the mech {Rob_obj.name} from the {Rob_obj.empire} empire moved to position  {round(Rob_obj.x),round(Rob_obj.y)}")
        
                                  
                                  
        if AI == 0:
            print("")
            print("")
            print("press enter to continue")   
            print("press 1 to go back to spaceship") 

            sult = input()

            if not sult == "1":
                Rob_obj.attack()
            else:
                print("RETREATING BACK TO BASE")
        
    
    
    
b = 6
run = Attacks("Move",0,0,0,0,0,1) 


head_01 = Attacks("Head bump",20,50,70,0,50,0)
head_02 = Attacks("Head laser",40,90,80,100,300,0)
head_03 = Attacks("Head missile",30,40,83,20,100,0)
head_04 = Attacks("Head bowling ball",80,30,60,0,100,0)
head_05 = Attacks("Head bash",50,60,80,0,4000,0)
head_06 = Attacks("Headageddon",100,900,70,300,500,0)
head_07 = Attacks("Head spikes",60,50,75,0,600,0)
head_08 = Attacks("Head canon",70,200,90,0,3000,0)
head_09 = Attacks("Headache",100,20,100,0,50,0)
head_10 = Attacks("Head bandage (gives energy)",0,-200,70,0,10000000,0)
head_attacks = [head_01,head_02,head_03,head_04,head_05,head_06,head_07,head_08,head_09,head_10]


chest_01 = Attacks("chest laser",60,100,86,100,300,0)
chest_02 = Attacks("chest bash",40,40,80,0,40,0)
chest_03 = Attacks("chest drones",20,40,99,0,4000,0)
chest_04 = Attacks("chest missile",70,140,80,60,400,0)
chest_05 = Attacks("ultimate chest attack",160,500,70,60,400,0)
chest_06 = Attacks("Belly rub (gives energy)",0,-100,50,0,10000000,0)
chest_07 = Attacks("chest thump",20,10,99,0,300,0)
chest_08 = Attacks("belly button bash",70,70,87,50,500,0)
chest_09 = Attacks("chest o'davey jones",200,50,86,0,50,0)
chest_10 = Attacks("chesterman",50,50,50,0,50,0)
chest_attacks = [chest_01,chest_02,chest_03,chest_04,chest_05,chest_06,chest_07,chest_08,chest_09,chest_10]


arm_01 = Attacks("jab",40,20,80,0,50,0)
arm_02 = Attacks("uppercut",60,40,80,0,50,0)
arm_03 = Attacks("slap",70,70,70,0,400,0)
arm_04 = Attacks("hand missiles",40,40,99,0,4000,0)
arm_05 = Attacks("elbow grease",60,20,80,0,200,0)
arm_06 = Attacks("fist smash",40,40,97,0,1000,0)
arm_07 = Attacks("flick",20,10,100,0,600,0)
arm_08 = Attacks("grab",40,40,80,0,200,0)
arm_09 = Attacks("armgeddon",200,60,50,0,4000,0)
arm_10 = Attacks("armastice (gives energy)",0,-300,60,0,1000000,0)
arm_attacks = [arm_01,arm_02,arm_03,arm_04,arm_05,arm_06,arm_07,arm_08,arm_09,arm_10]


leg_01 = Attacks("kick",40,50,85,0,100,0)
leg_02 = Attacks("stomp",70,40,90,0,80,0)
leg_03 = Attacks("blast",75,100,70,0,200,0)
leg_04 = Attacks("ultimate karate kick",100,60,30,0,4000,0)
leg_05 = Attacks("leg-day",70,80,90,0,140,0)
leg_06 = Attacks("legiathon",100,70,90,0,30,0)
leg_07 = Attacks("knee jab",60,100,70,0,200,0)
leg_08 = Attacks("bicycle kick",300,60,30,0,600,0)
leg_09 = Attacks("spinjitstu",90,80,80,0,1000,0)
leg_10 = Attacks("dropkick",99,90,100,0,800,0)
leg_11 = Attacks("heel grind",69,40,70,0,500,0)
leg_attacks = [leg_01,leg_02,leg_03,leg_04,leg_05,leg_06,leg_07,leg_08,leg_09,leg_10,leg_11]




    
ahead_attacks = []
achest_attacks = []
aarm_attacks = []
aleg_attacks = []
for i in range(b):
    ahead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    achest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    aarm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    aleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
aleg_attacks.append(run)
ahead_attacks.append(run)
achest_attacks.append(run)
aarm_attacks.append(run)
a_Head = Module("Head",100,ahead_attacks)
a_Chest = Module("Chest",100,achest_attacks)
a_Arm = Module("Arm",100,aarm_attacks)
a_Leg = Module("Leg",100,aleg_attacks) 
Mech_a = Robot("Mech_x43_a",a_Head,a_Chest,a_Arm,a_Leg,2000,-1000,2000,0,"marks")  



bhead_attacks = []
bchest_attacks = []
barm_attacks = []
bleg_attacks = []
for i in range(b):
    bhead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    bchest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    barm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    bleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
bleg_attacks.append(run) 
barm_attacks.append(run) 
bhead_attacks.append(run) 
bchest_attacks.append(run) 
b_Head = Module("Head",100,bhead_attacks)
b_Chest = Module("Chest",100,bchest_attacks)
b_Arm = Module("Arm",100,barm_attacks)
b_Leg = Module("Leg",100,bleg_attacks) 
Mech_b = Robot("Mech_x43_b",b_Head,b_Chest,b_Arm,b_Leg,2000,-1000,2500,0,"marks")


chead_attacks = []
cchest_attacks = []
carm_attacks = []
cleg_attacks = []
for i in range(b):
    chead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    cchest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    carm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    cleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
cleg_attacks.append(run) 
cchest_attacks.append(run) 
carm_attacks.append(run) 
chead_attacks.append(run) 
c_Head = Module("Head",100,chead_attacks)
c_Chest = Module("Chest",100,cchest_attacks)
c_Arm = Module("Arm",100,carm_attacks)
c_Leg = Module("Leg",100,cleg_attacks) 
Mech_c = Robot("Mech_x43_c",c_Head,c_Chest,c_Arm,c_Leg,2000,-1000,3000,0,"marks")
   
dhead_attacks = []
dchest_attacks = []
darm_attacks = []
dleg_attacks = []
for i in range(b):
    dhead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    dchest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    darm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    dleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
dleg_attacks.append(run) 
dchest_attacks.append(run) 
darm_attacks.append(run) 
dhead_attacks.append(run) 
d_Head = Module("Head",100,dhead_attacks)
d_Chest = Module("Chest",100,dchest_attacks)
d_Arm = Module("Arm",100,darm_attacks)
d_Leg = Module("Leg",100,dleg_attacks) 
Mech_d = Robot("Mech_x43_d",d_Head,d_Chest,d_Arm,d_Leg,2000,0,0,1,"delta")
    
    
ehead_attacks = []
echest_attacks = []
earm_attacks = []
eleg_attacks = []
for i in range(b):
    ehead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    echest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    earm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    eleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
eleg_attacks.append(run) 
echest_attacks.append(run) 
earm_attacks.append(run) 
ehead_attacks.append(run) 
e_Head = Module("Head",100,ehead_attacks)
e_Chest = Module("Chest",100,echest_attacks)
e_Arm = Module("Arm",100,earm_attacks)
e_Leg = Module("Leg",100,eleg_attacks) 
Mech_e = Robot("Mech_x43_e",e_Head,e_Chest,e_Arm,e_Leg,2000,0,500,1,"delta")
    
    
fhead_attacks = []
fchest_attacks = []
farm_attacks = []
fleg_attacks = []
for i in range(b):
    fhead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    fchest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    farm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    fleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
fleg_attacks.append(run) 
fchest_attacks.append(run) 
farm_attacks.append(run) 
fhead_attacks.append(run) 
f_Head = Module("Head",100,fhead_attacks)
f_Chest = Module("Chest",100,fchest_attacks)
f_Arm = Module("Arm",100,farm_attacks)
f_Leg = Module("Leg",100,fleg_attacks) 
Mech_f = Robot("Mech_x43_f",f_Head,f_Chest,f_Arm,f_Leg,2000,0,500,1,"delta")    

ghead_attacks = []
gchest_attacks = []
garm_attacks = []
gleg_attacks = []
for i in range(b):
    ghead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    gchest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    garm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    gleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
gleg_attacks.append(run) 
gchest_attacks.append(run) 
garm_attacks.append(run) 
ghead_attacks.append(run) 
g_Head = Module("Head",100,ghead_attacks)
g_Chest = Module("Chest",100,gchest_attacks)
g_Arm = Module("Arm",100,garm_attacks)
g_Leg = Module("Leg",100,gleg_attacks) 
Mech_g = Robot("Mech_x43_g",g_Head,g_Chest,g_Arm,g_Leg,2000,0,500,1,"delta")


hhead_attacks = []
hchest_attacks = []
harm_attacks = []
hleg_attacks = []
for i in range(b):
    hhead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    hchest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    harm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    hleg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
hleg_attacks.append(run) 
hchest_attacks.append(run)
harm_attacks.append(run) 
hhead_attacks.append(run) 
h_Head = Module("Head",100,hhead_attacks)
h_Chest = Module("Chest",100,hchest_attacks)
h_Arm = Module("Arm",100,harm_attacks)
h_Leg = Module("Leg",100,hleg_attacks) 
Mech_h = Robot("Mech_x43_h",h_Head,h_Chest,h_Arm,h_Leg,2000,0,500,1,"rebels")


ihead_attacks = []
ichest_attacks = []
iarm_attacks = []
ileg_attacks = []
for i in range(b):
    ihead_attacks.append(head_attacks[random.randint(0,len(head_attacks) - 1)])
    ichest_attacks.append(chest_attacks[random.randint(0,len(chest_attacks) - 1)])
    iarm_attacks.append(arm_attacks[random.randint(0,len(arm_attacks) - 1)])
    ileg_attacks.append(leg_attacks[random.randint(0,len(leg_attacks) - 1)])
ileg_attacks.append(run) 
ichest_attacks.append(run)
iarm_attacks.append(run) 
ihead_attacks.append(run) 
i_Head = Module("Head",100,ihead_attacks)
i_Chest = Module("Chest",100,ichest_attacks)
i_Arm = Module("Arm",100,iarm_attacks)
i_Leg = Module("Leg",100,ileg_attacks) 
Mech_i = Robot("Mech_x43_i",i_Head,i_Chest,i_Arm,i_Leg,2000,0,500,1,"rebels")








    

    
p01 = Planet()    
p02 = Planet()     
p03 = Planet()        
p04 = Planet()        
p05 = Planet()      
p06 = Planet()     
p08 = Planet()        
p09 = Planet()
p10 = Planet()      
p11 = Planet()     
p12 = Planet()        
p13 = Planet() 
p14 = Planet()      
p15 = Planet()     
p16 = Planet()        
p17 = Planet() 
p18 = Planet()      
p19 = Planet()     
p20 = Planet()        
p21 = Planet() 
p22 = Planet()     
p23 = Planet()        
p24 = Planet() 
p25 = Planet()      
p26 = Planet()     
p27 = Planet()        
p28 = Planet()
p29 = Planet()        
p30 = Planet() 
p31 = Planet()     
p32 = Planet()        
p33 = Planet() 
p34 = Planet()      
p35 = Planet()     
p36 = Planet()        
p37 = Planet() 
p38 = Planet()     
p39 = Planet()        
p40 = Planet()
p41 = Planet()        
p42 = Planet() 
p43 = Planet()     
p44 = Planet()        
p45 = Planet() 
p46 = Planet()      
p47 = Planet()     
p48 = Planet()        
p49 = Planet()
p50 = Planet()        
m01 = Missile()
m02 = Missile()
m03 = Missile()
m04 = Missile()
m05 = Missile()
m06 = Missile()
m07 = Missile()
m08 = Missile()
m09 = Missile()
m10 = Missile()
m11 = Missile()
m12 = Missile()
m13 = Missile()
        
        
    
enemy_mechs = [Mech_d,Mech_e,Mech_f,Mech_g,Mech_h]    
    
    
    
    
        
T1 = Thruster(100,100,"main")        
T2 = Thruster(100,100,"backup")
T3 = Thruster(100,100,"double backup")
Mark_thruster = [T1,T2,T3]
Marks_mechs = [Mech_a,Mech_b,Mech_c]
Mark = Spaceship("ss guppy","marks",0,0,Mark_thruster,Marks_mechs,100000,2000,0,0,0)        





def Start(ship):
    print("")
    print("")
    print("")
    print("")
    print("Hello, commander!")
    time.sleep(1)
    print("")
    print("what do you want to name your empire?")
    emp = input()
    ship.empire = "The" + " " + emp + " " + "Empire"
    print( "Aaaand what would you like to name your ship?")
    name = input()
    ship.name = "The" + " " + name
    print("press enter to begin your ADVENTURE!")
    use = input()
    ship.x = 0
    ship.y = 0
    ship.money = 2000
    ship.energy = 100000
    ship.visited = []
    for i in range(len(ship.mechs)):
        g = ship.mechs[i]
        g.energy = 2000
        g.x = ship.x
        g.y = ship.y
    time.sleep(1)
    ship.hub()
    





    
    
    
def program():
    print("")
    print("")
    print("")
    print("Welcome to SPACE ADVENTURE!")
    time.sleep(0.5)
    print("")
    print("")
    time.sleep(1)
    while True:
        Start(Mark)          


        
            
            
            
            
            
    

program()
    


# In[ ]:





# In[ ]:




