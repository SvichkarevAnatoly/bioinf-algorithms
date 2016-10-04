import unittest
import knuth_morris_pratt as kmp


class Test(unittest.TestCase):
    def test_found_at_start(self):
        s = "abracadabra"
        sub = "abr"
        self.assertEqual(0, kmp.search(s, sub))

    def test_found_at_second(self):
        s = "cabracadabra"
        sub = "abr"
        self.assertEqual(1, kmp.search(s, sub))

    def test_found_at_end(self):
        s = "cbracadabr"
        sub = "abr"
        self.assertEqual(7, kmp.search(s, sub))

    def test_not_found(self):
        s = "cbracadab"
        sub = "abr"
        self.assertEqual(-1, kmp.search(s, sub))
