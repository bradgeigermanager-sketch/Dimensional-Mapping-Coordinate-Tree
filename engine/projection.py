import numpy as np

def hybrid_with_pca(points):
    rel_matrix = np.array([p.relational() for p in points])

    pca = PCA(n_components=3)
    rel_3d = pca.fit_transform(rel_matrix)

    hybrid = []

    for i, p in enumerate(points):
        r = abs(p.w)
        Xrel, Yrel, Zrel = rel_3d[i]

        hybrid.append((r, Xrel, Yrel, Zrel))

    return hybrid
