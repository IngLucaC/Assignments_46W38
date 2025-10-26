import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
from scipy import fftpack
from scipy.signal import iirnotch, filtfilt
from scipy.optimize import curve_fit

# load data from "Exercise 2" sheet
dataSeries = pd.read_excel("Module 7 - Exercises data.xlsx", sheet_name="Exercise 2")
speed = dataSeries["Wind speed (m/s)"]
pitch = dataSeries["Blade pitch (degrees)"]

# create an interpolation function
pitch_interpolated = interp1d(speed, pitch, kind="cubic")
speed_new = np.linspace(3, 25, 30)
pitch_new = pitch_interpolated(speed_new)

# Part 1) plot the blade pitch vs wind speed
fig, ax = plt.subplots()
ax.plot(speed, pitch, color="red")
ax.plot(speed_new, pitch_new, color="blue")
ax.set_xlabel("Wind speed [m/s]")
ax.set_ylabel("Blade pitch [deg]")
legend = ax.legend(["Original", "Interpolated"])
ax.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("Figure_6.jpeg", dpi=200)
plt.close("all")

# Part 2)
# load data from "Exercise 1" sheet
dataSeries_test = pd.read_excel(
    "Module 7 - Exercises data.xlsx", sheet_name="Exercise 1"
)
time_test = dataSeries_test["Time (s)"]
speed_test = dataSeries_test["Wind speed (m/s)"]


# define the interpolation function
def interpolation_function(time_test, speed_test, speed, pitch):

    # frequency sampling
    fs = 1 / (time_test[1] - time_test[0])

    # compute the wind speed spectrum using FFT
    spectrum = fftpack.fft(np.array(speed_test))
    freqs = fftpack.fftfreq(len(np.array(speed_test)), d=(time_test[1] - time_test[0]))

    # select only the positive frequencies
    mask = freqs > 0
    f_valid = freqs[mask]
    spectrum_valid = np.abs(spectrum[mask])

    # determine the max frequency
    maxfreq = f_valid[np.argmax(spectrum_valid)]

    # apply a notch filter to remove the peak frequency
    notch_b, notch_a = iirnotch(w0=maxfreq, Q=5, fs=fs)
    wind_speed_notch = filtfilt(notch_b, notch_a, np.array(speed_test))

    # determine the constants for linear fitting
    poly = np.polyfit(speed, pitch, 1)
    m = poly[0]
    c = poly[1]
    y_polyfit = m * wind_speed_notch + c

    def linear_model(x, a, b):
        return a * x + b

    popt, pcov = curve_fit(linear_model, speed, pitch)
    y_curve_fit = linear_model(wind_speed_notch, *popt)

    return y_polyfit, y_curve_fit, wind_speed_notch


# interpolation function
[y_polyfit, y_curve_fit, wind_speed_notch] = interpolation_function(
    time_test, speed_test, speed, pitch
)

# draw the comparison plot
fig, ax = plt.subplots()
ax.plot(wind_speed_notch, y_polyfit, color="red", lw=5)
ax.plot(wind_speed_notch, y_curve_fit, color="blue", lw=2)
ax.set_xlabel("Wind speed [m/s]")
ax.set_ylabel("Blade pitch [deg]")
legend = ax.legend(["polyfit", "curve_fit"])
ax.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("Figure_7.jpeg", dpi=200)
