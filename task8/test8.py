import unittest
import knuth_morris_pratt as kmp


class Test(unittest.TestCase):
    def test_prefix(self):
        s = "abcdabcabcdabcdab"
        self.assertEqual(
            [0, 0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6],
            kmp.prefix(s))

    def test_middle_prefix(self):
        s = "abcabgabcabc"
        sub = "abcabc"
        self.assertEqual(6, kmp.search(s, sub))

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
