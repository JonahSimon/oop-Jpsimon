import unittest

from head import Head

class   headTest(unittest.TestCase):

    def testDefaults(self):
        head = Head()
        self.assertEqual(head.NumHeads, Head.NUMBER_OF_HEADS)
        self.assertEqual(head.HP, Head.HIT_POINTS)
        self.assertEqual(head.crippled, Head.CRIPPLED)
        
    def testSpecific(self):
        testHeads : int = 3
        testHp : int = 25
        head = Head(heads = testHeads, hp = testHp)
        self.assertEqual(head.NumHeads, testHeads)
        self.assertEqual(head.hp, testHp)
        self.assertEqual(head.crippled,False)

    def testDead(self):
        head = Head()
        self.assertEqual(head.crippled,False)
        head.hp = 0
        self.assertEqual(head.HP,0)
        self.assertEqual(head.crippled,True)
        head.hp = 1000
        self.assertEqual(head.HP,0)
        self.assertEqual(head.crippled,True)

if __name__ == '__main__':
    unittest.main()


