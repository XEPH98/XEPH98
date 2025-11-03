from dataclasses import dataclass
import json

with open("civil_251103/project/200/beam_G1.json","r") as f:
    data = json.load(f)

@dataclass
class BeamInput:
    beam_ht_mm:float,
    beam_bw_mm:float


