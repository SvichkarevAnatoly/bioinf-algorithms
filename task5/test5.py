import unittest

import agp_alignment as agpa


class Test(unittest.TestCase):
    def test_sample(self):
        v, w = "PRTEINS", "PRTWPSEIN"
        align, score = agpa.alignment(v, w)

        self.assertEqual(8, score)
        self.assertEqual("PRT---EINS", align[v])
        self.assertEqual("PRTWPSEIN-", align[w])
