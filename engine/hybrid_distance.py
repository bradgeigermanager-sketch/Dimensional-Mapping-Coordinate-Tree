def hybrid_distance(a, b):
    return np.linalg.norm([
        a[0] - b[0],
        a[1] - b[1],
        a[2] - b[2],
        a[3] - b[3]
    ])
