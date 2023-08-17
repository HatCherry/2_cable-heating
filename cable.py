"""This function returns the cylinder's derived geometrical parameters given it's cross-section in [mm2]"""

def cable(size):
    from math import sqrt, pi

    # Unit conversion to [m2]
    A = size*1E-06
    # Derived cable data
    radius = sqrt(A/pi)
    diameter = radius*2
    char_length_theory = diameter
    char_length_coeff = 0.8
    char_length = char_length_theory*char_length_coeff

    return A, radius, diameter, char_length