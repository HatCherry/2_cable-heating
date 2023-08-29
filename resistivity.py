def resistivity(temperature):
    """
    Calculate the electrical resistivity of copper at a given temperature.
    
    This function uses the formula:
    R(T) = R_20 * (1 + alpha * (T - 20))
    where R(T) is the resistivity at temperature T,
    R_20 is the resistivity at 20°C, and
    alpha is the temperature coefficient of resistance.
    
    Parameters:
    - temperature (float): The temperature in degrees Celsius.
    
    Returns:
    - float: The electrical resistivity of copper at the given temperature in Ohm-meters.
    
    Example:
    >>> resistivity(135)
    2.4835079999999996e-08
    """
    
    R_20 = 1.72e-8  # Copper electrical resistivity at reference 20°C
    alfa = 0.00386  # Temperature coefficient of resistance (TCR) [1/°C]
    
    R = R_20 * (1 + alfa * (temperature - 20))  # Resistivity at the given temperature [Ohm*m]
    return R
