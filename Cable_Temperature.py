"""
This script calculates the steady-state temperature of a specified copper cylindrical cable under a given electrical load.

The script provides information about valid cable sizes and their maximum current capacity.
It then asks the user to input the cable size, electric current, and ambient temperature. 
If the entered values are within acceptable limits, the script outputs the steady-state temperature 
at which the cable should stabilize.

The script relies on the `steady_state` function to perform the temperature calculation.

Example:
Run the script and follow the prompts to input the cable size, electric current, and ambient temperature.

Constraints:
1. Cable size should be within the valid sizes mentioned in the displayed table.
2. Current should not exceed the maximum capacity of the selected cable size.

Note:
The script uses the Pandas library to display the table of valid cable sizes and their maximum current capacities.
"""
import pandas as pd
from steady_state import steady_state

#Script Handle
print("""
      The script is calculating the steady-state temperature of the cylindrical copper wire [mm2] 
under the given electric current [A] flowing through it, in the chosen ambient temperature [degC]
      """)
# Size and Load Restrictions Table
valid_size = [0.5, 0.75, 1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120]
max_current = [25, 30, 35, 45, 65, 85, 110, 155, 210, 280, 355, 450, 570, 705, 830]
boundaries = {'Valid size [mm2]':valid_size,'Maximum current [A]':max_current}
boundaries_table = pd.DataFrame(boundaries)
boundaries_table_transposed = boundaries_table.transpose()
print(boundaries_table_transposed.to_string(header=False))

# User Inputs
Cable = float(input("Cable size [mm2]: "))
# Check if valid
if Cable not in valid_size:
  print("\n - ERROR: Wrong cable size - \n\n")

else:
    prompt_I = float(input("Current [A]: "))
    I = abs(prompt_I)
    # Look up the maximum current for the given cable size
    max_current_allowed = boundaries_table[boundaries_table['Valid size [mm2]'] == Cable]['Maximum current [A]'].values

    # Check if current exceeds the allowed range
    if len(max_current_allowed) > 0 and I > max_current_allowed[0]:
        print("\n - ERROR: Cable is significantly overloaded - \n\n")

Ta = float(input("Ambient temperature [degC]: "))
Tc = round(steady_state(Cable,I,Ta),2)
print("\nCable should stabilize at: ", Tc, "  [degC] \n\n")