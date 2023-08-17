"""This function returns the HTC value of specified cylinder's at any given temperature, in defined ambient"""

def convection(size, Tcable, Tambient):
    from cable import cable

    # Get cylinder's data
    A, radius, diameter, char_length = cable(size)

    
    return