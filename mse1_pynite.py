import numpy as np
"""
About PyNiteFEA Package:
    is an open-source Finite Element Analysis (FEA) library written in python.
    it lets you analyze:
        Beams, Frames, Trusses, Plates, 3D structural elements

"""

#Example
from Pynite import FEModel3D

# 1. Create a new finite elmeent element model
model = FEModel3D()

# 2. Add nodes (supports and midspan)
model.add_node("A",0,0,0)
model.add_node("B",6,0,0)

# 3. Define a material and section properties
E = 29000 #ksi
G = 11200 #ksi
Iy = 100 #in4
Iz = 100 #in4
J = 10 #in4
A = 10 #in2

# 4. Add a member
model.add_member("Beam1","A","B",E,G,Iy,Iz,J,A)

# 5. Add supports
model.def_support("A",True,True,True,True,False,False)
model.def_support("B",True,True,True,False,False,False)

# 6. Add a uniform distributed load on the beam (Fy dir)
model.add_member_dist_load("Beam1","Fy",-2,-2)

# 7. Analyze the structure
model.analyze()

# 8. Print results
beam = model.members("Beam1")

print("Max deflection:",beam)
for node in model.nodes.values():
    print(f"{node.Name}: Rx = {node.RxnFX:.2f}, Ry = {node.RxnFY:.2f}, Rz = {node.RxnFZ:.2f}")