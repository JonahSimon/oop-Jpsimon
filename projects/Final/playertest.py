from player import Player
import unittest

class playerTest(unittest.TestCase):

    def testDefaults(self):
        player = Player()
        self.assertEqual(player._faction, "none")
        self.assertEqual(player._role, "none")


    def testSpecific(self):
        player = Player("Human","Warrior")
        self.assertEqual(player._faction, "Human")
        self.assertEqual(player._role, "Warrior")

    def testFaction(self):
        player = Player()
        self.assertEqual(player._faction, "none")
        player.SetFaction = "Dwarf"
        self.assertEqual(player._faction, "Dwarf")

    def testRole(self):
        player = Player()
        self.assertEqual(player._role , "none")
        player.SetRole = "Healer"
        self.assertEqual(player._role, "Healer")

        



