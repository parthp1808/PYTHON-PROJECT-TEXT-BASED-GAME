# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:30:22 2022

@author: ranit
"""
from actor import actor
from fileloader import fileloader
import numpy.random as npr
class creature(actor): #creature class 
    def __init__(self,name,magicalres,armor,location,abilities,state):
        loader=fileloader()
        super().__init__(magicalres,armor,location,state)
        self.abilities=abilities
        self.name=name
        
        self.state=state
        self.info=loader.fileloaderinst('creature')
        
    def takedamage(self,physicaldmg,magicaldmg):
        self.health-=abs((1-self.armor*0.05)*physicaldmg)
        self.health-=abs(1-self.magicalres*0.02)*magicaldmg 
        print(f"{self.name} just took damage and is angry.Interactions will mean certain war")
    def givedamage(self,opponent,magicresreduction,armorreduction,physicaldmg,magicaldmg): #possibly override.give damage to opponent
        opponent.armor-=armorreduction
        opponent.magicalres-=magicresreduction
    
        opponent.health-=abs((1-opponent.armor*0.05)*physicaldmg)
        opponent.health-=(1-opponent.magicalres*0.02)*magicaldmg 
    def usespell(self,opponent):#use spell and do damage to the player
        if self.state==True and self.location==opponent.location:         
            arr=self.info[self.name]['ABILITIES']
            rand=npr.randint(0,len(arr))
            for num,val in enumerate(arr):
                if num==rand:
                    self.givedamage(opponent,arr[val].get('magicresreduction'),arr[val].get('armorreduction'),arr[val].get('physicaldmg'),arr[val].get('magic damage'))
                    print(f"{arr[val]['Description']} ")
    def takedamagefromplayer(self,opponent,name):
        if self.State==False:
            self.State=True
        print("ATTACKED")
        for vals in opponent.items:
            if (name==vals.name) and (vals.fight==1):
                self.takedamage(vals.physicaldmg,vals.magicaldmg)
                print(self.health)
                
                
    def updatestate(self,opp):
        
        for x in opp.items:
            if x.name=='TimeStopper' or self.health<100:
                self.state=True
            
        
    def interactplayer(self,opponent):
        
        if self.state==False:
            
            print("HARSH GROANING NOISES COME OUT")
        else:
            self.usespell(opponent)
