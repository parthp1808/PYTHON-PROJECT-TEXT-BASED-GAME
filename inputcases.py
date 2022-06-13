# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 10:54:37 2022

@author: ranit
"""
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

class inputcases:
    def __init__(self,player):
        self.player=player
        
    def commands(self):
        self.player.describeroom()
        self.player.displaymoves()
        nlp = spacy.load("en_core_web_lg")
        while self.player.health>0:
            
            inp=input()
        #player inventory string for checking
            playeritemtextarr=[]
            for x in self.player.items:
                playeritemtextarr.append(x.name)
            
            if inp in ['N','S','E','W']:
                try:
                    self.player.movecommand(inp)
                    self.player.describeroom()
                except:KeyError('Direction not available.')
            elif inp.lower() =='health':
                 print(self.player.health)
            elif inp.lower()=='show moves':
                self.player.displaymoves()
            
            elif inp.lower()=='see items':
                return self.player.seeitemsaround()
            
            elif inp.lower()=='describe room':
                return self.player.describeroom()
            else:
                
                
                temparr=[]
                inp1=word_tokenize(inp)
               
                
                if len(inp1)<3 and len(inp1)>1:
                    verb=inp1[0]
                    noun=inp1[1]
                    
                    if nlp(verb).similarity(nlp('pick'))>0.5:
                        for vals in self.player.dict1[self.player.location]['items']:
                            temparr.append(vals.name)
                        
                        if noun in temparr:
                            self.player.pickitem(noun)
                        else:
                            print('Item not in this area')
                            
                           
                    
                    elif self.player.dict1[self.player.location]['nuggets']!='':#check if you are in the same room with a nugget and the verb and verb in nuggets is accurate,then open nuugget
                        if noun==self.player.dict1[self.player.location]['nuggets'].name:
                            
                            if nlp(verb).similarity(nlp(self.player.nuggets[noun]['verb']))>0.5:
                                    self.player.revealnugget()
                    elif inp1[1]=='inventory':#last word ends with inventory,show your inventory
                        self.player.checkinventory()
                    
                    elif nlp(verb.lower()).similarity(nlp('interact'))>0.5 and (noun==self.player.dict1[self.player.location]['characters'].name):#first word interact second word character name
                        self.player.dict1[self.player.location]['characters'].interactplayer(self.player)
                        
                    elif nlp(verb.lower()).similarity(nlp('interact'))>0.5 and (noun==self.player.dict1[self.player.location]['creatures'].name):#first word interact second word creature name
                         self.player.dict1[self.player.location]['creatures'].interactplayer(self.player)
                         
         
                    elif noun in list(self.player.gameitems)  and self.player.gameitems[noun]['STATS']['FIGHT']==0:
                        for vals in self.player.gameitems[noun]['STATS']['verb']:
                            if nlp(verb.lower()).similarity(nlp(vals))>0.5:#verb in game item verb and noun in game items and make sure the item is not an attacking item(wand,daggers)
                                self.useitem(noun)
                    else:
                        print("I DIDNT QUITE GET YOU")
                                 
                   
                       
                elif len(word_tokenize(inp))==3:
                        verb=inp1[0]
                        noun=' '.join(inp1[1:])
                        
                        if self.player.dict1[self.player.location]['characters']!='' or self.player.dict1[self.player.location]['characters']!='':
                            
                            if(noun.split()[1]==(self.player.dict1[self.player.location]['characters']).name) and (noun.split()[0] in playeritemtextarr):
                                
                               
                                
                                for verbs in self.player.items[(playeritemtextarr.index(noun.split(' ')[0]))].verb:
                                    if nlp(verb).similarity(nlp(verbs))>0.5:
                                        self.player.dict1[self.player.location]['characters'].takedamagefromplayer(self.player,self.player.gameitems[noun.split()[0]]['STATS']['magicaldmg'])
                                 
                            elif (noun.split()[1]==(self.player.dict1[self.player.location]['creatures']).name) and (noun.split()[0] in playeritemtextarr):
                                for verbs in self.player.items[(playeritemtextarr.index(noun.split(' ')[0]))].verb:
                                    if nlp(verb).similarity(nlp(verbs))>0.5:
                                        self.player.dict1[self.player.location]['creatures'].takedamage(self.player.gameitems[noun.split()[0]]['STATS']['physicaldmg'],self.player.gameitems[noun.split()[0]]['STATS']['magicaldmg'])
                else:
                    print("I DIDNT QUITE GET YOU")         
                          
# =============================================================================
