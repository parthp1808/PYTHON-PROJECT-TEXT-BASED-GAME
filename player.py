# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:32:07 2022

@author: ranit
"""

from actor import actor
from fileloader import fileloader
from nltk.tokenize import word_tokenize
from mapgame import mapgame


class player(actor):

    def __init__(self):
        loader = mapgame()
        loader1 = fileloader()
        self.dict1 = loader.mapgenerator()

        super().__init__(magicalres=2, armor=5, location=list(self.dict1.keys())[0],
                         state=False)  # initialiting the player with magic power and location
        self.visited = set()  # set to avoid duplicates
        self.quesdic = loader1.mapquesinstance()
        self.gameitems = (loader1.itemsdicinstance())
        self.nuggets = loader1.nuggetsinstance()

    def revealnugget(self):
        self.dict1[self.location]['items'].append(self.dict1[self.location]['nuggets'].items)
        print(
            f"Wow there is a new {self.dict1[self.location]['nuggets'].items.name} which came out of this {self.dict1[self.location]['nuggets'].name}")

    def seeitemsaround(self):
        for vals in self.dict1[self.location]['items']:
            print(vals.name + '\n')

    def seemap(self):
        print(self.dict1['MAIN YARD']['characters'])

    def movecommand(self, inp):  # move from one room to another

        for vals in self.dict1[self.location]['Surrounding']:
            try:
                self.location = self.dict1[self.location]['Surrounding'][inp]
                break
            except KeyError:
                print("Key not found")

    def displaymoves(self):  # display where u can go from current room and what room you are currently in
        maplist = list(self.dict1[self.location]['Surrounding'])

        print(f"You are in  the {(self.location).lower()}.Your directions from this location are")
        for vals in maplist:
            print(f" {vals}", end="")

    def describeroom(self):
        CYAN = '\033[36m'
        itemarrstring = []
        if self.location not in self.visited:
            for keys, vals in self.quesdic.items():
                if (keys == self.location):
                    print(CYAN + vals.get('descr1'))
                    break
        self.visited.add(self.location)
        if self.dict1[self.location]['characters'] != '':
            print(f"{CYAN}The people I see around are {self.dict1[self.location]['characters'].name}")
        else:
            print("There seems to be no signs of intelligent life anywhere around here")
        if self.dict1[self.location]['creatures'] != '':
            print(f"Oh i see a disgusting {self.dict1[self.location]['creatures'].name}")
        if self.dict1[self.location]['nuggets'] != '':
            print(
                f"There lies a {self.dict1[self.location]['nuggets'].name}.{self.dict1[self.location]['nuggets'].descr}")
        for vals2 in self.dict1[self.location]['items']:
            itemarrstring.append(vals2.name)
        print("The items I see around here are", ",".join(itemarrstring))

    def pickitem(self, item1s):
        selfitemsarray = [x.name for x in self.items]
        for vals in self.dict1[self.location]['items']:
            if vals.name == item1s and item1s not in selfitemsarray:
                self.items.append(vals)

                print(f"The item {item1s} was added to the inventory")
                break
        else:
            print('CANT PICK ITEM.NOT AVAILABLE IN AREA or you already have it')

    def useitem(self, name):  # does not involve fighting with item
        for num, item1 in enumerate(self.items):
            if name == 'Chest':
                item1.chestopener(self)
                break
            if name == 'Maraudersmap':
                print(f"The shortest path to your destiny to reach voldemort is\n")
                for vals in self.dict1[self.location]['items'][0].maraudersmap(self):
                    print(vals + "----->", end='')
                print("destiny")
                break
            if name == item1.name and item1.fight == 0:
                self.health += self.gameitems[name]['STATS']['heal']
                if self.health > 100:
                    self.health == 100
                self.magicalres += self.gameitems[name]['STATS']['magicalres']
                self.armor += self.gameitems[name]['STATS']['armor']
            self.items.pop(num)

        for item2 in self.items:
            if item2.fight == 1:
                item2.physicaldmg += self.gameitems[name]['STATS']['physicaldmg']
                item2.magicaldmg += self.gameitems[name]['STATS']['magicaldmg']

    def marauder(self):
        return self.dict1[self.location]['items'][0].maraudersmap(self)

    def checkinventory(self):
        for vals in self.items:
            print(vals.name, end="")

    def inputparser(self):
        print(self.location)
        self.describeroom()

        while self.health > 0 or self.dict1['SlYTHERIN DORM']['creatures'].health <= 0:

            if self.dict1[self.location]['creatures'] != "":
                self.dict1[self.location]['creatures'].updatestate(self)
                self.dict1[self.location]['creatures'].usespell(self)
            userinput = input()

            inp = word_tokenize(userinput)
            textitemarray = []
            [textitemarray.append(x.name) for x in self.items]
            if userinput in ['N', 'S', 'E', 'W']:
                self.movecommand(userinput)
                self.describeroom()
                self.displaymoves()
            elif userinput == 'health':
                print(self.health)
            elif userinput == 'see items':
                self.seeitemsaround()
            else:

                verb = inp[0]
                noun = ' '.join(inp[1:])

                if verb == 'pick':
                    self.pickitem(noun)

                elif noun.split()[-1] == 'inventory':
                    self.checkinventory()
                elif verb == 'interact' and (noun.split()[-1] == self.dict1[self.location]['characters'].name):
                    self.dict1[self.location]['characters'].interactplayer(self)
                elif verb == 'interact' and (noun.split()[-1] == self.dict1[self.location]['creatures'].name):
                    self.dict1[self.location]['creatures'].interactplayer(self)

                elif noun in list(self.gameitems) and verb in self.gameitems[noun]['STATS']['verb'] and \
                        self.gameitems[noun]['STATS']['FIGHT'] == 0:
                    self.useitem(noun)
                elif self.dict1[self.location]['characters'] != '' and len(inp) == 3:
                    (noun.split()[-1] == (self.dict1[self.location]['characters']).name) and (
                                noun.split()[0] in textitemarray)

                    self.dict1[self.location]['characters'].takedamage(
                        self.gameitems[noun.split()[0]]['STATS']['physicaldmg'],
                        self.gameitems[noun.split()[0]]['STATS']['magicaldmg'])

                elif self.dict1[self.location]['creatures'] != '' and len(inp) == 3:
                    noun.split()[-1] == (self.dict1[self.location]['creatures']).name and (
                                noun.split()[0] in textitemarray)

                    self.dict1[self.location]['creatures'].takedamage(
                        self.gameitems[noun.split()[0]]['STATS']['physicaldmg'],
                        self.gameitems[noun.split()[0]]['STATS']['magicaldmg'])

                elif self.location == self.nuggets[noun]['LOCATION'] and verb in self.nuggets[noun]['verb']:
                    self.revealnugget()


# =============================================================================
# 
# loader=mapgame()
# a=player()
# a.movecommand('W')
# 
# g=loader.itemcreator('Maraudersmap')
# x=g.maraudersmap(a)
# for vals in x:
#     print(vals)
# 
# 
# =============================================================================
a = player()
a.inputparser()
