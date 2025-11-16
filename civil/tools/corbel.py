from dataclasses import dataclass
from typing import List

@dataclass
class anchor_bolt:
    """Origin always at bottom left of plate.
    Args:
        x (float): inch, horizontal distance
        y (float): inch, vertical distance
    """
    x: float
    y: float

@dataclass
class group_anchor:
    anchors: List[anchor_bolt]

a1 = anchor_bolt(2,2)
a2 = anchor_bolt(4,2)
a3 = anchor_bolt(2,4)
a4 = anchor_bolt(4,4)

class anchor:
    def __init__(self, dia, futa, n_anchor, cc_dist, edge_dist, hef):
        """_summary_

        Args:
            dia (float): _description_
            futa (float): _description_
            n_anchor (int): _description_
            cc_dist (float): _description_
            edge_dist (float): _description_
            hef (float): _description_
        """
        self.dia = dia
        self.futa = futa
        self.n_anchor = n_anchor
        self.cc_dist = cc_dist
        self.edge_dist = edge_dist
        self.hef = hef

    @property
    def proj_area_single_anchor(self) -> float:
        """Calculation of A_nco per ACI 318M 19, Figure R17.6.2.1"""
        return round(2*1.5*self.hef*2*1.5*self.hef,2)
    def proj_area_group_anchor(self) -> float:
        pass
    def strength_breakout(self):
        if self.n_anchor == 1:
            nominal_cb = 1