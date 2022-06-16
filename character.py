# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:11:20 2022

@author: ranit
"""
from creature import creature
from fileloader import fileloader


import random
class character(creature):
    def __init__(self,name,look,items,magicalres,armor,location,abilities,state):
        loader=fileloader()
        super().__init__(name,look,magicalres,armor,location,abilities,state)
      
       
        self.location=location
        
        self.info=loader.fileloaderinst('character')
        
        self.phrases=loader.fileloaderinst('phrase')
        self.items.append(items)
       
    def interactplayer(self,opp):
        self.updatestate(opp)
        
        
        if self.state!=True:
            
            print(f"Hey {self.name} here again")
            randkey=random.choice(list(self.phrases.keys()))
            print(random.choice(list(self.phrases[randkey])))
        
        if self.state==True:
            self.usespell(opp)
    def damagetakerprompts(self):
        if self.health<=80 and self.health>=70:
            print(f'{self.name} seems to be bleeding out of his nose a little bit.')
        elif self.health>=60 and self.health<70:
            print(f'{self.name} bones seemed to crack a little bit too much.They might have dislocated.')
        elif self.health>=50 and self.health<60:
            print(f'{self.name} legs seem to be twisted around taking all the hits.')
        elif self.health>=40 and self.health<50:
            print(f'{self.name} is hobbling so hard that it doesnt feel like he will be able to fight very much more.')
        elif self.health>=30 and self.health<50:
            print(f'There appear to be large wounds formed around the groin of the injured {self.name}.')
        elif self.health>0 and self.health<30:
            print(f'Appears to be loads of gore coming off the forehead of {self.name} and is barely able to control himself')