# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:36:13 2022

@author: 
"""

import nltk
from nltk.tokenize import word_tokenize
import json
import numpy.random as npr
import random

itemjson=open('items.json')
characterjson=open('characters.json')
mapjson = open('map.json')
creaturesjson=open('creatures.json')
mapquesjson = open('mapques.json')
mapresponse=open('mapresponses.json')
charjson=open('characters.json')
map1= json.load(mapjson)
items1=json.load(itemjson)
characters1=json.load(characterjson)
questions=json.load(mapquesjson)
creatures1=json.load(creaturesjson)
chars1=json.load(charjson)
mapresponsejson=json.load(mapresponse)
map1dic=map1['map']#map
quesdic=questions['mapques']#dictionary with game questions
characters=chars1['characters']#character dictionary
responses=mapresponsejson['mapresponses']#responses
creatures=creatures1['creatures']
characterf=characters1['characters']  #character dictyionary to use
items=items1['items']


class actor:#abstract class for chararcter,player
    def __init__(self,magicalres,armor,location,state):
        self.health=100 #all characters start with 100 hp
        self.location=location
        
        
        self.magicalres=magicalres
        self.armor=armor
        self.items=[]
        self.state=state
    
    def takedamage(self,physicaldmg,magicaldmg):
        self.health-=abs((1-self.armor*0.05)*physicaldmg)
        self.health-=abs(1-self.magicalres*0.02)*magicaldmg 
    
    
        
        
    def  alivechecker(self):
        while self.health>=0:
            return True
        return False
        
        
    
    

class creature(actor): #creature class 
    def __init__(self,name,magicalres,armor,location,spell,state):
        super().__init__(magicalres,armor,location,state)
        self.spell=spell
        self.name=name
        self.currentlocation=location[0]
        self.state=state
    
    
    def givedamage(self,opponent,magicresreduction,armorreduction,physicaldmg,magicaldmg): #possibly override.give damage to opponent
        opponent.armor-=armorreduction
        opponent.magicalres-=magicresreduction
    
        opponent.health-=abs((1-opponent.armor*0.05)*physicaldmg)
        opponent.health-=(1-opponent.magicalres*0.02)*magicaldmg 
    def usespell(self,opponent,name):            #use spell and do damage to the player
        arr=creatures[name]['ABILITIES']
        rand=npr.randint(0,len(arr))
        for num,val in enumerate(arr):
            if num==rand:
                self.givedamage(opponent,arr[val].get('magicresreduction'),arr[val].get('armorreduction'),arr[val].get('physicaldmg'),arr[val].get('magic damage'))
                
    def takedamagefromplayer(self,opponent,name):
        for vals in opponent.items:
            if (name==vals.name) and (vals.fight==1):
                self.takedamage(vals.physicaldmg,vals.magicaldmg)
            

class character(actor):
    def __init__(self,name,magicalres,armor,states,location,items,state):
        super().__init__(magicalres,armor,location,state)
        self.name=name
        self.magicalres=magicalres
        self.armor=armor
        self.location=location
        self.states=states
        self.items=items
    
    
    
        
    
    
    
                 
                
        
class item(actor):
    def __init__(self,name,heal,physicaldmg,magicaldmg,magicalres,armor,location,fight,state):
        super().__init__(magicalres,armor,location,state)
        self.name=name
        self.heal=heal
        self.physicaldmg=physicaldmg
        self.magicaldmg=magicaldmg
        self.magicalres=magicalres
        self.armor=armor
        
        self.location=location
        self.fight=fight
        self.state=state
       
    
    def chestcreator(self):#DONOT USE FUNCTION.DONOT CALL THIS.only chest opener uses this
        randomarr=[]
        for vals in items.keys():
            if vals!='Key' and vals!='Chest':
                randomarr.append(vals)
        
        return itemcreator(random.choice(randomarr))
    
    def chestopener(self,player):#--------------if key in items,remove the key from items and open chest and put item in items if the item is not already in inventory
        newarr=[]    
        [newarr.append(vals.name) for vals in player.items]
        
        try:
            chestind=newarr.index('Chest')
            keyind=newarr.index('Key')
        except ValueError:
            print("Item not available")
            
        player.items.pop(chestind)
        player.items.append(self.chestcreator())
                
            
        
    def timestopper(self):
       # [voldemort for voldemort in dict1['SLYTHEIN DORM']['characters'] if voldemort.name=='Voldemort']
        return 1
    
    def mauradersmap(self):
        return 1
    
    
    
    
    
        
        

class player(actor):
    def __init__(self,dict1):
        super().__init__(magicalres=2,armor=5,location=list(map1dic.keys())[0],state=False) #initialiting the player with magic power and location
        self.visited=set() #set to avoid duplicates
        self.dict1=dict1
        
   
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
        if self.location not in self.visited:
            for keys,vals in quesdic.items():
                if(keys==self.location):
                    print(vals.get('descr1'))
                    break
        self.visited.add(self.location)
        for vals in self.dict1[self.location]['characters']:
            print("The people I see around are ",vals.name)
        for vals2 in self.dict1[self.location]['items']:
           
               print(vals2.name)     ###29 MAY LEFT OFF
    def pickitem(self,item1s):
        ls=[]
        for v in self.dict1[self.location]['items']:
            ls.append(v.name)
        if item1s in ls:
            self.items.append(self.dict1[self.location]['items'][ls.index(item1s)]) 
        else:
            print('No item')
    
    

   
        
    
    def userturn(self):#plays user turn.Asks user for input and checks if verb is in the line.Does things accordingly
        usrinputverb=input()
        tokenized=word_tokenize(usrinputverb)
        
        for count,ans in enumerate(responses[self.location].get('verb')):
            if tokenized[0]==ans:
                    self.magic=self.magic+responses[self.location][f'eventres{count+1}']['magic']
                    self.health=self.health+responses[self.location][f'eventres{count+1}']['health']
                    
def charactercreator():
    objlist=[]
    for keyz in characterf.keys():
        keyz1=character(keyz,characterf[keyz]['STATS'].get('magicalres'),characterf[keyz]['STATS'].get('armor'),characterf[keyz].get('State'),characterf[keyz].get('location'),characterf[keyz].get('items'),characterf[keyz].get('State'))
        objlist.append(keyz1)
    return objlist
def creaturecreator():#create objects for the creatures
    objlist=[]
    for keyz in creatures.keys():
        keyz1=creature(keyz,creatures[keyz]['STATS'].get('magicalres'),creatures[keyz]['STATS'].get('armor'),creatures[keyz].get('location'),creatures[keyz]['ABILITIES'],creatures[keyz]['STATS'].get('STATE'))
        objlist.append(keyz1)
    return objlist
def itemcreator(name):
    statsitems=items[name]['STATS']
    obj=item(name,statsitems.get('heal'),statsitems.get('physicaldmg'),statsitems.get('magicaldmg'),statsitems.get('magicalres'),statsitems.get('armor'),statsitems.get('location'),statsitems.get('FIGHT'),statsitems.get('State'))
    
    return obj

def fight(player,opponent,dict1):#if player and opponent in same room,they keep fighting
        print(f"An angry {(opponent.name).lower()} rushes towards me.It's rage boils over.")
        playeritems=[]
        [playeritems.append(x.name) for x in player.items]
        
        if len(playeritems)!=0:
            for vals in player.items: #check if user has items to fight
                if vals.fight==1:
                   
        
                    while True:
        
                        inp=input()
                        if inp in playeritems:
                            opponent.takedamagefromplayer(player,inp)
            
                        if opponent.alivechecker()==False:
                            print(f"{opponent.name} has been slayn")
                            del(dict1[player.location]['creatures'])
                            break
    
                        opponent.usespell(player,opponent.name)
                        if player.alivechecker()==False:
                            print("You have died gameover")
                            break
                        print(f"player health is{player.health}")
                        print(f"{opponent.name}health is{opponent.health}")
                        print(player.alivechecker())
                        print(opponent.alivechecker())
        else:
            print("Cannot fight!I have no weapons.")
       
def mapgenerator():#generates map with creatures and rooms in specific place.BASE FOR ALL FYH
    characters=charactercreator()
    creatures=creaturecreator()
    itemscreatorarray=[]
    [itemscreatorarray.append(itemcreator(x)) for x in items.keys()]
    
    gamemap={}
    for vals in map1dic.keys(): #all locations
        gamemap[vals]={}
        
        gamemap[vals]["items"]=[]
        gamemap[vals]["characters"]=[]
        gamemap[vals]["creatures"]=[]
    
    for keys,vals in map1dic.items():
        gamemap[keys]['Surrounding']=vals
    for people in characters:
        for vals in people.location:
            gamemap[vals]['characters'].append(people)
    for creats in creatures:
        gamemap[creats.location]['creatures'].append(creats)
    for its in itemscreatorarray:
        for val in its.location:
            gamemap[val]['items'].append(its)
    return gamemap    


def gameplayer():
    terrain=mapgenerator()
    harry=player(terrain)
    while harry.alivechecker() or [voldemort.alivechecker()==False for voldemort in terrain['SLYTHEIN DORM']['characters'] if voldemort.name=='Voldemort']:
        [fight(harry,creats,terrain) for creats in terrain[harry.location]['creatures'] if creats!="" ]
        
       
        harry.describeroom()
        harry.displaymoves()
        inp=input()
        try:
            harry.pickitem(inp)
        except:
            print("Keep going")
        [print(itm.name) for itm in harry.items]
        inp2=input()
        harry.movecommand(inp2)        

a=player()
 


