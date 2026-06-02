import numpy as np
from .relational_projection import relational3D

def hybrid_vector(point):
    """
    Hybrid 4D manifold: H = (r, Xrel, Yrel, Zrel)
    """
    r = abs(point.w)
    xr, yr, zr = relational3D(point)
    return np.array([r, xr, yr, zr], dtype=float)

def hybrid_distance(A, B):
    a = hybrid_vector(A)
    b = hybrid_vector(B)
    return float(np.linalg.norm(b - a))

def hybrid_angle(A, B):
    a = hybrid_vector(A)
    b = hybrid_vector(B)
    dot = float(np.dot(a, b))
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    if na == 0 or nb == 0:
        return 0.0
    cos_theta = max(-1.0, min(1.0, dot / (na * nb)))
    return float(np.arccos(cos_theta))
