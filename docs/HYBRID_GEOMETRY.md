# Hybrid Geometry Specification

This document defines the hybrid 4D manifold used by the engine.

## 1. Purpose
The hybrid geometry provides a meaningful way to compare 10D points by:
- Collapsing the first 3 dimensions
- Treating the 4th dimension as radial distance
- Projecting the remaining 6 dimensions into a 3D relational space

## 2. Radial Shell
The first four dimensions collapse into:
r = |w|
This defines the height of the point.

## 3. Relational 3D Projection
The relational dimensions:
(v, u, q, p, s, f)
are projected into 3D using a stable matrix `P`:
(Xrel, Yrel, Z_rel) = P · (v,u,q,p,s,f)

## 4. Hybrid Vector
The hybrid vector is:
H = (r, Xrel, Yrel, Z_rel)
This is the canonical representation for:
- Distances
- Angles
- Tree visualization
- Measurement chains

## 5. Hybrid Distance
d = sqrt( (Δr)^2 + (ΔX)^2 + (ΔY)^2 + (ΔZ)^2 )

## 6. Hybrid Angle
θ = arccos( (A·B) / (|A||B|) )
Where `A` and `B` are hybrid vectors.

## 7. Interpretation
- Points with similar `|w|` lie on the same “branch level”
- Points with similar relational 3D values cluster horizontally
- The geometry is interpretable and stable
