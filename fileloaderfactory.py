# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:47:52 2022

@author: ranit
"""
import json
class fileloaderfactory:
    def __init__(self):
        pass
    def loadjson(self,jsonfile):#opens the json and returns an object
        a=open(jsonfile)
        opened=json.load(a)
        
        return opened
    
    def characterdicinstance(self):
        a=self.loadjson('characters.json')
        
        return a['characters']
    
    def creaturedicinstance(self):
        a=self.loadjson('creatures.json')
        return a['creatures']
    
    def itemsdicinstance(self):
        a=self.loadjson('items.json')
        return a['items']
    
    def mapinstance(self):
        a=self.loadjson('map.json')
        
        return a['map']
    
    def mapquesinstance(self):
        a=self.loadjson('mapques.json')
        return a['mapques']
    
    def phrasesinstance(self):
        a=self.loadjson('PHRASES.json')
        return a['PHRASES']

    
    def nuggetsinstance(self):
        a=self.loadjson('nuggets.json')
        return a['nuggets']


