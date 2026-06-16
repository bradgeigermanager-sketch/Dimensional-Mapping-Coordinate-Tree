# Dimensional Tracking Engine — Architecture

This document describes the full architecture of the Dimensional Tracking Engine, including the 10D coordinate system, hybrid geometry, visualization pipeline, and measurement subsystems.

## 1. System Overview
The engine represents entities in 10-dimensional space:
(x, y, z, w, v, u, q, p, s, f)
The system provides:
- A strict 10D coordinate class
- Dimensional entanglement constraints
- Multiple collapse modes
- A hybrid 4D manifold
- A relational 3D projection
- A radial-shell tree visualization
- A measurement suite
- A full web UI

## 2. Dimensional Semantics
**Collapsed Spatial Dimensions (x, y, z)**  
These dimensions collapse into a shared origin and do not contribute to distance.

**Radial Shell Dimension (w)**  
Defines the height of a point in the hybrid manifold:
r = |w|

**Relational Dimensions (v, u, q, p, s, f)**  
These form a 6D relational space, projected into 3D.

## 3. Hybrid Geometry
The hybrid manifold is defined as:
H = (r, Xrel, Yrel, Z_rel)
Where:
- `r = |w|`
- `(Xrel, Yrel, Z_rel)` is the 3D projection of `(v,u,q,p,s,f)`

Distances and angles are computed in this 4D space.

## 4. Visualization Pipeline
**Hybrid Visualization**
- 3D relational space
- Radial shell height
- Rotation (yaw, pitch, roll)
- Zoom
- Metadata hover

**Tree Visualization**
- Trunk = collapsed (x,y,z)
- Height = |w|
- Branch spread = relational 3D
- Leaves = points

## 5. Measurements
The measurement suite computes:
- Radial deltas
- Relational 3D deltas
- Hybrid 4D distances
- Hybrid 4D angles
- Multi-point chain measurements
- Branch split detection

## 6. UI Architecture
The UI is modular:
- `rotation_controls.js`
- `zoom_controls.js`
- `hybrid_visualization.js`
- `tree_mode.js`
- `measurements_panel.js`

Each module is independent and communicates through shared state.


# Architecture

## Pipeline

1. Load data (10D vectors)
2. Apply constraints
3. Project to hybrid space (4D)
4. Render in 3D

## Modules

- vector.py → data structure
- projection.py → dimensional reduction
- distance.py → measurements
- pipeline.py → orchestration

## Data Flow

JSON → Vector10D → Hybrid → UI
## 7. Data Flow
10D Point → Hybrid Vector → Visualization → Measurements

The system is deterministic, reversible via metadata, and auditable.
