# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:31:14 2022

@author: ranit
"""
from actor import actor
from fileloader import fileloader
import random
class item(actor):
    def __init__(self,name,look,heal,physicaldmg,magicaldmg,magicalres,armor,location,fight,verb,state):
        super().__init__(name,magicalres,armor,location,state)
        self.name=name
        self.look=look
        self.heal=heal
        self.physicaldmg=physicaldmg
        self.magicaldmg=magicaldmg
        self.fight=fight
        self.verb=verb
        loader=fileloader()
        self.items=loader.fileloaderinst('item')
        self.map=loader.fileloaderinst('map')
    def maraudersmap(self,player1):
       
        newdic={}

        for keys in self.map:
            newdic[keys]=list(self.map[keys].values())
        explored = []
        queue = [[player1.location]]
        if player1.location == 'SLYTHEIN DORM':
            print("Same Node")
                
             
          
        while queue:
            path = queue.pop(0)
            node = path[-1]
         

            if node not in explored:
                neighbours = newdic[node]

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                     
                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour =='SLYTHEIN DORM':
                        return new_path
            
                explored.append(node)
             
    def mindreader(self,player1):
       for vals in player1.dict1.values():
           if vals['characters']!='':
              
               if vals['characters'].state==True:
                   
                   print(vals['characters'].name)
                
            
            
    
    
    def chestopener(self,player1):#--------------if key in items,remove the key from items and open chest and put item in items if the item is not already in inventory
        randomarr=[]
        newarr=[]
        selfarray=[x.name for x in player1.items]
        for vals in self.items.keys():
            if vals!='Key' and vals!='Chest':
                randomarr.append(vals)
        randomitemname=random.choice(randomarr)
        answer=self.itemcreator(randomitemname)    
            
        [newarr.append(vals2.name) for vals2 in player1.items]
        
        try:
            chestind=newarr.index('Chest')
            
            keyind=newarr.index('Key')
            
            player1.items.pop(chestind)
            if randomitemname not in selfarray:
                player1.items.append(answer)
            else:
                print("You have this item with you so you cannot pick it again.It will be destroyed")
            print(f'You found a {answer.name} and it has been added to your inventory')
        except ValueError:
            print("YOU CANNOT OPEN CHEST WITHOUT KEY")
            
    
    def itemcreator(self,name):
       
        statsitems=self.items[name]['STATS']
        obj=item(name,self.items[name].get('LOOK'),statsitems.get('heal'),statsitems.get('physicaldmg'),statsitems.get('magicaldmg'),statsitems.get('magicalres'),statsitems.get('armor'),statsitems.get('location'),statsitems.get('FIGHT'),statsitems.get('verb'),statsitems.get('State'))
        
        return obj


