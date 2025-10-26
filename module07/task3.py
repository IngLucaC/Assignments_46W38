import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import weibull_min

# load data from "Exercise 3" sheet
dataSeries = pd.read_excel("Module 7 - Exercises data.xlsx", sheet_name="Exercise 3")
date_time = dataSeries["Date/Time"]
speed = dataSeries["Wind Speed (m/s)"]

# Part 1) histogram of the wind speed
fig, ax = plt.subplots()
ax.hist(speed, bins=50, color="orange", edgecolor="black")
ax.set_xlabel("Wind Speed [m/s]")
ax.set_ylabel("Frequency")
ax.set_title("Wind Speed Distribution")
ax.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
plt.savefig("Figure_8.jpeg", dpi=200)
plt.close("all")

# Parts 2+3) fit a Weibull distribution to the wind speed data
speed_ref = np.linspace(0, max(speed), 100)
shape, loc, scale = weibull_min.fit(speed, floc=0)
pdf = weibull_min.pdf(speed_ref, shape, loc, scale)

fig, ax = plt.subplots()
ax.plot(speed_ref, pdf, color="red", linewidth=2)
ax.hist(speed, bins=50, color="orange", edgecolor="black", density=True)
ax.set_xlabel("Wind Speed [m/s]")
ax.set_ylabel("Frequency")
ax.set_title("Wind Speed Distribution")
ax.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
plt.savefig("Figure_9.jpeg", dpi=200)
plt.close("all")
