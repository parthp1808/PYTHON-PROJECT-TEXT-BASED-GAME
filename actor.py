# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:28:30 2022

@author: ranit
"""

class actor:#abstract class for chararcter,player
    def __init__(self,name,magicalres,armor,location,state):
        self.health=100 #all characters start with 100 hp
        self.location=location
        
        self.name=name
        self.magicalres=magicalres
        self.armor=armor
        self.items=[]
        self.state=state
    
   
    
        
    