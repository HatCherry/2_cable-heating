"""
This function returns the temperature that specified cable should stabilize at, given its size, current flowing thorugh it, and the ambient temperature

Example:
25mm2 Cable under 200A load in 20degC ambient:

>>> steady_state(25,200,20)
125.57038340954904
"""

def steady_state(size,current,Tambient):
    from cable import cable
    from resistivity import resistivity
    from convection import convection
    from math import pi
    from numpy import infty

    # Inputs
    L = 1;                                              # length of the cylinder [m]
    A, radius, diameter, char_length = cable(size)      # cross-section area [m2]
    epsilon = 1                                         # emissivity of the surface [-]
    sigma = 5.67E-08                                    # Stefan-Boltzmann constant [W/(m2.K4)]
    
    # Initialization
    Tc = Tambient                                       # initial guess for Tc
    As = 2 * pi * radius * L                            # surface area of the cylinder [m2]
    Tol = 1e-6                                          # tolerance for the iterative solution
    dT = infty                                          # initial temperature difference
    
    # Loop
    while abs(dT) > Tol:
        Tc_old = Tc
        
        # Update the resistivity and HTC for the current Tc
        R = resistivity(Tc)
        h = convection(size, Tambient, Tc)
        
        # Calculate the heat generated and lost
        P = current**2 * R * L / A
        Q_rad = epsilon * sigma * As * (Tc + 273.15)**4
        
        # Solve the heat balance equation
        Tc = (P + Q_rad) / (h * As + 4 * epsilon * sigma * As * (Tc + 273.15)**3)
    
        # Change in temperature
        dT = Tc - Tc_old

    return Tc