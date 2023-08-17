"""
This function returns the value of Copper electrical resistivity at any given temperature

Example:
Resistivity of copper that is heated up to 135degC is called by:

>>> resistivity(135)
2.4835079999999996e-08
"""

def resistivity(temperature):
    R_20 = 1.72e-8      #Copper el. resistivity at ref. 20[degC]
    alfa = 0.00386      #Temperature coefficient of resistance (TCR) [1/degC]
    R = R_20*(1+alfa*(temperature-20))      #Resistivity at any given temperature [Ohm*m] 
    return R