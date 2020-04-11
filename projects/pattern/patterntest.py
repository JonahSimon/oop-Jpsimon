import unittest

from pattern import Publisher
from pattern import Subscriber

class patternTest(unittest.TestCase):

    def testPattern(self):
        publisher = Publisher()
        subscriber1 = Subscriber(publisher)
        subscriber2 = Subscriber(publisher)
        subscriber3 = Subscriber(publisher)
        self.assertEquals(len(publisher.subscribers),3)