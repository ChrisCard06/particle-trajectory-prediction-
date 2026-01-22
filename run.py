from src.physics.orbit_simulator import simulate_orbit
import matplotlib.pyplot as plt

# Initial conditions (circular-ish orbit)
r0 = [1.0, 0.0]
v0 = [0.0, 1.0]

trajectory = simulate_orbit(r0, v0, dt=0.01, steps=5000)

x = trajectory[:, 0]
y = trajectory[:, 1]

plt.plot(x, y)
plt.scatter([0], [0], color='red')  # central body
plt.xlabel("x")
plt.ylabel("y")
plt.title("Simulated Orbit")
plt.axis("equal")
plt.show()

