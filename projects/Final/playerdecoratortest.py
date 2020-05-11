from player import Player
from playerdecorator import PlayerDecorator
from orcs import Orc
from elves import Elf
import unittest

class playerdecoratorTest(unittest.TestCase):

    def testDefaults(self):
        orc = Orc()
        elf = Elf()
        playerdecorator1 = PlayerDecorator(orc)
        playerdecorator2 = PlayerDecorator(elf)
        self.assertEqual(playerdecorator1.decorated_player.Role,"none")
        self.assertEqual(playerdecorator2.decorated_player.Role,"none")
        self.assertEqual(playerdecorator1.decorated_player.Faction,"Orc")
        self.assertEqual(playerdecorator2.decorated_player.Faction,"Elf")

    def testSpecificOrc(self):
        orc = Orc("Hunky")
        orc.SetRole = "Wingman"
        playerdecorator = PlayerDecorator(orc)
        self.assertEqual(playerdecorator.decorated_player.Faction,"Orc")
        self.assertEqual(playerdecorator.decorated_player.Role,"Wingman")
        self.assertEqual(playerdecorator.decorated_player.TuskType,"Hunky")


    def testSpecificElf(self):
        elf = Elf("Nature Communication")
        elf.SetRole = "Advisor"
        playerdecorator = PlayerDecorator(elf)
        self.assertEqual(playerdecorator.decorated_player.Faction,"Elf")
        self.assertEqual(playerdecorator.decorated_player.Role,"Advisor")
        self.assertEqual(playerdecorator.decorated_player.ElvishBlessing,"Nature Communication")