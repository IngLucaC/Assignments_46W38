import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import weibull_min
from scipy.optimize import Bounds
from scipy.optimize import minimize, LinearConstraint, NonlinearConstraint

# load data from "Exercise 3" sheet
dataSeries = pd.read_excel("Module 7 - Exercises data.xlsx", sheet_name="Exercise 3")
date_time = dataSeries["Date/Time"]
speed = dataSeries["Wind Speed (m/s)"]

# fit a Weibull distribution to the wind speed data
speed_ref = np.linspace(0, max(speed), 50)
shape, loc, scale = weibull_min.fit(speed, floc=0)
pdf = weibull_min.pdf(speed_ref, shape, loc, scale)

# data
rho = 1.225
Cp = 0.45
Vin = 3
Vout = 25
hours_year = 8760
P_rated_max = 10e6
hub_height = 100
R_max = 0.8 * hub_height

# rated power calculation
# contraint 1: rated power max = 10 MW
# contraint 2: rotor radius max = 80 m

speed_ref = np.linspace(0, max(speed), 50)
shape, loc, scale = weibull_min.fit(speed, floc=0)
pdf = weibull_min.pdf(speed_ref, shape, loc, scale)

# Data
rho = 1.225
Cp = 0.45
Vin = 3
Vout = 25
hours_year = 8760
P_rated_max = 10e6
hub_height = 100
R_max = 0.8 * hub_height  # 80% hub height


# Bounds
bounds = Bounds([70, Vin + 0.1], [400, Vout - 0.1])
x0 = np.array([150, 9])  # initial guess [D, Vr]

# Linear constraint: 0.5 * D <= R_max
linear_con = LinearConstraint([[0.5, 0]], -np.inf, [R_max])


# Nonlinear constraint: P_rated <= P_rated_max
def P_rated(x):
    D, Vr = x
    return 0.5 * rho * np.pi * (D / 2) ** 2 * Cp * Vr**3


def nonlin_func(x):
    return P_rated(x) - P_rated_max


nonlinear_con = NonlinearConstraint(nonlin_func, -np.inf, 0.0)


# Power curve
def power_curve(speed_ref, Vrated, Vin, Vout, Prated):
    P = np.zeros_like(speed_ref)
    # sub-rated region
    mask_sub = (speed_ref >= Vin) & (speed_ref < Vrated)
    P[mask_sub] = Prated * ((speed_ref[mask_sub] - Vin) / (Vrated - Vin)) ** 3
    # rated region
    mask_rated = (speed_ref >= Vrated) & (speed_ref <= Vout)
    P[mask_rated] = Prated
    return P


# AEP
def AEP(x):
    D, Vrated = x
    Pr = min(P_rated([D, Vrated]), P_rated_max)
    P = power_curve(speed_ref, Vrated, Vin, Vout, Pr)
    return hours_year * np.trapz(P * pdf, speed_ref)


# Cost function (negativo per minimizzazione)
def cost(x):
    return -AEP(x)


# Optimization
res = minimize(
    cost,
    x0,
    method="trust-constr",
    constraints=[linear_con, nonlinear_con],
    bounds=bounds,
    options={"verbose": 1},
)

D_opt, Vr_opt = res.x
P_opt = P_rated([D_opt, Vr_opt])
AEP_opt = AEP([D_opt, Vr_opt])

# Outputs
print(f"Optimal rotor diameter D = {D_opt:.2f} m")
print(f"Optimal rated wind speed Vr = {Vr_opt:.2f} m/s")
print(f"Rated Power = {P_opt/1e6:.2f} MW")
print(f"AEP ≈ {AEP_opt/1e6:.2f} MWh/year")

# Plot power curve
Pr_opt = min(P_opt, P_rated_max)
P_curve = power_curve(speed_ref, Vr_opt, Vin, Vout, Pr_opt)
plt.plot(speed_ref, P_curve / 1e6, "b-", linewidth=2)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("Power (MW)")
plt.title("Optimized Power Curve")
plt.grid(True)
plt.savefig("Figure_10.jpeg", dpi=200)
plt.show()
