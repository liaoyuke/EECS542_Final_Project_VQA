import numpy as np
from sklearn.cross_decomposition import CCA
from sklearn.externals import joblib

A1 = np.array(np.random.rand(100000,5000),dtype = "f2")
A2 = np.array(np.random.rand(100000,5000),dtype = "f2")

A3 = A1.tolist()
A4 = A2.tolist()
cca = CCA(n_components=1000)
cca.fit(A3,A4)




