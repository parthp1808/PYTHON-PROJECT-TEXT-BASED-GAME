# -*- coding utf-8 -*-
"""
Created on Sun Jun 12 10:54:37 2022

@author: ranit
"""

import spacy
from nltk.tokenize import word_tokenize


class inputcases:
    def __init__(self,player):
        self.player=player
        
    def commands(self):
       
        self.player.describeroom()
        self.player.displaymoves()
        while self.player.health>0 and self.player.dict1['SLYTHEIN DORM']['characters'].alivechecker()!=False:#check if player is alive
            self.player.npcdeath()#check if characters or creatures are alive and remove if dead.
            self.update()#update the states of characters and creatures
            inp=input()
            inp1=word_tokenize(inp)
           
        #player inventory string for checking
            if len(inp1)==1:
                if(self.basiccommands(inp)==False):
                    print('Donot understand you')
                    
            if len(inp1)==2:
                if self.basiccommands(inp)==False and len(inp1)==2:
                    self.checklen2(inp1)
                
            if len(inp1)==0 or len(inp1)>=3:
                print('Inacurrate command')
                
        if self.player.health<=0:  #if player is dead,game ends
            print('You died')
        if self.player.dict1['SLYTHEIN DORM']['characters'].alivechecker()==False:#if voldemort dies,game ends
            print("Voldemort died.You have gotten peace to the world of wizards and artistry.Congragulations you remain a hero forever")
    
    def basiccommands(self,inp):
        g='filename_pi.obj'
        if inp in ['N','S','E','W']:
            
            self.player.movecommand(inp)
            self.player.describeroom()
                 
        elif inp.lower()=='stats':
            print(f'Armor:{self.player.armor}\n Magical Resistance:{self.player.magicalres}')
        elif inp.lower() =='health':
             print(self.player.health)
             return
        elif inp.lower()=='weapon':
            self.player.equippedweapon()
        elif inp.lower()=='save game':
            g=self.player.save()
            print('GAME SAVED')
        elif inp.lower()=='load game':
            self.player.load(g)
            print('GAME LOADED.')
            self.player.describeroom()
        elif inp.lower()=='show moves':
            self.player.displaymoves()
            return
        
        
        elif inp.lower()=='describe room':
            self.player.describeroom()
            return
        elif 'inventory' in inp:
            self.player.checkinventory()
            return
        elif inp.lower()=='see people':
            self.player.seepeople()
            return
        elif inp.lower()=='see items':
            self.player.seeitems()
            return
        elif inp.lower()=='save':
            self.player.save()
           
        elif inp.lower()=='load':
            
            self.player.load()
        else:
            return False
        
        
    def update(self):
        
        if self.player.dict1[self.player.location]['creatures'] != "":
            self.player.dict1[self.player.location]['creatures'].updatestate(self.player)
            self.player.dict1[self.player.location]['creatures'].usespell(self.player)
        
        if self.player.dict1[self.player.location]['characters'] != "":
            self.player.dict1[self.player.location]['characters'].updatestate(self.player)
            
# =============================================================================
    def checklen2(self,inp1):
       
        nlp = spacy.load("en_core_web_lg")
        
        verb=inp1[0]
        noun=inp1[1]
        
        if nlp(verb).similarity(nlp('pick'))>0.5:
            if noun in list(self.player.gameitems):
                    
                    self.player.pickitem(noun)
                    return
        if nlp(verb).similarity(nlp('describe'))>0.5:
            if noun in list(self.player.gameitems):
                    
                    self.player.describeitem(noun)
                    return
        if nlp(verb).similarity(nlp('drop'))>0.5:
            if noun in list(self.player.gameitems):
                    
                    self.player.dropitem(noun)
                    return
        if nlp(verb).similarity(nlp('equip'))>0.5:
            if noun in list(self.player.gameitems):
                self.player.equipweapon(noun)
                return
            else:
                print('Unknown item')
                return
         
        if nlp(verb).similarity(nlp('attack'))>0.65:
            if self.player.dict1[self.player.location]['characters']!='':
                if(noun.split()[-1]==(self.player.dict1[self.player.location]['characters']).name):
                    self.player.dict1[self.player.location]['characters'].takedamagefromplayer(self.player)
                    self.player.dict1[self.player.location]['characters'].damagetakerprompts()
                    return
        if nlp(verb).similarity(nlp('attack'))>0.65:
            if self.player.dict1[self.player.location]['creatures']!='':
                if(noun.split()[-1]==(self.player.dict1[self.player.location]['creatures']).name):
                    self.player.dict1[self.player.location]['creatures'].takedamagefromplayer(self.player)
                    return
        if self.player.dict1[self.player.location]['characters']!='':         
            if nlp(verb.lower()).similarity(nlp('interact'))>0.5:
           
                if (noun==self.player.dict1[self.player.location]['characters'].name):
                    self.player.dict1[self.player.location]['characters'].interactplayer(self.player)
                    return
        if self.player.dict1[self.player.location]['creatures']!='':               
            #first word interact second word character name
            if nlp(verb.lower()).similarity(nlp('interact'))>0.5:
           
                if (noun==self.player.dict1[self.player.location]['creatures'].name):
                    self.player.dict1[self.player.location]['creatures'].interactplayer(self.player)   
                    return
        if noun in list(self.player.gameitems) and self.player.gameitems[noun]['STATS']['FIGHT']==0:
            
            for vals in self.player.gameitems[noun]['STATS']['verb']:
                if nlp(verb.lower()).similarity(nlp(vals))>0.5:#verb in game item verb and noun in game items and make sure the item is not an attacking item(wand,daggers)
                   
                    self.player.useitem(noun)
                    return
                    
        
        if self.player.dict1[self.player.location]['nuggets']!='':#check if you are in the same room with a nugget and the verb and verb in nuggets is accurate,then open nuugget
            if noun==self.player.dict1[self.player.location]['nuggets'].name:
                
                if nlp(verb).similarity(nlp(self.player.nuggets[noun]['verb']))>0.5:
                        self.player.revealnugget()
                        return
        if verb in self.player.gameitems and noun=='STATS':
            self.player.checkitemstats(verb)
            return
             
        print('I didnt quite get you')
   