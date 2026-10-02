import math


def time_of_flight(v0, angle_deg, g=9.81):
    angle_rad = math.radians(angle_deg)
    return (2 * v0 * math.sin(angle_rad)) / g


def max_height(v0, angle_deg, g=9.81):
    angle_rad = math.radians(angle_deg)
    return (v0**2 * math.sin(angle_rad)**2) / (2 * g)


def range_projectile(v0, angle_deg, g=9.81):
    angle_rad = math.radians(angle_deg)
    return (v0**2 * math.sin(2 * angle_rad)) / g