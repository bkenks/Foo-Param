""" Validate parameters """

def validate_radius(radius):

    """ Validate the radius of a sphere """

    if not isinstance(radius, (float, int)) or radius <= 0:
        raise ValueError("The radius must be a positive number")
