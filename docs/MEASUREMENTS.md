# Measurement System

This document describes the hybrid measurement suite.

## 1. Pairwise Measurements
For points `A` and `B`:

**Radial Delta**
Δr = |wB| - |wA|

**Relational 3D Delta**
ΔX, ΔY, ΔZ

**Relational Distance**
d_rel = sqrt(ΔX^2 + ΔY^2 + ΔZ^2)

**Hybrid Distance**
d = sqrt(Δr^2 + d_rel^2)

**Hybrid Angle**
θ = arccos( (A·B) / (|A||B|) )

## 2. Multi-Point Chains
Given points `A → B → C → D` the system computes:
- Pairwise hybrid distances
- Pairwise hybrid angles
- Branch split points
- Radial progression
- Relational progression

## 3. Branch Split Detection
The branch split is identified by radial divergence `|Δr|`.
