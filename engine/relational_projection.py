import numpy as np

# Stable 6D -> 3D projection matrix
P = np.array([
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1]
], dtype=float)

# Normalize rows
P = P / np.linalg.norm(P, axis=1, keepdims=True)

def relational3D(point):
    """
    Project (v, u, q, p, s, f) into a stable 3D relational space.
    Returns a length-3 numpy array [Xrel, Yrel, Zrel].
    """
    H = np.array([point.v, point.u, point.q, point.p, point.s, point.f], dtype=float)
    return P.dot(H)
