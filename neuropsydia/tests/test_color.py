from unittest import TestCase

import neuropsydia as n
n.start(open_window=False)

class TestColor(TestCase):
    def test_is_string(self):
        s = funniest.joke()
        self.assertTrue(isinstance(s, basestring))