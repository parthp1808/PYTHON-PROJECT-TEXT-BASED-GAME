# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:30:22 2022

@author: ranit
"""
from actor import actor
from fileloader import fileloader
import numpy.random as npr
class creature(actor): #creature class 
    def __init__(self,name,look,magicalres,armor,location,abilities,state):
        loader=fileloader()
        super().__init__(name,magicalres,armor,location,state)
        self.abilities=abilities
        self.look=look
        
        self.info=loader.fileloaderinst('creature')
    
        
    def damagecalculatorhelperfunc(self,physicaldmg,magicaldmg):
        self.health-=abs((1-self.armor*0.05)*physicaldmg)
        self.health-=abs(1-self.magicalres*0.02)*magicaldmg 
        print(f"{self.name} just took damage")
        
    def givedamage(self,opponent,magicresreduction,armorreduction,physicaldmg,magicaldmg): #possibly override.give damage to opponent
        opponent.armor-=armorreduction
        opponent.magicalres-=magicresreduction
    
        opponent.health-=abs((1-opponent.armor*0.05)*physicaldmg)
        opponent.health-=(1-opponent.magicalres*0.02)*magicaldmg 
    def usespell(self,opponent):#use spell and do damage to the player
        
            if self.state==True:
                arr=self.info[self.name]['ABILITIES']
                rand=npr.randint(0,len(arr))
                for num,val in enumerate(arr):
                    if num==rand:
                        self.givedamage(opponent,arr[val].get('magicresreduction'),arr[val].get('armorreduction'),arr[val].get('physicaldmg'),arr[val].get('magic damage'))
                        print(f"{arr[val]['Description']} ")
    def takedamagefromplayer(self,opponent):
        
        if self.state!=True and self.state!=False:
           if self.location==opponent.location:
               print('I am not here to hurt you or fight you.I am here to talk to you')
        for vals in opponent.items:
            if (vals.state==True) and (vals.fight==1):
                self.usespell(opponent)
                if self.state==False:
                    self.state=True
                self.damagecalculatorhelperfunc(vals.physicaldmg,vals.magicaldmg)
                return
        print('CANNOT Attack without proper Equipment')
            
    def alivechecker(self):
       if self.health<=0:
           print(f'DEATH ON {self.name}')
           return False
       return True
           
       
    def updatestate(self,opp):
        
        for x in opp.items:
            if x.name=='TimeStopper' and self.state==False:
                self.state=True
        
        
    def interactplayer(self,opponent):
        
        if self.state!=True:
            
            print("HARSH GROANING NOISES COME OUT")
        
        if self.state==True and self.location==opponent.location:
            self.usespell(opponent)
        
    