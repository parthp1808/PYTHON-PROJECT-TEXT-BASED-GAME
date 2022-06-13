# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 23:47:08 2022

@author: ranit
"""
from fileloaderfactory import fileloaderfactory
class fileloader:
    def __init__(self):
        
        self.val=fileloaderfactory()
        
    def fileloaderinst(self,name):
        if name=='character':
            return self.val.characterdicinstance()
        elif name=='creature':
            return self.val.creaturedicinstance()
        elif name=='item':
            return self.val.itemsdicinstance()
        elif name=='map':
            return self.val.mapinstance()
        elif name=='mapques':
            return self.val.mapquesinstance()
        elif name=='phrase':
            return self.val.phrasesinstance()
        elif name=='nugget':
            return self.val.nuggetsinstance()
            