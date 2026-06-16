from dataclasses import dataclass
import numpy as np

@dataclass
class Vector10D:
    x: float
    y: float
    z: float
    w: float
    v: float
    u: float
    q: float
    p: float
    s: float
    f: float

    def to_array(self):
        return np.array([
            self.x, self.y, self.z, self.w,
            self.v, self.u, self.q, self.p,
            self.s, self.f
        ])

    def radial(self):
        return abs(self.w)

    def relational(self):
        return np.array([self.v, self.u, self.q, self.p, self.s, self.f])
