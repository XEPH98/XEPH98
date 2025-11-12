from dataclasses import dataclass
from typing import List

@dataclass
class BoltPosition:
    x_in: float #mm from plate reference
    y_in: float #mm from plate reference

@dataclass
class BoltLayout:
    bolts: List[BoltPosition]

@dataclass
class EndPlate:
    thickess_in: float
    width_in: float
    height_in: float
    p_ext_in: float
    gage_in: float


con1_try = EndPlate(thickess_in=3/8,
                    width_in=8,
                    height_in=24,
                    p_ext_in=5,
                    gage_in = 3)
@dataclass
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
    plate: EndPlate

def build_connection_from_input(data:dict) -> EndPlateConnection:
    
    