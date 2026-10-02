def validate_velocity(v0):
    if not isinstance(v0, (int, float)):
        raise TypeError("Velocity must be a number.")

    if v0 < 0:
        raise ValueError("Velocity cannot be negative.")

    return True

def validate_angle(angle_deg):
    if not isinstance(angle_deg, (int, float)):
        raise TypeError("Angle must be a number.")

    if angle_deg < 0 or angle_deg > 90:
        raise ValueError("Angle must be between 0 and 90 degrees.")

    return True