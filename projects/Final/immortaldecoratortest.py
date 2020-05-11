from playerdecorator import PlayerDecorator
import unittest
from elves import Elf
from orcs import Orc
from immortaldecorator import ImmortalDecorator

class immortalplayerdecoratorTest(unittest.TestCase):
    def testDefaults(self):
        orc = Orc()
        playerdecorator1 = PlayerDecorator(orc)
        immortalplayerdecorator1 = ImmortalDecorator(playerdecorator1)
        elf = Elf()
        playerdecorator2 = PlayerDecorator(elf)
        immortalplayerdecorator2 = ImmortalDecorator(playerdecorator2)
        self.assertEqual(immortalplayerdecorator1.decorated_player.decorated_player.Faction,"Orc")
        self.assertEqual(immortalplayerdecorator2.decorated_player.decorated_player.Faction,"Elf")
        self.assertEqual(immortalplayerdecorator1.decorated_player.decorated_player.Role,"none")
        self.assertEqual(immortalplayerdecorator2.decorated_player.decorated_player.Role,"none")
        self.assertEqual(immortalplayerdecorator1.Immortal(),True)
        self.assertEqual(immortalplayerdecorator2.Immortal(),True)


    def testOrcSpecific(self):
        orc = Orc("Gargantuan")
        orc.SetRole = "Care Taker"
        playerdecorator = PlayerDecorator(orc)
        immortalplayerdecorator = ImmortalDecorator(playerdecorator)
        self.assertEqual(immortalplayerdecorator.decorated_player.decorated_player.Faction,"Orc")
        self.assertEqual(immortalplayerdecorator.decorated_player.decorated_player.Role,"Care Taker")
        self.assertEqual(immortalplayerdecorator.decorated_player.decorated_player.TuskType, "Gargantuan")
        self.assertEqual(immortalplayerdecorator.Immortal(),True)

    def testElfSpecific(self):
        elf = Elf("Clairvoyance")
        elf.SetRole = "Peace Keeper"
        playerdecorator = PlayerDecorator(elf)
        immortalplayerdecorator = ImmortalDecorator(playerdecorator)
        self.assertEqual(immortalplayerdecorator.decorated_player.decorated_player.Faction,"Elf")
        self.assertEqual(immortalplayerdecorator.decorated_player.decorated_player.Role,"Peace Keeper")
        self.assertEqual(immortalplayerdecorator.decorated_player.decorated_player.ElvishBlessing, "Clairvoyance")
        self.assertEqual(immortalplayerdecorator.Immortal(),True)