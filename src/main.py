from src.physics import time_of_flight, max_height, range_projectile
from src.validation import validate_velocity, validate_angle
from simulations.projectile import generate_trajectory, plot_trajectory


def main():
    try:
        velocity = float(input("Enter initial velocity (m/s): "))
        angle = float(input("Enter launch angle (degrees): "))

        validate_velocity(velocity)
        validate_angle(angle)

    except (ValueError, TypeError) as error:
        print(f"\nInput error: {error}")
        return

    flight_time = time_of_flight(velocity, angle)
    height = max_height(velocity, angle)
    distance = range_projectile(velocity, angle)

    print("\nProjectile Results")
    print("------------------")
    print(f"Time of flight: {flight_time:.2f} s")
    print(f"Maximum height: {height:.2f} m")
    print(f"Range: {distance:.2f} m")

    t, x, y = generate_trajectory(velocity, angle)
    plot_trajectory(x, y, velocity, angle)

if __name__ == "__main__":
    main()    