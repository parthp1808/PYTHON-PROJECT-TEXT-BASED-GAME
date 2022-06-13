# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:32:07 2022

@author: ranit
"""



from actor import actor
from fileloader import fileloader
from nltk.tokenize import word_tokenize
from mapgame import mapgame
from inputcases import inputcases
import random
class player(actor):
    
    
    def __init__(self):
        loader=mapgame()
        loader1=fileloader()
        self.dict1=loader.mapgenerator()
        
        super().__init__(magicalres=2,armor=5,location=list(self.dict1.keys())[0],state=False) #initialiting the player with magic power and location
        self.visited=set() #set to avoid duplicates
        self.quesdic=loader1.fileloaderinst('mapques')
        self.gameitems=(loader1.fileloaderinst('item'))
        self.nuggets=loader1.fileloaderinst('nugget')
    def revealnugget(self):
        self.dict1[self.location]['items'].append(self.dict1[self.location]['nuggets'].items)
        print(f"Wow there is a new {self.dict1[self.location]['nuggets'].items.name} which came out of this {self.dict1[self.location]['nuggets'].name}")
        
    def seeitemsaround(self):
        for vals in self.dict1[self.location]['items']:
            print(vals.name+'\n')
    
    def movecommand(self,inp):     #move from one room to another
       
       for vals in self.dict1[self.location]['Surrounding']:
           try:
               self.location=self.dict1[self.location]['Surrounding'][inp]
               break
           except KeyError:
               print("Key not found")
       
    def displaymoves(self):       #display where u can go from current room and what room you are currently in
        maplist=list(self.dict1[self.location]['Surrounding'])
               
        print(f"You are in  the {(self.location).lower()}.Your directions from this location are")
        for vals in maplist:
            
            print(f" {vals}",end="")
    def describeroom(self):
        CYAN='\033[20m'
        itemarrstring=[]
        if self.location not in self.visited:
            for keys,vals in self.quesdic.items():
                if(keys==self.location):
                    print(CYAN+vals.get('descr1'))
                    break
        self.visited.add(self.location)
        if self.dict1[self.location]['characters']!='':
            print(f"{CYAN}The people I see around are {self.dict1[self.location]['characters'].name}")
        else:
            print("There seems to be no signs of intelligent life anywhere around here")
        if self.dict1[self.location]['creatures']!='':
            print(f"Oh i see a disgusting {self.dict1[self.location]['creatures'].name}")
        if self.dict1[self.location]['nuggets']!='':
            print(f"There lies a {self.dict1[self.location]['nuggets'].name}.{self.dict1[self.location]['nuggets'].descr}")
        for vals2 in self.dict1[self.location]['items']:
               itemarrstring.append(vals2.name)
        print("The items I see around here are" ,",".join(itemarrstring))   
    def pickitem(self,item1s):
        selfitemsarray=[x.name for x in self.items]
        for vals in self.dict1[self.location]['items']:
            if vals.name==item1s and item1s not in selfitemsarray:
                self.items.append(vals)
                #self.dict[self.location]['items'].pop(selfitemsarray.index(item1s))
        
                print(f"The item {item1s} was added to the inventory")
                break
        else:
            print('Cant pick item. you already have it or have used it ')
        
    def useitem(self,name):#does not involve fighting with item
        temp=[]
        for num,item1 in enumerate(self.items):
            if name=='Chest':
                item1.chestopener(self)
                break
            if name=='Maraudersmap':
                print(f"The shortest path to your destiny to reach voldemort is\n")
                for vals in self.dict1[self.location]['items'][0].maraudersmap(self):
                    print(vals+"----->",end='')
                print("destiny")
                break
            if name=='Portal':
                self.location=random.choice(list(self.dict1.keys()))
                print("You have been randomly teleported to",self.location)
                
                
            if name==item1.name and item1.fight==0:
                self.health+=self.gameitems[name]['STATS']['heal']
                if self.health>100:
                    self.health==100
                self.magicalres+=self.gameitems[name]['STATS']['magicalres']
                self.armor+=self.gameitems[name]['STATS']['armor']
            self.items.pop(num)
            
        for item2 in self.items:    
            if item2.fight==1:
                item2.physicaldmg+=self.gameitems[name]['STATS']['physicaldmg']
                item2.magicaldmg+=self.gameitems[name]['STATS']['magicaldmg']
        
    def marauder(self):
        return self.dict1[self.location]['items'][0].maraudersmap(self)
    
    def checkinventory(self):
        print("INVENTORY :",end="")
        for vals in self.items:
            print(vals.name,end="")
    def play(self):
        
        b=inputcases(self)
        b.commands()


        
a=player()
a.play()