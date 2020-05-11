from player import Player
import unittest
from typing import cast
from orcs import Orc

class orcTest(unittest.TestCase):

    def testDefaults(self):
        orc = Orc()
        self.assertEqual(orc.Faction, "Orc")
        self.assertEqual(orc.TuskType, "none")
        self.assertEqual(orc.Role, "none")


    def testSpecific(self):
        orc = Orc("WarTorn")
        self.assertEqual(orc._faction, "Orc")
        self.assertEqual(orc._tusktype, "WarTorn")
        self.assertEqual(orc._role, "none")

    def testTuskType(self):
        orc = Orc()
        self.assertEqual(orc._tusktype, "none")
        orc.SetTuskType = "Engraved"
        self.assertEqual(orc._tusktype, "Engraved")

    def testOrcPlayerFaction(self):
        player : Player = Orc()
        orc : Orc = cast(Orc,player)
        self.assertEqual(orc._tusktype , "none")
        orc.SetFaction = "Independent"
        self.assertEqual(orc._faction, "Independent")

        



