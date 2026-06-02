class EntanglementEngine:
    """
    Mechanical constraint propagation between dimensions.
    Supports:
      - linear bonds
      - inverse bonds
    """
    def __init__(self):
        self.bonds = {}  # (srcdim, tgtdim) -> config

    def create_bond(self, src, tgt, ratio=1.0, bond_type="linear"):
        self.bonds[(src, tgt)] = {"ratio": ratio, "type": bond_type}

    def process(self, entity, modified_dim, delta):
        """
        Apply entanglement rules when a dimension changes.
        entity: object with attributes for dims (e.g., 'v','u', etc.)
        modified_dim: name/key of modified dimension
        delta: numeric change applied to modified_dim
        """
        for (src, tgt), cfg in self.bonds.items():
            if src == modified_dim:
                if cfg["type"] == "linear":
                    setattr(entity, tgt, getattr(entity, tgt) + delta * cfg["ratio"])
                elif cfg["type"] == "inverse" and delta != 0:
                    setattr(entity, tgt, getattr(entity, tgt) / (delta * cfg["ratio"]))
        return entity
