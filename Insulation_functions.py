import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

# Given parameters
Current_flat = [500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700]
Insulation_flat = [0, 0.5, 1.0, 1.5, 2.0, 0, 0.5, 1.0, 1.5, 2.0, 0, 0.5, 1.0, 1.5, 2.0]
Actual_Heat_Flux = [0, -5, 0, 10, 20, 0, 10, 25, 45, 70, 0, 40, 80, 130, 180]

# Coefficients for the polynomial
p00 = -4.052
p10 = 0.007541
p01 = 323.8
p20 = -1.027e-6
p11 = -1.452
p02 = 20.55
p21 = 0.001551
p12 = -0.007161
p03 = -2.241

# Define the polynomial function using the given parameters
def polynomial_from_matlab(x, y):
    return p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p21 * y * x ** 2 + p12 * x * y ** 2 + p03 * y ** 3

# Output the function formula
function_formula = f"Heat Flux = {p00} + {p10}*Current + {p01}*Insulation + {p20}*Current^2 + {p11}*Current*Insulation + {p02}*Insulation^2 + {p21}*Insulation*Current^2 + {p12}*Current*Insulation^2 + {p03}*Insulation^3"
print(function_formula)

# Now we plot the function and the difference between actual and predicted heat flux
fig = plt.figure(figsize=(12, 5))

# Subplot for the polynomial surface
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Create a grid over which we'll calculate the polynomial values
x_range = np.linspace(min(Current_flat), max(Current_flat), 100)
y_range = np.linspace(min(Insulation_flat), max(Insulation_flat), 100)
X, Y = np.meshgrid(x_range, y_range)
Z = polynomial_from_matlab(X, Y)

# Plot the surface
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Scatter plot of actual data points for comparison
ax1.scatter(Current_flat, Insulation_flat, Actual_Heat_Flux, color='r', label='Actual Data')

# Labels and title
ax1.set_xlabel('Current')
ax1.set_ylabel('Insulation')
ax1.set_zlabel('Heat Flux')
ax1.set_title('Polynomial Fit of Heat Flux')
ax1.legend()

# Subplot for the difference between actual and predicted heat flux
ax2 = fig.add_subplot(1, 2, 2)

# Calculate the difference between actual and predicted heat flux
predicted_heat_flux = polynomial_from_matlab(np.array(Current_flat), np.array(Insulation_flat))
difference = predicted_heat_flux - np.array(Actual_Heat_Flux)

# Set colors based on the sign of the difference
colors = ['r' if diff > 0 else 'b' for diff in difference]

# Plot the difference as a bar plot
ax2.bar(range(len(Current_flat)), difference, color=colors)
ax2.axhline(0, color='k', linestyle='--')
ax2.grid(True)
ax2.set_xlabel('Data Point')
ax2.set_ylabel('Difference (Predicted - Actual)')
ax2.set_title('Difference between Predicted and Actual Heat Flux')

# Create a dataframe for comparison
comparison_df = pd.DataFrame({
    'Current': Current_flat,
    'Insulation': Insulation_flat,
    'Actual Heat Flux': Actual_Heat_Flux,
    'Predicted Heat Flux': predicted_heat_flux
})

print(comparison_df)

# Show the plots
plt.tight_layout()
plt.show()