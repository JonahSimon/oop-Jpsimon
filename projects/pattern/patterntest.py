import unittest

from pattern import Publisher
from pattern import Subscriber

class patternTest(unittest.TestCase):

    def testPattern(self):
        publisher = Publisher()
        publisher2 = Publisher()
        subscriber1 = Subscriber(publisher)
        subscriber2 = Subscriber(publisher)
        subscriber3 = Subscriber(publisher)
        subscriber4 = Subscriber(publisher2)
        self.assertEquals(len(publisher.subscribers),3)
        publisher.update_subscribers('Test')
        self.assertEqual(subscriber1.recived,True)
        self.assertEqual(subscriber2.recived,True)
        self.assertEqual(subscriber3.recived,True)
        self.assertEqual(subscriber4.recived,False)
        publisher2.update_subscribers('Test')
        self.assertEqual(subscriber4.recived,True)


        