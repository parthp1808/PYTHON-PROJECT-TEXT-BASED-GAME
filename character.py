# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:11:20 2022

@author: ranit
"""
from creature import creature
from fileloader import fileloader

import random
class character(creature):
    def __init__(self,name,magicalres,armor,location,abilities,State):
        loader=fileloader()
        super().__init__(name,magicalres,armor,location,abilities,State)
        self.name=name
        self.magicalres=magicalres
        self.armor=armor
        self.location=location
        self.abilities=abilities
        self.info=loader.fileloaderinst('character')
        self.State=State
        self.phrases=loader.fileloaderinst('phrase')
        
     
    def interactplayer(self,opp):
        self.updatestate(opp)
        self.usespell(opp)
        
        if self.state==False:
            
            print(f"Hey {self.name} here again")
            randkey=random.choice(list(self.phrases.keys()))
            print(random.choice(list(self.phrases[randkey])))
        
    
