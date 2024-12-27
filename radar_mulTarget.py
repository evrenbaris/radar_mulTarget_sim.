import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)

# Multiple targets with different distances (in meters)
targets = [1000, 2000, 3500]  # Example target distances
pulse_times = [2 * d / c for d in targets]  # Round-trip times for each target

# Generate time array
time = np.linspace(0, 1e-5, 1000)  # 10 microseconds
signal = np.sin(2 * np.pi * 1e6 * time)  # Transmitted signal (1 MHz frequency)

# Create reflected signals with delays
reflected_signals = [np.roll(signal, int(t * len(time) / max(pulse_times))) for t in pulse_times]

# Combine all reflected signals into one
combined_signal = np.sum(reflected_signals, axis=0)

# Add noise to simulate a realistic environment
noise = np.random.normal(0, 0.1, len(time))
noisy_signal = combined_signal + noise

# Plot transmitted and reflected signals
plt.figure(figsize=(12, 6))
plt.plot(time, signal, label="Transmitted Signal")
plt.plot(time, noisy_signal, label="Received Signal (With Noise)", linestyle="--")
plt.legend()
plt.title("Radar Simulation with Multiple Targets")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Print target distances
print("Target Distances (meters):", targets)
# Detect each target
for i, t in enumerate(pulse_times):
    estimated_distance = (c * t) / 2  # Calculate distance
    print(f"Target {i + 1}: Estimated Distance = {estimated_distance:.2f} meters")
