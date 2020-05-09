from player import Player
import unittest
from typing import cast
from elves import Elf

class elfTest(unittest.TestCase):

    def testDefaults(self):
        elf = Elf()
        self.assertEqual(elf._faction, "Elf")
        self.assertEqual(elf._elvishblessing, "none")
        self.assertEqual(elf._role, "none")


    def testSpecific(self):
        elf = Elf("Time Dilation")
        self.assertEqual(elf._faction, "Elf")
        self.assertEqual(elf._elvishblessing, "Time Dilation")
        self.assertEqual(elf._role, "none")

    def testTuskType(self):
        elf = Elf()
        self.assertEqual(elf._elvishblessing, "none")
        elf.SetElvishBlessing = "Arcane Knowledge"
        self.assertEqual(elf._elvishblessing, "Arcane Knowledge")

    def testOrcPlayerFaction(self):
        player : Player = Elf()
        elf : Elf = cast(Elf,player)
        self.assertEqual(elf._elvishblessing , "none")
        elf.SetFaction = "Independent"
        self.assertEqual(elf._faction, "Independent")

        



