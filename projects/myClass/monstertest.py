import unittest

from monster import Monster

class monsterTest(unittest.TestCase):

    def testDefaults(self):
        monster = Monster()
        self.assertEqual(monster._arms, Monster.NUMBER_OF_ARMS)
        self.assertEqual(monster._legs, Monster.NUMBER_OF_LEGS)
        self.assertEqual(monster._heads, Monster.NUMBER_OF_HEADS)
        self.assertEqual(monster._health, Monster.HIT_POINTS)
        self.assertEqual(monster._color, Monster.COLOR)
        self.assertEqual(monster._dead, Monster.DEAD)


    def testNegativePressure(self):
        testDiameter : float = 22.0
        testPressure : float = -1
        self.assertRaises(ValueError, lambda : Wheel(diameter = testDiameter, pressure = testPressure))


    def testSpecific(self):
        testDiameter : float = 22.0
        testPressure : float = Wheel.BURST_PRESSURE/2.0
        wheel = Wheel(diameter = testDiameter, pressure = testPressure)
        self.assertEqual(wheel.pressure, testPressure)
        self.assertEqual(wheel.diameter, testDiameter)
        self.assertEqual(wheel.burst,False)
        self.assertEqual(wheel.flat,False)


    def testFlat(self):
        testPressure = Wheel.BURST_PRESSURE / 2.0
        wheel = Wheel()
        wheel.pressure = testPressure
        self.assertEqual(wheel.pressure, testPressure)
        self.assertEqual(wheel.flat, False)
        wheel.pressure = 0.0
        self.assertEqual(wheel.flat, True)


    def testBurst(self):
        wheel = Wheel()
        wheel.pressure = Wheel.BURST_PRESSURE / 2.0
        self.assertEqual(wheel.flat,False)
        self.assertEqual(wheel.burst,False)
        wheel.pressure = Wheel.BURST_PRESSURE
        self.assertEqual(wheel.pressure,0.0)
        self.assertEqual(wheel.flat,True)
        self.assertEqual(wheel.burst,True)
        wheel.pressure = Wheel.BURST_PRESSURE / 2.0
        self.assertEqual(wheel.pressure,0.0)
        self.assertEqual(wheel.flat,True)
        self.assertEqual(wheel.burst,True)


if __name__ == '__main__':
    unittest.main()


