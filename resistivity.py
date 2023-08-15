# This function returns the value of Copper electrical resistivity at any given temperature

def resistivity(temperature):
    R_20 = 1.72e-8      #Copper el. resistivity at ref. 20[degC]
    alfa = 0.00386      #Temperature coefficient of resistance (TCR) [1/degC]
    R = R_20*(1+alfa*(temperature-20))      #Resistivity at any given temperature [Ohm*m] 
    return R