from dataclasses import dataclass
from typing import List

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
        self.dia:float = dia
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
        if 
    def strength_breakout(self):
        if self.n_anchor = 1:
            nominal_cb = 