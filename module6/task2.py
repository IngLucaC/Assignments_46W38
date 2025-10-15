import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Wind-Data.xlsx")

# Display the first few rows of the data frame
# print(df.head())

WindSpeed = df["Wind speed (m/s)"]
Power = df["Power (kW)"]
Thrust = df["Thrust (kN)"]
Speed = df["Rotor speed (rpm)"]
Pitch = df["Blade pitch (degrees)"]

# plot Power and Thrust vs Wind Speed
fig, (ax1, ax3) = plt.subplots(2, 1)
ax1.set_xlabel("Wind Speed (m/s)")
ax1.set_ylabel("Power (kW)")
(line1,) = ax1.plot(WindSpeed, Power, color="red", label="Power (kW)")
ax2 = ax1.twinx()
ax2.set_ylabel("Thrust (kN)")
(line2,) = ax2.plot(WindSpeed, Thrust, color="green", label="Thrust (kN)")
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="lower right")

# plot Speed and Pitch vs Wind Speed
ax3.set_xlabel("Wind Speed (m/s)")
ax3.set_ylabel("Rotor Speed (rpm)")
(line3,) = ax3.plot(WindSpeed, Speed, color="blue", label="Rotor Speed (rpm)")
ax4 = ax3.twinx()
ax4.set_ylabel("Blade Pitch (degrees)")
(line4,) = ax4.plot(WindSpeed, Pitch, color="gray", label="Blade Pitch (degrees)")
lines2 = [line3, line4]
labels2 = [line.get_label() for line in lines2]
ax3.legend(lines2, labels2, loc="lower right")
plt.tight_layout()
plt.show()
plt.savefig("Figure_2.jpeg", dpi=300)
