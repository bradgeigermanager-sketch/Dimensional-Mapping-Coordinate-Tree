from .hybrid_geometry import hybrid_distance, hybrid_angle

def chain_measurements(points):
    """
    Compute pairwise hybrid distances and angles for a sequence of points.
    points: iterable of Coordinate10D instances
    Returns a list of dicts with measurement results for each adjacent pair.
    """
    results = []
    for A, B in zip(points, points[1:]):
        results.append({
            "A": getattr(A, "label", None),
            "B": getattr(B, "label", None),
            "radial_A": abs(A.w),
            "radial_B": abs(B.w),
            "hybrid_distance": hybrid_distance(A, B),
            "hybrid_angle": hybrid_angle(A, B)
        })
    return results
