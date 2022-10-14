import unittest
import math

class OnlineStatistics:
    def __init__(self):
        self._acc = 0
        self._acc2 = 0
        self._cnt = 0

    def mean(self):
        return self._acc / self._cnt if self._cnt > 0 else math.nan

    def add(self, value):
        self._acc += value
        self._acc2 += value ** 2
        self._cnt += 1
    
    def var(self):
        return (self._acc2 - self._cnt * self.mean() ** 2) / (self._cnt - 1) if self._cnt > 1 else math.nan

class OnlineStatisticsTest(unittest.TestCase):
    def setUp(self):
        self.st = OnlineStatistics()

    def test_MeanIsNan_WhenNoInput(self):
        self.assertTrue(math.isnan(self.st.mean()))

    def test_MeanWhenSingleInput(self):
        self.st.add(0)
        self.assertAlmostEqual(0, self.st.mean()) # Comparación flotante

    def test_MeanWhenTwoInputs(self):
        self.st.add(1)
        self.st.add(2)
        self.assertAlmostEqual(1.5, self.st.mean())

    def test_VArIsNan_WhenNoInput(self):
        self.assertTrue(math.isnan(self.st.var()))
    
    def test_VarIsNan_WhenSingleInput(self):
        self.st.add(1)
        self.assertTrue(math.isnan(self.st.var()))

    def test_Var_WhenTwoInputs(self):
        self.st.add(1)
        self.st.add(2)
        self.assertAlmostEqual(0.5, self.st.var())


if __name__ == '__main__':
    unittest.main()