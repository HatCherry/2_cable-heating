# Given the parameters from MATLAB, let's define the function, plot it, output the equation, and compare predicted vs actual values.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Current_flat = [10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20]
Insulation_flat = [0.5,1.0,1.5,2.0, 0.5,1.0,1.5,2.0, 0.5,1.0,1.5,2.0]
Actual_Heat_Flux = [-150,-275,-350,-425, -500,-750,-950,-1100, -1300,-1825,-2150,-2400]

# MATLAB parameters for the polynomial p00 + p10*x + p01*y + p20*x^2 + p11*x*y + p02*y^2
p00 = -1261 
p10 = 248 
p01 = 32 
p20 = -11.42
p11 = -53.98 
p02 = 138.2 

# Define the polynomial function using the given parameters
def polynomial_from_matlab(x, y):
    return p00 + p10*x + p01*y + p20*x**2 + p11*x*y + p02*y**2

# Now we plot the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid over which we'll calculate the polynomial values
x_range = np.linspace(min(Current_flat), max(Current_flat), 100)
y_range = np.linspace(min(Insulation_flat), max(Insulation_flat), 100)
X, Y = np.meshgrid(x_range, y_range)
Z = polynomial_from_matlab(X, Y)

# Output the function formula
function_formula = f"Heat Flux = {p00} + {p10}*Current + {p01}*Insulation + {p20}*Current^2 + {p11}*Current*Insulation + {p02}*Insulation^2"

# Predict the heat flux using the polynomial and compare with actual values
predicted_heat_flux = polynomial_from_matlab(np.array(Current_flat), np.array(Insulation_flat))

# Create a dataframe for comparison
comparison_df = pd.DataFrame({
    'Current': Current_flat,
    'Insulation': Insulation_flat,
    'Actual Heat Flux': Actual_Heat_Flux,
    'Predicted Heat Flux': predicted_heat_flux
})

print(function_formula, comparison_df)

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Scatter plot of actual data points for comparison
ax.scatter(Current_flat, Insulation_flat, Actual_Heat_Flux, color='r', label='Actual Data')

# Labels and title
ax.set_xlabel('Current')
ax.set_ylabel('Insulation')
ax.set_zlabel('Heat Flux')
ax.set_title('Polynomial Fit of Heat Flux')

# Legend
ax.legend()

# Show the plot
plt.show()