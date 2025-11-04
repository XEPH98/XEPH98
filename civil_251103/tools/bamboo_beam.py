from dataclasses import dataclass
import json

with open("civil_251103/project/fmr/config.json","r") as f:
    data = json.load(f)

Fb = data["Fb_MPa"]
Fv = data["Fv_MPa"]
Fc = data["Fc_MPa"]
Eb = data["E_bending_GPa"]
@dataclass
class bambooInputs:
    dia:float
    Fb:float
    Fv:float
    Fc:float
    Eb:float


b1 = bambooInputs(100,Fb,Fv,Fc,Eb)
print(b1.Fb)

# loads
surcharge = 10 #kPa
soil_unit_wt = 21 #kN/m3

eq_surcharge = 0.33*surcharge/soil_unit_wt #kPa
eq_soil = 0.33*soil_unit_wt #kPa