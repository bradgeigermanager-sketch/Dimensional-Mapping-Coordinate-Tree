def enforce_linear_constraint(v, factor=1.0):
    v.u = v.v * factor
    return v

def enforce_inverse_constraint(v):
    if v.q != 0:
        v.p = 1 / v.q
    return v
