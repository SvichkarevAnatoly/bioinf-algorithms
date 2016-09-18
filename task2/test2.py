import unittest
import g_alignment as ga


class Test(unittest.TestCase):
    def test_from_lecture(self):
        v = "AKRANR"
        w = "KAAANK"
        align, score = ga.alignment(v, w)
        self.assertEqual(18, score)
        self.assertEqual("AKRA--NR", align[v])
        self.assertEqual("-K-AAANK", align[w])


if __name__ == '__main__':
    unittest.main()
