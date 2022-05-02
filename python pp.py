map1 = {
  0:[1,2,3,4],
  1:[8,0],
  2:[5,1],
  3:[6,1],
  4:[5,1],
  5:[2],
  6:[7],
  7:[0,8],
  8:[7],
  }

class jedi:
    def __init__(self):
        self.inventory=["starfighter license","green milk","disguise cape" ]
        self.health=100
        self.weapon=["blaser"]
        self.force=["push"]
        self.life=1;
        self.money=100
   
    def inventoryremove(self,item):
        self.inventory.remove(item)
    def displayinventory(self):
        print('INVENTORY--------->',end='')
        for val in self.inventory:
            print(f'{val},',end='')
        print("\n")
    
    def inventoryupdate(self,item):
        if len(self.inventory)==5:
            print("You have too many items.You must drop one.You can only have five")
            print(self.inventory)
            ans=input("Do you want to remove one of the other ones or not pick this up")
            if 'remove' in ans:
                self.inventory.remove(ans)
                self.inventory.append(item)
            
        else:
            self.inventory.append(item)
    def displayforce(self):
        print('MY FORCE POWERS---->',end='')
        for val in self.force:
            print(f'{val},',end='')
        print('\n')
            
    def healthupdate(self,event):
        self.health+=event
    
    def weaponupdate(self,weapon):
        self.weapon.append(weapon)
        
    def forceupdate(self,forcenew):
        self.force.append(forcenew)
    def death(self):
        self.life=0
    def buy(self,price):
        if(self.money>=price):
            print(f"Transaction complete.Galactic credits remaining: {self.money-price}")
        else:
            print("Donot have enough galactic credits")
    def pickup(self,amt):
        self.money+=amt
        
class jedimissionfighter(jedi):
    def __init__(self):
        super().__init__()
       
        self.pos=0
       
    def room0(self):
        print(f"Troopers around but they seem to be sleeping!Great time to start our mission.Current Location:Amidala's Funeral room(mission area {self.pos})")
        for cc in map1.get(0):
            print(f"This hall gives me access to mission area{cc}")
        
        ans=input('Use controls w a s d  to move around')
        while (ans!="w" and ans!="s"and ans!="a" and ans!="d"):
            ans=input('Use controls w a s d  to move around')
        if ans=='w':
            self.pos=1;
        elif ans=='s':
            self.pos=2;
        elif ans=='a':
            self.pos=3
        elif ans=='d':
            self.pos=4    
    def room1(self):
       print("We are in the galactic casino(mission area 2).There seems to be a lot of people around.Bargwill Tomber seems to be working his massage to all the guests.Oh no!I have to stay focused.Lets move! ")
       print("I see a percussive cannon on the ground beside Slowen Lo who is passed out.Should i pick it up?")
       ans=input()
       if(ans=='yes'):
           self.inventoryupdate("percussive cannon")
           print(f'Current inventory:{self.inventory}')
       for val in map1.get(1):
           print(f"I see a way through to mission area{val}!")
       print("There seems to be two choices to move to the next area.Where to?Forward or back???This place is getting sketchy")
       ans=input()
       while ans!='w' or ans!='s':
           if ans=='w':
               self.pos=8;
           elif ans=='s':
              self.pos=0;
           else:
              print("I couldnt quite get you")
      
    def room2(self):
        print('Oh snap,we are in the galatic senate chamber.This is massive and I donot think I am supposed to be here.I cannot get caught!There is a thousand platforms around me and there seems to be people down there.I feel stronger suddenly.There is an element of the dark force which I feel right now.Should I pick up the ability to zap creatures?It seems to be too strong')
        ans=input()
        if(ans=='yes'):
            self.forceupdate("LIGHTNING")
            self.displayforce()
        print('I dont think i should have done that.urghhh i feel guilty!')
        print("Oh no someone saw me!I have to get out of here but all the doors are shut!Damnit,I see general grevious coming towards me.Oh wait,I see a tunnel through this platform.Should i jump through or try to fight")
        ans=input()
        if (ans=="fight"):
            print("The 2 lightsabers pierce my flesh and the force ghost escapes!Death.")
            self.death()
        else:
            print("Oh.I passed out.Where am i?")
            self.pos=5
    def room3(self):
        print("This room seems to be smell funny.It has historic artifacts,paintings,sculptures of the fighters in the battle of Endor and the resistance of the first order during the battle of Takodana.There seems to be nobody around except the shopkeeper here and its abnoxiously quiet.")
        ans=input("I see some Naboo patties and chewsticks.Should i buy them.They cost 20 galactic credits")
        if "buy" in ans or "yes" in ans:
            self.buy(20)
            self.inventoryupdate('Naboo patties and chewsticks')
            self.displayinventory()
        print("I see a door to the next room but its shut.How could i possibly get through")
        
        for val in map1.get(2):
            print(f" There lies a way to mission area{val}!")
        print("I can use force push to go through.However i dont know what lies behind.Should i go through?There seems to be no light seeping through and seems scary.Do i go back to mission area 0 or forward")
        ans=input()
        if 'forward' in ans:
            self.pos=6
        else:
            self.pos=0
    def room4(self):
        print("This place seems to be familiar.Oh it is the great ceremony hall of yavin4.This place seems to always be booming but there seems to be an eerie silence here tonight.Anyway,lets see whats in here")
        print("*Droid arrives asking for license*.Do i kill the droid,give him my license or go back.")
        ans=input()
        if 'give' in ans:
            print("Smooth entry phew.Alright lets go through.Oh no, he never returned my license")
            self.inventoryremove('starfighter license')
            self.displayinventory()
            print("*Royal guards arrive*You have been arrested sir for illegal entry into this section.You will be impriosened in force insensitive chamber for life")
            self.death()
        elif 'kill' in ans:
           print("Alright it didnt trigger a response.Lets run through this podium.")
           print("There seems to be a bowcaster on the ground.Do i pick it up?It will make my bag heavier and make me slow")
           ans=input()
           if 'yes' in ans or 'pickup' or 'pick' in ans:
               self.inventoryupdate('bowcaster')
               self.displayinventory()
               print("Ok lets move forward.This exploration mission must continue.Ill move through this dark tunnel")
               self.pos=5
        elif 'back' in ans:
            self.pos=0
    
    def room5(self):
        print("We are outside!Icy mountains,tons of wampa,large sharp glaciers,white skies and a buzzing atmosphere.This place seems to have an immaculate vibe.However I have to be careful for rebel spies.There comes the chancellor!")
        print("*WAMPAS*:Everyone bow down to the chancellor.We are here to celebrate the festival of lights.Everyone must show their ID's")
        if('starfighter license' in self.inventory):
            print( "*LICENSE ACCEPTED.STARFIGHTER PILOT")
            print("Let us buy things from the festival but i have to be careful for rebel spies tracking me down even though my fake ID has pulled me through here")
            print("Would like to buy Deep-Fried Nuna Legs with a side of Colo Claw fish for 15 galactic credits?")
            ans=input()
            if 'yes' in ans or 'buy' in ans:
                self.buy(15)
                self.forceupdate('Mind trick')
                print("Colo Fish has force enhancing properties.I feel stronger and have learned the mind trick")
                self.displayforce()
            print("10 rebel spies have grabbed me from behind and are controlling me.My hands and legs are tied")
            if 'Mind trick' not in self.force:
                print("I have nothing i can do without my limbs.CAPTURED!")
                self.life=0
            else:
               print('I must use the force.Which force do i use?')
               self.displayforce()
               ans=input()
               if 'trick' not in ans:
                   print('Damn these things donot respond to my forces.My hands are tied and i have been captured')
                   self.life=0
               elif 'trick' in ans:
                   print('Good thing i ate the Colo fish.These disgusting creatures are following my command to leave me alone')
                   print('Ok we have to get out of here before more rebel spies try to get on me.I see a tunnel on the southern side of the tower.I am going to head through this dark tunnel and see where it leads me.Oh,it is an antigravity vaccum tunnel.')
                   self.pos=2
                                
        
player1=jedimissionfighter()
while (player1.life==1):
    

    if (player1.pos==0):
        player1.room0()
    elif (player1.pos==1):
        player1.room1()
    elif(player1.pos==2):
        player1.room2()
    elif(player1.pos==3):
        player1.room3()
    elif(player1.pos==4):
        player1.room4()
    
    elif(player1.pos==5):
        player1.room5()
    
        
        
        
        
        
        
        
        