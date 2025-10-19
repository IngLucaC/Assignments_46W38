import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# PART 1
# load data from three excel sheets
df_baseline = pd.read_excel("Wind-Data.xlsx", sheet_name="Exercise 4 - Baseline")
df_A = pd.read_excel("Wind-Data.xlsx", sheet_name="Exercise 4 - A")
df_B = pd.read_excel("Wind-Data.xlsx", sheet_name="Exercise 4 - B")
Time = df_baseline["Time (s)"]
Speed_baseline = df_baseline["Rotor speed (rpm)"]
Speed_A = df_A["Rotor speed (rpm)"]
Speed_B = df_B["Rotor speed (rpm)"]
Thrust_baseline = df_baseline["Thrust (kN)"]
Thrust_A = df_A["Thrust (kN)"]
Thrust_B = df_B["Thrust (kN)"]
Tower_moment_baseline = df_baseline["Tower base moment (kNm)"]
Tower_moment_A = df_A["Tower base moment (kNm)"]
Tower_moment_B = df_B["Tower base moment (kNm)"]


# plot the three rotor speed time series
# fig, ax = plt.subplots()
fig = plt.figure(1)
ax = fig.add_subplot()
ax.plot(Time, Speed_baseline, color="black")
ax.plot(Time, Speed_A, color="orange")
ax.plot(Time, Speed_B, color="blue")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Rotor speed [rpm]")
ax.legend(["Baseline", "Control A", "Control B"])
ax.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("Figure_4.jpeg", dpi=200)

# PART 2
# compute the standard deviation of each time series
std_speed_baseline = Speed_baseline.std()
std_speed_A = Speed_A.std()
std_speed_B = Speed_B.std()
std_thrust_baseline = Thrust_baseline.std()
std_thrust_A = Thrust_A.std()
std_thrust_B = Thrust_B.std()
std_tower_moment_baseline = Tower_moment_baseline.std()
std_tower_moment_A = Tower_moment_A.std()
std_tower_moment_B = Tower_moment_B.std()

# normalization
norm_std_baseline = 1.0
norm_std_speed_A = std_speed_A / std_speed_baseline
norm_std_speed_B = std_speed_B / std_speed_baseline
norm_std_thrust_A = std_thrust_A / std_thrust_baseline
norm_std_thrust_B = std_thrust_B / std_thrust_baseline
norm_std_tower_moment_A = std_tower_moment_A / std_tower_moment_baseline
norm_std_tower_moment_B = std_tower_moment_B / std_tower_moment_baseline

# CasePlot: normalized bar chart
nBaseline = [1, 1, 1]
nA = [norm_std_speed_A, norm_std_thrust_A, norm_std_tower_moment_A]
nB = [norm_std_speed_B, norm_std_thrust_B, norm_std_tower_moment_B]

fig = plt.figure(2)
# fig, ax = plt.subplots()
ax = fig.add_subplot()
categories = ["Baseline", "Control A", "Control B"]
x = np.arange(len(categories))
width = 0.25  # width of the bars
rects1 = ax.bar(x - width, nBaseline, width, label="Rotor Speed")
rects2 = ax.bar(x, nA, width, label="Thrust")
rects3 = ax.bar(x + width, nB, width, label="Tower Base Moment")
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
ax.set_title("Norm. Std Dev. for Different Output Metrics")
fig.tight_layout()
ax.set_xticks(x)
ax.set_xticklabels(categories)
plt.show()
plt.savefig("Figure_5.jpeg", dpi=200)
