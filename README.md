# Dimensional Tracking Engine

Hybrid 10D → 4D → 3D Visualization & Analysis Framework

## Overview

The Dimensional Tracking Engine is a full-stack system for representing, transforming, visualizing, and comparing entities in 10-dimensional space. It includes:

- A strict 10D coordinate engine
- Dimensional entanglement constraints
- Multiple collapse modes
- A hybrid geometry manifold (radial shell + relational 3D)
- A tree visualization system
- A measurement suite for distances, angles, and branch analysis
- A complete web UI with rotation, zoom, and interactive controls

This repository contains both the Python backend and the HTML/JS frontend.

## Key Concepts

### 10D Vector Structure

Each point is represented as:
(x, y, z, w, v, u, q, p, s, f)

- x,y,z — collapsed spatial axes
- w — radial distance from origin
- v,u,q,p,s,f — higher-dimensional relational axes

### Hybrid Geometry (Core Innovation)

The engine defines a 4D hybrid manifold:

1. **Radial Shell** — The first 4 dimensions collapse into a single scalar: `r = |w|`
2. **Relational 3D** — Dimensions 5–10 are projected into a stable 3D space `(Xrel, Yrel, Zrel)`
3. **Hybrid Vector** `H = (r, Xrel, Yrel, Zrel)`

Distances and angles are computed in this 4D space.

### Tree Visualization

The hybrid geometry naturally forms a branching tree:

- The trunk is the collapsed (x,y,z)
- The height is the radial shell (`|w|`)
- The branches are the relational 3D projection
- The leaves are the actual points

This produces a clean, interpretable structure for high-dimensional data.

## Features

- **10D Engine**: Strict indexing, 10D Euclidean distance, vector operations  
- **Entanglement Engine**: Mechanical constraints between dimensions, linear and inverse bonds  
- **Collapse Modes**: Standard 3-axis projection, radial-shell collapse, hybrid geometry mode  
- **Hybrid Visualization**: 3D relational space, radial shell height, rotation controls, zoom controls, metadata hover  
- **Tree Visualization**: Trunk → height → branch spread, 3D rendering, branch-level clustering  
- **Measurements**: Pairwise hybrid distances, hybrid angles, multi-point measurement chains, branch split detection

## Installation

Clone the repository:

```bash
git clone https://github.com/YOURUSERNAME/dimensional-tracking-engine.git
cd dimensional-tracking-engine
Python modules may require:
pip install numpy
No external dependencies are required for the UI.

Running the UI
Open:
ui/index.html
in any modern browser.

Documentation
See the docs/ folder for:

Architecture overview

Hybrid geometry specification

Tree visualization theory

Measurement algorithms

API reference

License
MIT License — see LICENSE for details.
