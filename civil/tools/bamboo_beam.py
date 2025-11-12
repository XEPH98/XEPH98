from dataclasses import dataclass
import json
import math

with open("civil/project/fmr/config.json","r") as f:
    data = json.load(f)

Fb = data["Fb_MPa"]
Fv = data["Fv_MPa"]
Fc = data["Fc_MPa"]
Eb = data["E_bending_GPa"]


# bamboo properties
print("**Mechanical Properties of Bamboo**")
print(f"source: Mechanical Properties obtained from American Bamboo Society (bamboo.org) Journal #29")
print(f"Flexural Strength, Fb = {Fb}MPa")
print(f"Shear Strength, Fv = {Fv}MPa")
print(f"Compressive Strength, Fc = {Fc}MPa")
print(f"Modulus of Elasticity, Eb = {Eb}GPa")

# bamboo geometry
print("**Structure Geometry**")
spacing = 0.20 #m
span = 3.6 #m
dia_ext = 0.10 #m
dia_int = 0.04 #m
print(f"Bamboo dia_ext = {dia_ext}m | dia_int = {dia_int}m")
print(f"Bamboo spacing = {spacing}m | span = {span}m")
Ix = (math.pi/64)*(dia_ext**4 - dia_int**4)
print(f"Bamboo moment of inertia, Ix = {Ix*100**4:.2f} cm4")

# loads, and soil properties
surcharge =  10 #kPa
soil_unit_wt = 21 #kN/m3

Pq = 0.33*surcharge/soil_unit_wt #kPa
Pa = 0.33*soil_unit_wt #kPa
print(f"**Load Definition**")
print(f"surcharge = {surcharge:.2f}kPa")
print(f"assumed soil unit weight = {soil_unit_wt:.2f}kPa")
print(f"basis for computation of equivalent lateral earth pressure: Rankine Theory")
print(f"Active Earth Pressure, Pa = {Pa:.2f}kPa")
print(f"Eq. Lateral Earth Pressure due to Surcharge, Pq = {Pq:.2f}kPa")
P_totalmax = Pq + Pa #kPa
print(f"Total Lateral Earth Pressure, P_totalmax = {P_totalmax:.2f}kPa")
# Applied Load
print("**BEAM ANALYSIS AND DESIGN**")
print("Assume simply supported beam system.")
UDL_total = P_totalmax*spacing #kN/m
print(f"Beam UDL = {UDL_total:.2f}kN/m")
Mu = UDL_total*span**2/8 #kN-m
print(f"Applied Moment, Ma = {Mu:.2f}kN-m")

# design method
print("Design Method: ASD")
fb = Mu*dia_ext*0.50*0.001 / Ix
print(f"bending stress, fb = {fb:.2f}Mpa")
print(f"Bending Strength, Fb = {Fb:.2f}Mpa")
ratio_Fb_fb = Fb/fb
print(f"strength to stress ratio = {ratio_Fb_fb:.2f}")
print(f"Required Factor of Safety = 2.0")
if ratio_Fb_fb > 2:
    print(f"ratio is greater than required FOS. SAFE!")
else:
    ValueError("UNSAFE bending stress.")
# outputs

