# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:28:30 2022

@author: ranit
"""

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
        print("TOOK DAMAGE")
        
    
        
        
    def  alivechecker(self):
        while self.health>=0:
            return True
        return False