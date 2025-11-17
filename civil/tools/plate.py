from dataclasses import dataclass
from typing import List

@dataclass
class AnchorBolt:
    """Origin always at bottom left of plate.
    Args:
        x (float): inch, horizontal distance
        y (float): inch, vertical distance
    """
    x: float
    y: float

@dataclass
class GroupAnchor:
    """Represents a group of anchor bolts on the plate
    """
    anchors: List[AnchorBolt]

@dataclass
class Plate:
    """
    Represents a plate iwth a gorup of anchors
    Args:
        group (List): group of anchor bolts
        thk (float): in, plate thickness
        dimx (float): in
        dimy (float): in
        edge_dist (float): in
        cc_dist (float): in
    """
    group: GroupAnchor
    thk: float
    dimx: float
    dimy: float
    edge_dist: float
    cc_dist: float
    def show_bolt_positions(self):
        """Displays bolt coordinates and a simple 2D plot."""
        print("Bolt Positions (inches): ")
        for i, bolt in enumerate(self.group.anchors,1):
            print(f"Bolt {i}: (x={bolt.x}, y={bolt.y})")

if __name__ == "__main__":
    # Define four anchor bolts
    a1 = AnchorBolt(2,2)
    a2 = AnchorBolt(4,2)
    a3 = AnchorBolt(2,4)
    a4 = AnchorBolt(4,4)

    # Group of anchors
    group = GroupAnchor([a1,a2,a3,a4])

    # Plate definition
    plate = Plate(group=group, thk=0.02, dimx=6, dimy=6)

    # Show bolt positions and plot layout
    plate.show_bolt_positions()