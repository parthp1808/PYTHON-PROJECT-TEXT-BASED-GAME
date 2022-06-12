# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:29:08 2022

@author: ranit
"""

from character import character
from creature import creature
from item import item
from nuggets import nuggets
from fileloader import fileloader


class mapgame:

    def __init__(self):
        loader = fileloader()
        self.characterf = loader.characterdicinstance()
        self.creatures = loader.creaturedicinstance()
        self.items = loader.itemsdicinstance()
        self.map1dic = loader.mapinstance()
        self.nuggetdic = loader.nuggetsinstance()

    def charactercreator(self):

        objlist = []
        for keyz in self.characterf.keys():
            keyz1 = character(keyz, self.characterf[keyz]['STATS'].get('magicalres'),
                              self.characterf[keyz]['STATS'].get('armor'), self.characterf[keyz].get('location'),
                              self.characterf[keyz]['ABILITIES'], self.characterf[keyz].get('State'))
            objlist.append(keyz1)
        return objlist

    def creaturecreator(self):  # create objects for the creatures

        objlist = []
        for keyz in self.creatures.keys():
            if self.creatures[keyz].get('location') != "":
                keyz1 = creature(keyz, self.creatures[keyz]['STATS'].get('magicalres'),
                                 self.creatures[keyz]['STATS'].get('armor'), self.creatures[keyz].get('location'),
                                 self.creatures[keyz].get('ABILITIES'), self.creatures[keyz]['STATS'].get('STATE'))
                objlist.append(keyz1)
        return objlist

    def itemcreator(self, name):

        statsitems = self.items[name]['STATS']
        obj = item(name, statsitems.get('heal'), statsitems.get('physicaldmg'), statsitems.get('magicaldmg'),
                   statsitems.get('magicalres'), statsitems.get('armor'), statsitems.get('location'),
                   statsitems.get('FIGHT'), statsitems.get('State'))

        return obj

    def nuggetcreator(self):  ##WORJK ON THIS STUFF

        objlist = []
        for keyz in self.nuggetdic.keys():
            keyz1 = nuggets(keyz, self.nuggetdic[keyz]['LOOK'], self.nuggetdic[keyz]['verb'],
                            self.itemcreator(self.nuggetdic[keyz]['items']), self.nuggetdic[keyz]['LOCATION'])
            objlist.append(keyz1)
        return objlist

    def mapgenerator(self):  # generates map with creatures and rooms in specific place.BASE FOR ALL FYH
        characters = self.charactercreator()
        creatures = self.creaturecreator()
        nugs = self.nuggetcreator()
        itemscreatorarray = []
        [itemscreatorarray.append(self.itemcreator(x)) for x in self.items.keys()]

        gamemap = {}
        for vals in self.map1dic.keys():  # all locations
            gamemap[vals] = {}
            gamemap[vals]["items"] = []
            gamemap[vals]["characters"] = ""
            gamemap[vals]["creatures"] = ""
            gamemap[vals]["nuggets"] = ""

        for keys, vals in self.map1dic.items():
            gamemap[keys]['Surrounding'] = vals
        for people in characters:
            gamemap[people.location]['characters'] = people
        for creats in creatures:
            gamemap[creats.location]['creatures'] = creats
        for its in itemscreatorarray:
            for val in its.location:
                gamemap[val]['items'].append(its)
        for nugget in nugs:
            gamemap[nugget.location]['nuggets'] = nugget
        return gamemap
