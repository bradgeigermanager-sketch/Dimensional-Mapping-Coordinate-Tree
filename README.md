# Dimensional Mapping Coordinate Tree

A hybrid geometric engine that transforms strict 10‑dimensional coordinates into a 
4D hybrid manifold and then into a 3D tree‑based visualization.

This project includes:

- A full Python backend for 10D coordinate handling
- A hybrid geometry engine
- Collapse modes (standard, radial shell, hybrid)
- A relational projection engine
- A tree‑based visualization system
- A browser‑based UI for interactive exploration
- A complete documentation suite
- Sample datasets

---

## 🚀 Quick Start

### Run the UI
Open:
ui/index.html

No build step. No dependencies.

### Use the Python Engine

```python
from engine.HybridGeometry import hybrid_distance

d = hybrid_distance(pointA, pointB)
print(d)
