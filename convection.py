def convection(size, Tambient, Tcable):
    """
    Calculate the Heat Transfer Coefficient (HTC) of a specified cylinder at a given temperature 
    in a defined ambient environment.
    
    The function uses the following dimensionless numbers for calculations:
    - Prandtl
    - Grashof
    - Rayleigh
    - Nusselt

    Parameters:
    - size (float): The size of the cylinder in mm^2.
    - Tambient (float): The ambient temperature in degrees Celsius.
    - Tcable (float): The cable temperature in degrees Celsius.
    
    Returns:
    - float: The Heat Transfer Coefficient (HTC) at the given cable temperature in W/(m^2*K).
    
    Example:
    >>> convection(10, 20, 135)
    18.077843796422492

    Note:
    This function imports and uses the 'cable' function to get the cylinder's data.
    """
    import numpy as np
    from cable import cable
    
    # Gravitational acceleration
    g = 9.81

    # Get cylinder's data
    A, radius, diameter, char_length = cable(size)

    # Loop
    Temp = Tambient
    
    # Initialize empty arrays to store the table data
    Temperatures = np.empty(0, dtype=int)
    HTCs = np.empty(0, dtype=float)

    for i in range(21):

        # Air properties temperature-dependent functions
        rho = -6.9255137E-14*Temp**5 + 9.9497850E-11*Temp**4 - 5.7287703E-08*Temp**3 + 1.8734971E-05*Temp**2 - 4.8130164E-03*Temp + 1.2755735E+00
        cp = 1.0034184E-12*Temp**5 - 1.0738981E-09*Temp**4 -5.5326330E-08*Temp**3 + 4.9988769E-04*Temp**2 + 8.6774345E-03*Temp + 1.0064011E+03
        beta = -2.0935040E-16*Temp**5 + 2.9938499E-13*Temp**4 - 1.7111868E-10*Temp**3 + 5.5289942E-08*Temp**2 - 1.3991837E-05*Temp + 3.6745863E-03
        k = -3.0554483E-17*Temp**5 - 1.7674494E-15*Temp**4 + 4.9442424E-11*Temp**3 - 4.7410302E-08*Temp**2 + 7.6380159E-05*Temp + 2.4171139E-02
        mu = -2.0092968E-21*Temp** - 2.3935264E-17*Temp**4 + 4.3773859E-14*Temp**3 - 3.9016500E-11*Temp**2 + 5.0415245E-08*Temp + 1.7238931E-05
        Pr = 5.6148575E-16*Temp**5 - 1.5939497E-13*Temp**4 - 7.1499978E-10*Temp**3 + 6.6940014E-07*Temp**2 - 1.6804362E-04*Temp + 7.1791609E-01

        # Dimensionless Numbers
        Prandtl = Pr
        Grashof = (g*beta*(Temp-Tambient)*char_length**3)/((mu/rho)**2)
        Rayleigh = Prandtl*Grashof
        Nusselt = (0.6+(0.387*(Rayleigh**(1/6)))/((1+(0.559/Prandtl)**(9/16))**(8/27)))**2
        HTC = (Nusselt*k)/char_length

        # Prepare vectors that are going to be table's columns
        Temperatures = np.append(Temperatures, Temp)
        HTCs = np.append(HTCs, HTC)

        # Increment
        Temp = Temp + 10
    
    # Build a table out of the vectors from the loop
    HTC_Table = np.column_stack((Temperatures,HTCs))
    
    # From the table, interpolate the HTC at any given cable temperature
    h = np.interp(Tcable, Temperatures, HTCs)

    return h