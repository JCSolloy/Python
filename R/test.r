# Plot a sine wave
x <- seq(0, 2*pi, length.out=100)

plot(x, sin(x), type="l", col="blue")

# Save the plot to a file

dev.copy(png, file="sine_wave.png")
dev.off()

