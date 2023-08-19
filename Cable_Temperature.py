"""
This script is supposed to ask user for input values after providing all the information about restrictions, 
and output the analytical solution for steady-state temperature of the specified cable under given electrical load
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