from .relational_projection import relational3D

def tree_coords(point):
    """
    Tree visualization coordinates:
      height = |w|
      spread = relational3D projection
    Returns (x_rel, height, z_rel)
    """
    height = abs(point.w)
    xr, yr, zr = relational3D(point)
    return (xr, height, zr)
