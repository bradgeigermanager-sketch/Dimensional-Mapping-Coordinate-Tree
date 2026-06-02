# Tree Visualization Specification

The tree visualization expresses the hybrid manifold as a branching structure.

## 1. Concept
The tree has three layers:
- **Trunk**: Collapsed `(x,y,z)`
- **Branch Height**: `height = |w|`
- **Branch Spread**: Relational 3D projection of `(v,u,q,p,s,f)`

## 2. Coordinates
X = X_rel * scale
Y = -|w| * scale
Z = Z_rel * scale

## 3. Rendering
- Draw trunk from base to height
- Draw branch horizontally
- Draw leaf node at branch tip

## 4. Behavior
- Points with similar `|w|` appear at same height
- Points with similar relational 3D cluster horizontally
- The tree rotates and zooms with the camera
- Tree mode can be toggled independently

## 5. Use Cases
- Branch analysis
- Cluster visualization
- High-dimensional structure mapping
