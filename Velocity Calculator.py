def calculate_velocity(vi, a, t):
    vel = vi + (a * t)
    return vel
    
init_vel = int(input("Initial Velocity: "))
accel = int(input("Acceleration (m/s,f/s, etc): "))
time = int(input("Time (sec): "))

print("Final Velocity: " + str(calculate_velocity(init_vel, accel, time)))
