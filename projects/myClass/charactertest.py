import unittest

from  character import Character
from hero import Hero
from monster import Monster
from typing import cast,List

class CharacterTest(unittest,TestCase):

    def testHeroDead(self):
        hero = Hero()
        self.assertEqual(hero.Dead,False)
        hero.hp = 0
        self.assertEqual(hero.Dead,True)
        hero.hp = 1000
        self.assertEqual(hero.Dead,True)
        hero.SetAlive()
        self.assertEqual(hero.Dead,False)
        hero.SetPower = "Immortal"
        hero.hp = 0
        self.assertEqual(hero.Dead,False)



        
    def testMonstersAndHeros(self):
        players : List[Character]=[]
        players.append(Monster())
        players.append(Hero())
        hero = Hero()
        hero.hp = 0
        hero.SetPower = "Immortal"
        players.append(hero)
        for player in players:
            self.assertEqual(player.Dead,False)

        hero : Hero = cast(Hero,players[2])
        hero.SetDead()
        self.assertEqual(players[1].Dead,True)   



if __name__ == '__main__':
    unittest.main()
