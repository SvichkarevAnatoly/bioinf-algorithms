import unittest
import l_alignment as la


class Test(unittest.TestCase):
    def test_slide(self):
        v = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
        w = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
        align, score = la.alignment(v, w)
        self.assertEqual(12, score)
        self.assertEqual("CAGTTATGTCAG", align[v])
        self.assertEqual("CAGTTATGTCAG", align[w])

    def test_simple(self):
        v = "ACT"
        w = "ATT"
        align, score = la.alignment(v, w)
        self.assertEqual(1, score)
        self.assertEqual("A", align[v])
        self.assertEqual("A", align[w])

    def test_rosalind(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        align, score = la.alignment(v, w)
        self.assertEqual(3, score)
        self.assertEqual("ANTLY", align[v])
        self.assertEqual("AN-LY", align[w])

    def test_rosalind_reversed(self):
        v = "YLTNASAELP"
        w = "YLNAEM"
        align, score = la.alignment(v, w)
        self.assertEqual(3, score)
        self.assertEqual("YLTNA", align[v])
        self.assertEqual("YL-NA", align[w])

    def test_from_wiki(self):
        # https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
        v = "ACACACTA"
        w = "AGCACACA"
        align, score = la.alignment(v, w)
        self.assertEqual(5, score)
        self.assertEqual("ACACA", align[v])
        self.assertEqual("ACACA", align[w])


if __name__ == '__main__':
    unittest.main()
