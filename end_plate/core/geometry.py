from dataclasses import dataclass
from typing import List
import math

#Material Property
Ft = 90 #ksi, bolt strength, tensile
phi = 0.75
phi_b = 0.90
Fpy = 50 #ksi, plate yield strength
@dataclass
class BoltPosition:
    x_in: float #mm from plate reference
    y_in: float #mm from plate reference

@dataclass
class BoltLayout:
    bolts: List[BoltPosition]

@dataclass
class EndPlate_1_2_unstiffened():
    """
    Args:
        bf (float): inch, beam flange width
        bp (float): inch, end plate width
        tf (float): inch, beam flange thickness
        gage (float): inch, hor. dist of bolt c-c
        pf_i (float): inch, inside flange to center of bolt
        pf_o (float): inch, outside of flange to center of bolt
        p_b (float): inch, c-c bolt distance
        p_ext (float): inch, outside of flange to edge of end plate
        bolt_dia (float): inch, bolt diameter
        h (float): inch, beam height
        Mu (float): kip-in, ultimate moment
    """
    bf: float
    bp: float
    tf: float
    gage: float
    pf_i: float
    pf_o: float
    p_b: float
    p_ext: float
    bolt_dia: float
    h: float
    Mu: float
    Yr: float = 1 # for extended connections


    @property
    def d_0(self):
        return round(self.h - self.tf*0.50 + self.pf_o,2)
    @property
    def d_1(self):
        return round(self.h - self.tf*0.50 - self.pf_i,2)
    @property
    def d_2(self):
        return round(self.d_1 - self.p_b,2)
    @property
    def sum_dn(self):
        return round(self.d_0 + self.d_1 + self.d_2,2)
    @property
    def h_0(self):
        return round(self.h + self.pf_o,2)
    @property
    def h_1(self):
        return round(self.h - self.tf - self.pf_i,2)
    @property
    def h_2(self):
        return round(self.h_1 - self.p_b,2)

    def required_bolt_dia(self):
        return round(math.sqrt(2*self.Mu / (math.pi*phi*Ft*self.sum_dn)),2)
    
    def required_end_plate_thickness(self):
        bp = self.bp
        h1 = self.h_1
        h2 = self.h_2
        h0 = self.h_0
        pf_o = self.pf_o
        pf_i = self.pf_i
        p_b = self.p_b
        gage = self.gage
        s_check = round(0.50*math.sqrt(self.bp*self.gage),2)
        if self.pf_i <= s_check:
            s = self.pf_i
        else:
            s = s_check
        Y = round(bp*0.50*( (h1/pf_i) + (h2/s) + (h0/pf_o)-0.50) + (2/gage)*(h1*(pf_i+0.75*p_b)+h2*(s+0.25*p_b))+gage*0.50,2)
        Pt = round(math.pi*(self.bolt_dia**2)*Ft/4 , 2)
        LRFD_Mnp = phi*2*Pt*self.sum_dn
        tp_req = round(math.sqrt(1.11*self.Yr*LRFD_Mnp/(phi_b*Fpy*Y)),2)
        return tp_req
            

con1_try = EndPlate_1_2_unstiffened(
    bf=8,
    bp=8,
    tf=3/8,
    gage=3,
    pf_i=1.75,
    pf_o=2.5,
    p_b=2.5,
    p_ext=5,
    bolt_dia=5/8,
    h=24,
    Mu=2400)

aaa = con1_try.required_bolt_dia()
aaa = con1_try.required_end_plate_thickness()

print(aaa)

class Member:
    section:str
    depth:float
    tf:float
    tw:float

@dataclass
class EndPlateConnection:
    bolt_dia: float
    type: str # flush or extended
    column: str
    beam: str