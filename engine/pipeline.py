from .projection import project_to_hybrid

def run_pipeline(points):
    hybrid_points = []

    for p in points:
        h = project_to_hybrid(p)
        hybrid_points.append(h)

    return hybrid_points
