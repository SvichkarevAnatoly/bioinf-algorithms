import unittest
import l_alignment as la


class Test(unittest.TestCase):
    def test_simple(self):
        v = "ACT"
        w = "ATT"
        align, score = la.alignment(v, w)
        self.assertEqual(1, score)
        self.assertEqual("ACT", align[v])
        self.assertEqual("ATT", align[w])

    def test_rosalind(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        align, score = la.alignment(v, w)
        self.assertEqual(3, score)
        self.assertEqual("PLEAS--ANTLY", align[v])
        self.assertEqual("-----MEAN-LY", align[w])

    def test_from_wiki(self):
        # https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
        v = "ACACACTA"
        w = "AGCACACA"
        align, score = la.alignment(v, w)
        self.assertEqual(5, score)
        self.assertEqual("A-CACACTA", align[v])
        self.assertEqual("AGCACAC-A", align[w])


if __name__ == '__main__':
    unittest.main()
