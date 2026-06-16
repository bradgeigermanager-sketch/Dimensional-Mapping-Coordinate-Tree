import numpy as np

def project_to_hybrid(v):
    """
    Convert 10D vector → hybrid 4D representation
    """

    # Radial component
    r = abs(v.w)

    # Relational dimensions (6D → 3D projection)
    rel = np.array([v.v, v.u, v.q, v.p, v.s, v.f])

    # Simple deterministic projection
    Xrel = rel[0] + rel[1]
    Yrel = rel[2] + rel[3]
    Zrel = rel[4] + rel[5]

    return (r, Xrel, Yrel, Zrel)
``
