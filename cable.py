"""
This function returns the cylinder's derived geometrical parameters given it's cross-section in [mm2]

Example:
Area, radius, diameter and characteristic length of 10mm2 cylinder is called by:

>>> cable(10)
9.999999999999999e-06 0.001784124116152771 0.003568248232305542 0.0028545985858444336
"""

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