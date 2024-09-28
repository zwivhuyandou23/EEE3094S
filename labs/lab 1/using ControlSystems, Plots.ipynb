using ControlSystems, Plots

# Define transfer function coefficients
num1 = 0.753 * 4.393^2
den1 = [1, 2*0.4481*4.393, 4.393^2]
num2 = 5
den2 = [1]

# Create transfer functions
G1 = tf(num1, den1)
G2 = tf(num2, den2)

# Combine transfer functions
G = G1 + G2

# Calculate step response
t, y = step(G)

# Extract performance metrics
info = stepinfo(G)
period = 2 * info.peaktime  # Assuming a second-order system
overshoot = info.overshoot * 100  # Convert to percentage
settling_time = info.settlingtime
settling_amplitude = maximum(y[t > settling_time])

# Plot the step response
plot(t, y, label="Step Response")
xlabel("Time (s)")
ylabel("Output")
title("Step Response")
grid(true)

# Add performance metrics as annotations
text!(settling_time, settling_amplitude, "Settling Amplitude: $(settling_amplitude, digits=2)")
text!((period / 2), maximum(y), "Overshoot: $(overshoot, digits=2)%")

legend!(bottom=true)
show()
