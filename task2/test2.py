import unittest
import g_alignment as ga


class Test(unittest.TestCase):
    def test_simple(self):
        v = "ACT"
        w = "ATT"
        align, score = ga.alignment(v, w)
        self.assertEqual(1, score)
        self.assertEqual("ACT", align[v])
        self.assertEqual("ATT", align[w])

    def test_from_rosalind(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        align, score = ga.alignment(v, w)
        self.assertEqual(0, score)
        self.assertEqual("PLEASANTLY", align[v])
        self.assertEqual("M-EA--N-LY", align[w])

    def test_from_same_length(self):
        v = "PLEASANTLY"
        w = "LPLEAAANTL"
        align, score = ga.alignment(v, w)
        self.assertEqual(5, score)
        self.assertEqual("-PLEASANTLY", align[v])
        self.assertEqual("LPLEAAANTL-", align[w])


if __name__ == '__main__':
    unittest.main()
