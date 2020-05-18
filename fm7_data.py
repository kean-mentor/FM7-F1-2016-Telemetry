import ctypes


class FM7TelemetryData(ctypes.LittleEndianStructure):
    """fl=front left, fr=front right, rl=rear left, rr=rear right"""

    _pack_ = 1
    _fields_ = [
        ('is_race_on', ctypes.c_int),  # 1 when race is on, 0 when in menus/race stopped
        ('timestamp_ms', ctypes.c_uint),
        ('engine_max_rpm', ctypes.c_float),
        ('engine_idle_rpm', ctypes.c_float),
        ('current_engine_rpm', ctypes.c_float),
        ('acceleration_x', ctypes.c_float),  # In the car's local space, x=right, y=up, z=forward
        ('acceleration_y', ctypes.c_float),
        ('acceleration_z', ctypes.c_float),
        ('velocity_x', ctypes.c_float),
        ('velocity_y', ctypes.c_float),
        ('velocity_z', ctypes.c_float),
        ('angular_velocity_x', ctypes.c_float),  # In the car's local space, x=pitch, y=yaw, z=roll
        ('angular_velocity_y', ctypes.c_float),
        ('angular_velocity_z', ctypes.c_float),
        ('yaw', ctypes.c_float),
        ('pitch', ctypes.c_float),
        ('roll', ctypes.c_float),
        ('normalized_suspension_travel_fl', ctypes.c_float),  # Suspension travel normalized: 0.0f=max stretch, 1.0=max compression
        ('normalized_suspension_travel_fr', ctypes.c_float),
        ('normalized_suspension_travel_rl', ctypes.c_float),
        ('normalized_suspension_travel_rr', ctypes.c_float),
        ('tire_slip_ratio_fl', ctypes.c_float),  # Tire normalized slip ratio, 0 means 100% grip and > 1.0 means loss of grip
        ('tire_slip_ratio_fr', ctypes.c_float),
        ('tire_slip_ratio_rl', ctypes.c_float),
        ('tire_slip_ratio_rr', ctypes.c_float),
        ('wheel_rotation_speed_fl', ctypes.c_float),  # Wheel rotation speed radians/sec
        ('wheel_rotation_speed_fr', ctypes.c_float),
        ('wheel_rotation_speed_rl', ctypes.c_float),
        ('wheel_rotation_speed_fl', ctypes.c_float),
        ('wheel_on_rumble_strip_fl', ctypes.c_float),  # 1 when wheel is on rumble strip, 0 when off
        ('wheel_on_rumble_strip_fr', ctypes.c_float),
        ('wheel_on_rumble_strip_rl', ctypes.c_float),
        ('wheel_on_rumble_strip_rr', ctypes.c_float),
        ('wheel_in_puddle_depth_fl', ctypes.c_float),  # from 0 to 1, where 1 is the deepest puddle
        ('wheel_in_puddle_depth_fr', ctypes.c_float),
        ('wheel_in_puddle_depth_rl', ctypes.c_float),
        ('wheel_in_puddle_depth_rr', ctypes.c_float),
        ('surface_rumble_fl',  ctypes.c_float),  # Non-dimensional surface rumble values passed to controller force feedback
        ('surface_rumble_fr', ctypes.c_float),
        ('surface_rumble_rl', ctypes.c_float),
        ('surface_rumble_rr', ctypes.c_float),
        ('tire_slip_angle_fl', ctypes.c_float),  # Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
        ('tire_slip_angle_fr', ctypes.c_float),
        ('tire_slip_angle_rl', ctypes.c_float),
        ('tire_slip_angle_rr', ctypes.c_float),
        ('tire_combined_slip_fl', ctypes.c_float),  # Tire normalized combined slip, = 0 means 100% grip and |slip| > 1.0 means loss of grip.
        ('tire_combined_slip_fr', ctypes.c_float),
        ('tire_combined_slip_rl', ctypes.c_float),
        ('tire_combined_slip_rr', ctypes.c_float),
        ('suspension_travel_meters_fl', ctypes.c_float),  # Actual suspension travel in meters
        ('suspension_travel_meters_fr', ctypes.c_float),
        ('suspension_travel_meters_rl', ctypes.c_float),
        ('suspension_travel_meters_rr', ctypes.c_float),
        ('car_ordinal', ctypes.c_int),   # Unique ID of the car make/model
        ('car_class', ctypes.c_int),  # Between 0 (D -- worst cars) and 7 (X class -- best cars) inclusive 
        ('car_performance_index', ctypes.c_int),  # Between 100 (slowest car) and 999 (fastest car) inclusive
        ('drivetrain_type', ctypes.c_int),  # 0 = FWD, 1 = RWD, 2 = AWD
        ('num_cylinders', ctypes.c_int),  # Number of cylinders in the engine
        ('position_x', ctypes.c_float),
        ('position_y', ctypes.c_float),
        ('position_z', ctypes.c_float),
        ('speed', ctypes.c_float),  # meters per second
        ('power', ctypes.c_float),  # watts
        ('torque', ctypes.c_float),  # newton meter
        ('tire_temp_fl', ctypes.c_float),
        ('tire_temp_fr', ctypes.c_float),
        ('tire_temp_rl', ctypes.c_float),
        ('tire_temp_rr', ctypes.c_float),
        ('boost', ctypes.c_float),
        ('fuel', ctypes.c_float),
        ('distance_traveled', ctypes.c_float),
        ('best_lap', ctypes.c_float),  # Best clean lap (or dirty if all laps are dirty).
        ('last_lap', ctypes.c_float),
        ('current_lap', ctypes.c_float),
        ('current_race_time', ctypes.c_float),
        ('lap_number', ctypes.c_ushort),
        ('race_position', ctypes.c_uint8),
        ('accel', ctypes.c_uint8),
        ('brake', ctypes.c_uint8),
        ('clutch', ctypes.c_uint8),
        ('handbreak', ctypes.c_uint8),
        ('gear', ctypes.c_uint8),
        ('steer', ctypes.c_int8),
        ('normalized_driving_line', ctypes.c_int8),
        ('normalized_ai_brake_difference', ctypes.c_int8)
    ]
