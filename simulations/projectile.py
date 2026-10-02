import numpy as np
import matplotlib.pyplot as plt


def generate_trajectory(v0, angle_deg, g=9.81, num_points=100):
    angle_rad = np.radians(angle_deg)

    total_time = (2 * v0 * np.sin(angle_rad)) / g

    t = np.linspace(0, total_time, num_points)

    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

    return t, x, y


def plot_trajectory(x, y, velocity=None, angle=None):
    label = "Trajectory"

    if velocity is not None and angle is not None:
        label = f"v₀ = {velocity} m/s, angle = {angle}°"

    plt.plot(x, y, label=label)

    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.title("Projectile Trajectory")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()