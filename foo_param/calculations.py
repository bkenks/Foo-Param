""" Calculate various mathematical functions """

import math
from .parameters import validate_radius


def calculate_volume(radius):

    """ Calculate the volume of a sphere """

    validate_radius(radius)
    volume = (4/3) * math.pi * radius**3
    return volume
