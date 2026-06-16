import numpy as np
from sklearn.decomposition import PCA

class PCAProjector:
    def __init__(self, n_components=3):
        self.n_components = n_components
        self.model = PCA(n_components=n_components)
        self.fitted = False

    def fit(self, vectors):
        """
        Fit PCA model on dataset
        """
        matrix = np.array([v.to_array() for v in vectors])
        self.model.fit(matrix)
        self.fitted = True

    def transform(self, vectors):
        """
        Transform vectors → reduced dimensions
        """
        if not self.fitted:
            raise ValueError("PCA must be fitted before transform")

        matrix = np.array([v.to_array() for v in vectors])
        reduced = self.model.transform(matrix)

        return reduced
