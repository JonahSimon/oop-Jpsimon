from character import Character
import unittest

from typing import cast
from monster import Monster

class monsterTest(unittest.TestCase):

    def testDefaults(self):
        monster = Monster()
        self.assertEqual(monster._arms, Monster.NUMBER_OF_ARMS)
        self.assertEqual(monster._legs, Monster.NUMBER_OF_LEGS)
        self.assertEqual(monster._heads, Monster.NUMBER_OF_HEADS)
        self.assertEqual(monster._health, Monster.HIT_POINTS)
        self.assertEqual(monster._color, Monster.COLOR)
        self.assertEqual(monster._dead, False)

    def testSpecific(self):
        testHeads : int = 3
        testHp : int = 25
        monster = Monster(heads = testHeads, hp = testHp)
        self.assertEqual(monster.NumHeads, testHeads)
        self.assertEqual(monster.HP, testHp)
        self.assertEqual(monster.Dead,False)

    def testDead(self):
        monster = Monster()
        self.assertEqual(monster.Dead,False)
        monster.hp = 0
        self.assertEqual(monster.HP,0)
        self.assertEqual(monster.Dead,True)
        monster.hp = 1000
        self.assertEqual(monster.HP,0)
        self.assertEqual(monster.Dead,True)

    def testMonsterCharacterDead(self):
        character : Character = Monster()
        monster : Monster = cast(Monster,character)
        monster.hp = 0
        self.assertEqual(monster.HP,0)
        self.assertEqual(character.Killed,True)
        self.assertEqual(monster.Killed,True)


if __name__ == '__main__':
    unittest.main()


