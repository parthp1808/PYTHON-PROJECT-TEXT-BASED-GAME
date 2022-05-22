# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:36:13 2022

@author: ranit
"""
import json
mapjson = open('map.json')
mapquesjson = open('mapques.json')
map1= json.load(mapjson)
questions=json.load(mapquesjson)
map1dic=map1['map']
quesdic=questions['mapques']#dictionary with game questions


class actor:
    def __init__(self,magic,location):
        self.hp=100 #all characters start with 100 hp
        self.location=location
        self.magic=magic
        self.items={}
    
    def fight(self,dmg):
        self.hp=self.hp-dmg
        
    def  alivechecker(self):
        if self.hp<=0:
            return False
        if self.magic<=0:
            return False
        return True
    

class charac(actor):
    def __init__(self,magic,location,state):
        super().__init__(location,magic)
        self.states=state
        
        

class player(actor):
    def __init__(self):
        super().__init__(magic=10,location=list(map1dic.keys())[0]) #initialiting the player with magic power and location
        self.visited=set()         #set to avoid duplicates
          #creating visited array
        
   
    def movecommand(self,inp):     #move from one room to another
       
       for keys,vals in map1dic.items():
           if keys==self.location:
               self.location=vals.get(inp)
               break
       
       
    def displaymoves(self):       #display where u can go from current room and what room you are currently in
        for keys,vals in map1dic.items():
            if keys==self.location:
                maplist=list(vals.keys())
                break
        print(f"You are in  the {(self.location).lower()}.Your directions from this location are")
        for vals in maplist:
            
            print(f" {vals}",end="")
    def describeroom(self):
        if self.location not in self.visited:
            for keys,vals in quesdic.items():
                if(keys==self.location):
                    print(vals.get('descr1'))
                    break
        self.visited.add(self.location)
#creating map
    

a=player()
a.describeroom()
a.displaymoves()
a.movecommand('W')
print(a.location)
a.describeroom()


