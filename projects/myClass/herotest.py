from character import Character
import unittest
from hero import Hero
from typing import cast

class HeroTest(unittest.TestCase):

    def testDefaults(self):
        hero = Hero()
        self.assertEqual(hero._arms, Hero.NUMBER_OF_ARMS)
        self.assertEqual(hero._legs, Hero.NUMBER_OF_LEGS)
        self.assertEqual(hero._heads, Hero.NUMBER_OF_HEADS)
        self.assertEqual(hero._health, Hero.HIT_POINTS)
        self.assertEqual(hero._color, Hero.COLOR)
        self.assertEqual(hero._dead, False)

    def testSpecific(self):
        testHeads : int = 3
        testHp : int = 25
        hero = Hero(heads = testHeads, hp = testHp)
        self.assertEqual(hero.NumHeads, testHeads)
        self.assertEqual(hero.HP, testHp)
        self.assertEqual(hero.Dead,False)

    def testDead(self):
        hero = Hero()
        hero.hp = 0
        self.assertEqual(hero.Dead,True)
        self.assertEqual(hero.HP,0)
        
        hero.hp = 100
        self.assertEqual(hero.Dead,True)
        self.assertEqual(hero.HP,0)

        hero.SetAlive()
        hero.hp = 1000
        self.assertEqual(hero.Dead,False)
        self.assertEqual(hero.HP,1000)
        
        hero.SetPower = "Immortal"
        hero.hp = 0
        self.assertEqual(hero.Dead,False)
        self.assertEqual(hero.HP,1000)

        hero.SetPower = "Resurrection"
        hero.hp = 0
        self.assertEqual(hero.Dead,False)
        self.assertEqual(hero.HP,1000)

        

    def testHeroCharacterDead(self):
        character : Character = Hero()
        hero : Hero = (cast(Hero,character))
        hero.hp = 0
        self.assertEqual(hero.HP, 0)
        self.assertEqual(character.Dead, True)
        self.assertEqual(hero.Dead, True)