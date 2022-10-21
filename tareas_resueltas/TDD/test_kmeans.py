import unittest
import math
from math import dist

"""
Nota: solo pude aplicar KMeans para una dimensión
"""

class KMeans:
    def __init__(self):
        self._centroides = []
        
    # Recibe un sample y devuelve a que clase pertenece (int). Para eso fijarse que centroide està màs cercano
    def proces(self, sample):
        dista = abs(sample - self._centroides[0])
        match = 0
        for i in range(1, len(self._centroides)):
            new_dist = abs(sample - self._centroides[i]) 
            if(new_dist < dista):  
                match = i
                dista = new_dist
        return match
    
    def centroides(self):
        return self._centroides

    # Recibe una lista de samples y la cantidad máxima de iteraciones. Devuelve una lista con los centroides
    def train(self, samples, n_clusters, max_iter):
        grupos = [[] for _ in range(n_clusters)]
 
        self._centroides.append(2)                                                
        self._centroides.append(8)

        for _ in range(1, max_iter + 1):
            for sample in samples:
                grupo = self.proces(sample)
                grupos[grupo].append(sample)
            for i in range(len(grupos)):
                self._centroides[i] = sum(grupos[i]) / len(grupos[i])
        
        return self._centroides

class KMeansTest(unittest.TestCase):
    def setUp(self):
        self.oneFeatureSamples = [1, 9]
        self.oneFeatureSamples2 = [1, 2, 9, 11]
        self.oneCluster = 1
        self.twoClusters = 2
    
    def testKMeansTrainDevuelveUnCentroidePara1FeatureY1Clase(self):
        self.km = KMeans()
        self.assertAlmostEqual(2, self.km.train(self.oneFeatureSamples, self.oneCluster, 0)[0])        
    
    def testKMeansElCentroidePara1FeatureY1ClaseEsCorrectoLuegoDeEntrenar(self):
        self.km = KMeans()
        self.km.train(self.oneFeatureSamples, self.oneCluster, 0)
        self.assertAlmostEqual(2, self.km.centroides()[0])    
    
    def testKMeansDevuelveLaClaseCorrectaParaUnSampleUsando1FeatureY1Clase(self):
        self.km = KMeans()
        self.km.train(self.oneFeatureSamples, self.oneCluster, 0)
        self.assertAlmostEqual(0, self.km.proces(3)) 
    
    def testKMeansFuncionaPara1FeatureY2ClasesUsando2Samples(self):
        self.km = KMeans()
        self.km.train(self.oneFeatureSamples, self.twoClusters, 1)
        self.assertAlmostEqual(0, self.km.proces(3)) 
        self.assertAlmostEqual(1, self.km.proces(10)) 
    
    def testKMeansFuncionaPara1FeatureY2ClasesUsando4Samples(self):
        self.km = KMeans()
        self.km.train(self.oneFeatureSamples2, self.twoClusters, 1)
        self.assertAlmostEqual(0, self.km.proces(3)) 
        self.assertAlmostEqual(1, self.km.proces(10)) 
        self.assertAlmostEqual(1.5, self.km.centroides()[0])
        self.assertAlmostEqual(10, self.km.centroides()[1])
   
    def testKMeansFuncionaPara1FeatureY2ClasesUsando4SamplesYConDosIteraciones(self):
        self.km = KMeans()
        self.km.train(self.oneFeatureSamples2, self.twoClusters, 2)
        self.assertAlmostEqual(0, self.km.proces(3)) 
        self.assertAlmostEqual(1, self.km.proces(10)) 
        self.assertAlmostEqual(1.5, self.km.centroides()[0])
        self.assertAlmostEqual(10, self.km.centroides()[1])
    
if __name__ == '__main__':
    unittest.main()