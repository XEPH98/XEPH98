from dataclasses import dataclass
from typing import List
from math import sqrt
from math import pi
#validation
def safe_pass(minv,val,maxv,name_attr):
    """Safe pass

    Args:
        minv (float): _description_
        val (float): _description_
        maxv (float): _description_
        name_attr(str): attribute name to be evaluated

    Raises:
        ValueError: _description_
    """
    if val > minv and val < maxv:
        print(f"{name_attr} value OK. {minv} < {val} < {maxv}")
    else:
        raise ValueError(f"val = {val} outside valid range ({minv}, {maxv})")

#material properties
fc = 21 #MPa
futa = 400 #MPa
fya = 250 #MPa

class Anchor:
    """_summary_

        Args:
            type_anchor (int): [1] cast-in headed stud anchor [2] post-installed anchors
            dia (float): _description_
            n_anchor (int): pcs
            cc_dist (float): mm
            edge_dist (float): mm
            hef (float): mm
            kc (int): input [10] for cast-in anchors [7] for post-installed anchors (ACI318M-14, Section 17.4.2.2)
    """
    def __init__(self, type_anchor, dia, n_anchor, cc_dist, edge_dist, hef, kc):
        self.type_anchor = type_anchor
        self.dia = dia
        self.n_anchor = n_anchor
        self.cc_dist = cc_dist
        self.edge_dist = edge_dist
        self.hef = hef
        self.kc = kc
    @property
    def proj_area_single_anchor(self) -> float:
        """Calculation of A_nco per ACI 318M 19, Figure R17.6.2.1"""
        return round(2*1.5*self.hef*2*1.5*self.hef,2)
    def proj_area_group_anchor(self) -> float:
        s1 = self.cc_dist
        ca1 = self.edge_dist
        hef = self.hef
        dict = {
            1:'a',
            2:'b',
            4:'c'
        }
        case = dict[self.n_anchor]
        if case == 'a':
            Anc = (ca1 + 1.5*hef)**2
        elif case == 'b': #provided that ca1 < 1.5hef and s1 < 3hef
            Anc = (ca1 + s1 + 1.5*hef)*(2*1.5*hef)
        elif case == 'c':
            Anc = (ca1+s1+1.5*hef)*(ca1+s1+1.5*hef)
        return Anc
    def strength_breakout_single_tension(self) -> float:
        lamda = 1.00 #ACI318M-14, Section 19.2.4.2
        lamda_a = 0.60*lamda #See ACI318M-14, Section 7.2.6
        if (self.hef < 280 or self.hef > 635):
            Nb = self.kc*lamda_a*sqrt(fc)*self.hef**1.5 #N, ACI318M-14, Section 17.4.2.2a
            return round(Nb,2)
        elif self.hef >= 280 and self.hef <= 635:
            Nb = 3.9 * lamda_a * sqrt(fc)*(self.hef)**(5/3) #N, ACI318M-14, Section 17.4.2.2b
            return round(Nb,2)
        else:
            raise ValueError("No match case")
    def strength_cb_in_tension(self) -> float:
        """Concrete breakout strength of anchors in tension, ACI318M-14, Section 17.4.2"""
        Anco = self.proj_area_single_anchor
        Anc = self.proj_area_group_anchor()
        psi_edN = 1
        psi_cN = 1
        psi_cpN = 1
        psi_ecN = 1
        Nb = self.strength_breakout_single_tension()
        if self.n_anchor == 1:
            Ncb = (Anc/Anco)*psi_edN*psi_cN*psi_cpN*Nb
        else:
            Ncb = (Anc/Anco)*psi_ecN*psi_edN*psi_cN*psi_cpN*Nb
        return round(Ncb,2)
    
    def pull_out_strength(self):
        Abrg = 1
        Np = 8*Abrg*fc
        psi_cP =1 #ACI318M-14, SEction 17.4.3.6
        Npn = psi_cP*Np
        return "ongoing"
    
    def strength_shear_single(self):
        Ase_v = pi * (self.dia**2) * 0.25#effective cs area of an anchor in shear, mm2
        if self.type_anchor == 2:
            Vsa = 0.60* Ase_v * futa #N, ACI318M-14, Section 17.5.1.2(c)
        return round(Vsa,2)
    
    def strength_cb_in_shear(self):
        ca1 = self.edge_dist
        Avco = 4.5*(ca1)**2 #ACI318M-14, Section 17.5.2.1c
        Avc = 1
        #can be conservatively assumed as using 1 bolt for now,


    def validation(self) -> str:
        return safe_pass(0, futa, min(1.90*fya,860), "F_uta")

    def output(self):
        print("*** VALIDATION OF ATTRIBUTES ***")
        self.validation()
        print("*** DESIGN CHECKS ***")
        print(f"Breakout Strength of Single Anchor in tension, Ncb = {self.strength_breakout_single_tension()}-N")
        print(f"Breakout Strength of Anchor Group in tension, Ncb = {self.strength_cb_in_tension()}-N")
        print(f"Nominal strength of anchor in shear, Vsa = {self.strength_shear_single()}-N")
connn1 = Anchor(type_anchor = 2,
                dia=20,
                n_anchor=1,
                cc_dist=200,
                edge_dist=100,
                hef=100,
                kc=7)

connn1.output()
print(pi)