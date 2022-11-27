"""
Project Portfolio 3 (Python): "Avarice"

Developed and written by Andrey Belyakov, November 2022.
Code is for a terminal of 80 characters wide and 24 rows high.
This module contains the room generation logic.
"""


class Path:
    """
    The core path for the map within the world.
    """
    def __init__(self, desc, r1_coords, r2_coords, lock=False, block=False):
        """
         Creates an instance of a new path.
         Parameter desc = description of the path.
         Parameters r1_coords & r2_coords = path between two rooms.
         Parameters lock and block: locked and blocked paths.
        """
        self.desc = desc
        self.between = [r1_coords, r2_coords]
        self.lock = lock
        self.block = block
