import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import fftpack
from scipy.signal import butter, iirnotch, filtfilt, welch

# load data from three excel sheets
dataSeries = pd.read_excel("Module 7 - Exercises data.xlsx", sheet_name="Exercise 1")
time = dataSeries["Time (s)"]
speed = dataSeries["Wind speed (m/s)"]

# frequency sampling
fs = 1 / (time[1] - time[0])

# Part1) plot the wind speed time series
fig, ax = plt.subplots()
ax.plot(time, speed, color="black")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Wind speed [m/s]")
ax.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("Figure_1.jpeg", dpi=200)
plt.close("all")

# Part 2)
# compute the wind speed spectrum using FFT
spectrum = fftpack.fft(np.array(speed))
freqs = fftpack.fftfreq(len(np.array(speed)), d=(time[1] - time[0]))

# select only the positive frequencies
mask = freqs > 0
f_valid = freqs[mask]
spectrum_valid = np.abs(spectrum[mask])

# determine the max frequency
maxfreq = f_valid[np.argmax(spectrum_valid)]

# apply a notch filter to remove the peak frequency
notch_b, notch_a = iirnotch(w0=maxfreq, Q=5, fs=fs)
wind_speed_notch = filtfilt(notch_b, notch_a, np.array(speed))

# compute the wind speed spectrum of the filtered signal
spectrum2 = fftpack.fft(wind_speed_notch)
freqs2 = fftpack.fftfreq(len(wind_speed_notch), d=(time[1] - time[0]))

# select only the positive frequencies
mask2 = freqs2 > 0
f_valid2 = freqs2[mask2]
spectrum_valid2 = np.abs(spectrum2[mask2])

# print the removed frequency
print(f"Removed frequency: {maxfreq:.2f} Hz")

# welch method to estimate the PSD
f, PSD = welch(wind_speed_notch, fs=fs, nperseg=fs)

# plot the characteristic wind speed spectrum
fig, ax = plt.subplots()
ax.plot(f_valid, spectrum_valid, color="black")
ax.plot(f_valid2, spectrum_valid2, color="orange")
ax.set_xscale("log")
ax.legend(["Non-filtered signal", "Filtered signal"])
plt.tight_layout()
plt.show()
plt.savefig("Figure_2.jpeg", dpi=200)
plt.close("all")

# plot the characteristic wind speed spectrum
fig, ax = plt.subplots()
ax.plot(f, PSD, color="orange")
plt.tight_layout()
plt.savefig("Figure_3.jpeg", dpi=200)
plt.show()
plt.close("all")

# PART 3)
cutoff = [0.0025, 0.005, 0.05, 0.2]


# define a butter_filter function
def butter_filter(data, cutoff, fs, order=4, btype="low"):
    nyq = 0.5 * fs
    normal_cutoff = np.array(cutoff) / nyq
    b, a = butter(order, normal_cutoff, btype=btype, analog=False)
    return filtfilt(b, a, data)


# a) apply a low-pass filter before filtering
fig, ax = plt.subplots()
filtered_signals = []
for fcut in cutoff:
    low_pass = butter_filter(np.array(speed), fcut, fs, btype="low")
    ax.plot(time, low_pass, label=f"cutoff = {fcut:.4f} Hz")

ax.plot(time, speed, label="Original")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Speed")
ax.legend()
plt.show()
plt.savefig("Figure_4.jpeg", dpi=200)
plt.close("all")

# b) apply a low-pass filter after filtering
fig, ax = plt.subplots()
filtered_signals = []
for fcut in cutoff:
    low_pass = butter_filter(np.array(speed), fcut, fs, btype="low")
    spectrum3 = fftpack.fft(low_pass)
    freqs3 = fftpack.fftfreq(len(low_pass), d=(time[1] - time[0]))

    # select only the positive frequencies
    mask3 = freqs3 > 0
    f_valid3 = freqs3[mask3]
    spectrum_valid3 = np.abs(spectrum3[mask3])

    ax.plot(f_valid3, spectrum_valid3, label=f"cutoff = {fcut:.4f} Hz")

ax.plot(time, speed, label="Original")
ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Signal Amplitude")
ax.legend()
plt.show()
plt.savefig("Figure_5.jpeg", dpi=200)

print(
    f"The cutoff frequency that offers the best trade-off between signal\
       smoothness and information loss is 0.005 Hz"
)
