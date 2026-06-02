class Coordinate10D:
    """
    Strict 10D coordinate representation.
    Dimensions:
      x, y, z — collapsed spatial axes
      w — radial shell dimension
      v, u, q, p, s, f — relational axes
    """
    def __init__(self, x, y, z, w, v, u, q, p, s, f, label=None):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)
        self.v = float(v)
        self.u = float(u)
        self.q = float(q)
        self.p = float(p)
        self.s = float(s)
        self.f = float(f)
        self.label = label or "10D_Node"

    def to_vector(self):
        return [self.x, self.y, self.z, self.w, self.v, self.u, self.q, self.p, self.s, self.f]

    def __repr__(self):
        return f"<10D {self.label}: {self.to_vector()}>"
