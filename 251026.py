from dataclasses import dataclass

@dataclass
class Cup:
    height_mm:float
    dia_mm:float = 40

pandemanila = Cup(height_mm=20)
print(pandemanila)