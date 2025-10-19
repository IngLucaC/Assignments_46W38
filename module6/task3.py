import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Wind-Data.xlsx", sheet_name="Exercise 3", index_col=0)

TSR = df.index.values.astype(float)
Pitch = df.columns.values.astype(float)

# Crea griglia per il surface plot
Beta, Lambda = np.meshgrid(Pitch, TSR)  # NB: ordine (X, Y)

# Matrice dei valori di Cp
Cp = df.values.astype(float)

# Plot 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(Beta, Lambda, Cp, cmap="cividis")

# Etichette
ax.set_xlabel("β [°]")
ax.set_ylabel("λ [-]")
ax.set_zlabel("$C_p$ [-]")

plt.tight_layout()
plt.show()
plt.savefig("Figure_3.jpeg", dpi=300)
