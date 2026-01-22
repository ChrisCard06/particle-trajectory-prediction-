import numpy as np
from src.physics.orbit_simulator import simulate_orbit

def generate_orbit_dataset(num_samples=100, steps=1000):
    X = []
    Y = []

    for _ in range(num_samples):
        r0 = np.random.uniform(0.5, 2.0, size=2)
        v0 = np.random.uniform(-1.0, 1.0, size=2)

        trajectory = simulate_orbit(r0, v0, dt=0.01, steps=steps)

        # Inputs: current position & velocity
        # Targets: next position & velocity
        for i in range(len(trajectory) - 1):
            X.append(np.concatenate([trajectory[i], trajectory[i+1] - trajectory[i]]))
            Y.append(trajectory[i+1])

    return np.array(X), np.array(Y)

