import matplotlib.pyplot as plt

EnergySource = [
    "Crude Oil",
    "Natural Gas",
    "Renewable Energies",
    "Solid Fuels",
    "Nuclear Energy",
]
Percentage = [37.7, 20.4, 19.5, 10.6, 11.8]

# fig = plt.figure(num=1, figsize=(5, 5))
fig = plt.figure(num=1)
ax = plt.axes()

# cdax.plot(EnergySource, Percentage, marker="x", color="red")
# plt.show(block=False)
ax.bar(EnergySource, Percentage, color="blue")
# ax.set_xlabel("Energy Source")
ax.set_ylabel("Total Energy Generation (%)")
plt.xticks(rotation=45)
# plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
# ax.set_title("Global Primary Energy Consumption by Source in 2020")
ax.grid(True)
ax.legend(["Energy Source vs Percentage"])
plt.show()


plt.savefig("Figure_1.jpeg", dpi=300)
