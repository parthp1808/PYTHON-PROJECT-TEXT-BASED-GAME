# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:32:07 2022

@author: ranit
"""


import warnings
warnings.filterwarnings('ignore')
import pickle
from actor import actor
from fileloader import fileloader
from mapgame import mapgame
from inputcases import inputcases
import random

random.seed(59)
class player(actor):
    
    
    def __init__(self):
        loader=mapgame()
        loader1=fileloader()
        self.dict1=loader.mapgenerator()
        
        super().__init__(name='Harry',magicalres=2,armor=5,location=list(self.dict1.keys())[0],state=False) #initialiting the player with magic power and location
        self.visited=set() #set to avoid duplicates
        self.quesdic=loader1.fileloaderinst('mapques')
        self.gameitems=(loader1.fileloaderinst('item'))
        self.nuggets=loader1.fileloaderinst('nugget')
       
    def revealnugget(self):
        nuggetlocation=self.dict1[self.location]['nuggets']
        self.dict1[self.location]['items'].append(self.dict1[self.location]['nuggets'].items)
        print(f"Wow there is a new {self.dict1[self.location]['nuggets'].items.name} which came out of this {self.dict1[self.location]['nuggets'].name}")
        self.dict1[self.location]['nuggets']=''
    
    
    def movecommand(self,inp):     #move from one room to another
       useritemtext=[]
       [useritemtext.append(x.name) for x in self.items]
       for vals in self.dict1[self.location]['Surrounding']:
           
           try:
               location=self.dict1[self.location]['Surrounding'][inp]
               if location=='SLYTHEIN DORM':
                   if 'TimeStopper' in useritemtext:
                       self.location=location
                       break
                   else:
                       print('SLYTHEIN DORM IS LOCKED')
                       break
               self.location=location
                     
               break
           except KeyError:
               print("Key not found")
    def seepeople(self):
        print(f"The people I see around are {self.dict1[self.location]['characters'].name}") if self.dict1[self.location]['characters']!='' else  print("There seems to be noone  anywhere around here")
        
    def seeitems(self):
        print('The items I see in this area are ',end='')
        len1=len(self.dict1[self.location].get('items'))-1
        if len1==-1:#no items
            print('nothing')
        for num,vals in enumerate(self.dict1[self.location].get('items')):
            
            if len1==0:#1 item
                print(f'{vals.name} which is a {vals.look}')
           
            elif num==len1:#last item
                
                print(f' and {vals.name} which is a {vals.look}',end='')
            elif num==len1-1:#element before last item must have and
                print(f'{vals.name} which is a {vals.look}',end='')
           
            else:
                print(f'{vals.name} which is a {vals.look} ,',end='')
    def dropitem(self,name):#go through items and check if it exists,then add it to game dictionary
        
        for nums,vals in enumerate(self.items):
            if vals.name==name:
                self.dict1[self.location]['items'].append(vals)
                del self.items[nums]
                print(f'{vals.name} dropped')
                return
        
    def equippedweapon(self):
        try:
            print([value.name for value in self.items if (value.state==True) and value.fight==1][0])
        except IndexError:
            print('No item equipped')
    def displaymoves(self): 
        #display where u can go from current room and what room you are currently in
        maplist=list(self.dict1[self.location]['Surrounding'])
       
               
        print(f"You are in  the {(self.location).lower()}.Your directions from this location are")
        [print(f" {vals}",end="") for vals in maplist]
            
            
    def describeroom(self):
        CYAN='\033[40m'
        
     
        if self.location not in self.visited:
            for keys,vals in self.quesdic.items():
                if(keys==self.location):
                    print(f'{CYAN+vals.get("descr1")}\n',end='')
                    self.seeitems()
                    print('\n')
                    self.seepeople()
                    
                    if self.dict1[self.location]['creatures']!='':
                        print(f"Oh i see a {self.dict1[self.location]['creatures'].look}.It is a {self.dict1[self.location]['creatures'].name}")
                    break
        else:
            print('You are in ',self.location)
            if self.dict1[self.location]['creatures']!='':
                print('I see a ',self.dict1[self.location]['creatures'].name)
        self.visited.add(self.location)
        if self.dict1[self.location]['nuggets']!='':
            print(f"There lies a {self.dict1[self.location]['nuggets'].name}.{self.dict1[self.location]['nuggets'].descr}")
            
     
          
        
    def pickitem(self,item1s):
        switch=0;
        roomitemval=self.dict1[self.location]['items']
        selfitemsarray=[x.name for x in self.items] #create string array for all users current items
        if len(self.items)<=4:
            for num,vals in enumerate(roomitemval):#loop through all items in location and check if item called for exists in same room.
            
                if vals.name==item1s and item1s not in selfitemsarray:
                    self.items.append(vals)
                    del roomitemval[num]
                    switch=1
                    print(f"The item {item1s} was added to the inventory")
                    break
        else:
            print('Slots full. ')
        print('Cant pick item. ') if switch==0 else print('')
    def useitem(self,name):#does not involve fighting with item
        
        for num,item1 in enumerate(self.items):
            if name=='Chest' and item1.name=='Chest':
                item1.chestopener(self)
                break
            elif name=='Maraudersmap' and item1.name=='Maraudersmap':
                print("The shortest path to your destiny to reach voldemort is\n")
                for vals in self.items[0].maraudersmap(self):
                    print(vals+"----->",end='')
                print("destiny")
                break
            elif name=='Portal' and item1.name=='Portal':
                self.location=random.choice(list(self.dict1.keys()))
                print("You have been randomly teleported to",self.location)
                break
            elif name==item1.name=='Mindreader':
                    print("The people who are possesed are")
                    self.items[0].mindreader()
                    
            elif name==item1.name and item1.fight==0:
                self.nonfightitemstatsupdate(name,num)
    def checkitemstats(self,name):
        for vals in self.items:
            if name==vals.name:
                print('PHYSICAL DMG',vals.physicaldmg)
                print('MAGICAL DMG',vals.magicaldmg)
                break
    def nonfightitemstatsupdate(self,name,num):
       
         self.health=self.health+self.gameitems[name]['STATS']['heal']
         
         if self.health>100:
             
             self.health=100
         self.magicalres+=self.gameitems[name]['STATS']['magicalres']
         
         self.armor+=self.gameitems[name]['STATS']['armor']
         print(f'{name} used successfully')
         
         self.items.pop(num)
         
         for vals in self.items:  #update damage of magicwand and daggers
             if vals.fight==1:
                 
                vals.physicaldmg+=self.gameitems[name]['STATS']['physicaldmg']
                
                vals.magicaldmg+=self.gameitems[name]['STATS']['magicaldmg']
                 
 
        
    def marauder(self):
        return self.maraudersmap(self)
    def equipweapon(self,name):
        if len(self.items)==0:
            print('No items in stash')
            return
        for weapon in self.items:
            if weapon.fight==1 and weapon.name==name:
                weapon.state=True
                print(f'{weapon.name} EQUIPPED')
            if weapon.fight==1 and weapon.name!=name:
                weapon.state=False
               
                    
            elif weapon.fight==0 and weapon.name==name:
                print('Item is not a a weapon')
    def describeitem(self,name):
        [print(vals.look) for vals in self.items if vals.name==name]
           
                
    def checkinventory(self):
        print("INVENTORY :",end="") 
        [print(vals.name,end=" ") for vals in self.items]
           
    def npcdeath(self):
        if self.dict1[self.location]['characters']!='':
            
            if (self.dict1[self.location]['characters']).alivechecker()==False:
                print(f'An item dropped on the ground off the death.:{self.dict1[self.location]["characters"].items[0].name}')
                self.dict1[self.location]['items'].append(self.dict1[self.location]['characters'].items[0])
                self.dict1[self.location]['characters']=''
        if self.dict1[self.location]['creatures']!='':
            if self.dict1[self.location]['creatures'].alivechecker()==False:
                
                self.dict1[self.location]['creatures']=''
    def play(self):
        
        b=inputcases(self)
        b.commands()

    def save(self):
        name='filename_pi.obj'
        file_pi = open(name, 'wb') 
        pickle.dump(self, file_pi)
        file_pi.close
        
        return name

        
    def load(self,name):
        filehandler = open(name, 'rb') 
        object = pickle.load(filehandler)
        self.__dict__.update(object.__dict__)

       
def main():
    harry=player()
    harry.play()

if __name__ == "__main__":
    main()