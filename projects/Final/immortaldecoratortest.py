import unittest
from player import Player
from immortaldecorator import ImmortalDecorator

class immortalplayerdecoratorTest(unittest.TestCase):
    def testDefaults(self):
        immortalplayerdecorator = ImmortalDecorator()
        self.assertEqual(immortalplayerdecorator._Immortal,True)

    def testSpecific(self):
        immortalplayerdecorator = ImmortalDecorator("God" , "PeaceKeeper")
        self.assertEqual(immortalplayerdecorator._faction,"God")
        self.assertEqual(immortalplayerdecorator._role,"PeaceKeeper")
        self.assertEqual(immortalplayerdecorator._Immortal,True)

