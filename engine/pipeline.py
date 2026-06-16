from .projection import project_to_hybrid
from .pca import PCAProjector

def run_pipeline(points, mode="hybrid"):
    """
    mode:
      - "hybrid" (your original system)
      - "pca" (new)
    """

    if mode == "hybrid":
        return [project_to_hybrid(p) for p in points]

    elif mode == "pca":
        projector = PCAProjector(n_components=3)
        projector.fit(points)
        return projector.transform(points)

    else:
        raise ValueError("Unknown mode")
