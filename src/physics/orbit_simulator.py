import numpy as np

def gravitational_acceleration(r, mu=1.0):
    """
    Compute acceleration due to gravity.
    r: position vector (x, y)
    mu: gravitational parameter (GM)
    """
    distance = np.linalg.norm(r)
    return -mu * r / distance**3

def simulate_orbit(r0, v0, dt=0.01, steps=10000, mu=1.0):
    """
    Simulate an orbit using Euler's method.
    r0: initial position vector
    v0: initial velocity vector
    dt: time step
    steps: number of simulation steps
    """
    r = np.array(r0, dtype=float)
    v = np.array(v0, dtype=float)

    trajectory = [r.copy()]


    for _ in range(steps):
        a = gravitational_acceleration(r, mu)
        v = v + a * dt
        r = r + v * dt
        trajectory.append(r.copy())

    return np.array(trajectory)


