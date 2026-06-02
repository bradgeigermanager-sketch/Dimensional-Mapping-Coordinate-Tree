def radial_shell(point):
    """
    Collapse dims 1–4 into a single scalar: r = |w|
    point is expected to have attribute 'w'
    """
    return abs(point.w)
