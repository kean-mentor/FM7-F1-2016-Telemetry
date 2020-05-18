import ctypes


class F12016TelemetryData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('time', ctypes.c_float),
        ('lap_time', ctypes.c_float),
        ('lap_distance', ctypes.c_float),
        ('total_distance', ctypes.c_float),
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
        ('z', ctypes.c_float),
        ('speed', ctypes.c_float),
        ('xv', ctypes.c_float),
        ('yv', ctypes.c_float),
        ('zv', ctypes.c_float),
        ('xr', ctypes.c_float),
        ('yr', ctypes.c_float),
        ('zr', ctypes.c_float),
        ('xd', ctypes.c_float),
        ('yd', ctypes.c_float),
        ('zd', ctypes.c_float),
        ('susp_pos_bl', ctypes.c_float),
        ('susp_pos_br', ctypes.c_float),
        ('susp_pos_fl', ctypes.c_float),
        ('susp_pos_fr', ctypes.c_float),
        ('susp_vel_bl', ctypes.c_float),
        ('susp_vel_br', ctypes.c_float),
        ('susp_vel_fl', ctypes.c_float),
        ('susp_vel_fr', ctypes.c_float),
        ('wheel_speed_bl', ctypes.c_float),
        ('wheel_speed_br', ctypes.c_float),
        ('wheel_speed_fl', ctypes.c_float),
        ('wheel_speed_fr', ctypes.c_float),
        ('throttle', ctypes.c_float),
        ('steer', ctypes.c_float),
        ('brake', ctypes.c_float),
        ('clutch', ctypes.c_float),
        ('gear', ctypes.c_float),
        ('gforce_lat', ctypes.c_float),
        ('gforce_lon', ctypes.c_float),
        ('lap', ctypes.c_float),
        ('engine_rate', ctypes.c_float),
        ('sli_pro_native_support', ctypes.c_float),
        ('car_position', ctypes.c_float),
        ('kers_level', ctypes.c_float),
        ('kers_max_level', ctypes.c_float),
        ('drs', ctypes.c_float),
        ('traction_control', ctypes.c_float),
        ('anti_lock_brakes', ctypes.c_float),
        ('fuel_in_tank', ctypes.c_float),
        ('fuel_capacity', ctypes.c_float),
        ('in_pits', ctypes.c_float),
        ('sector', ctypes.c_float),
        ('sector1_time', ctypes.c_float),
        ('sector2_time', ctypes.c_float),
        ('brakes_temp', ctypes.c_float * 4),
        ('wheels_pressure', ctypes.c_float * 4),
        ('team_info', ctypes.c_float),
        ('total_laps', ctypes.c_float),
        ('track_size', ctypes.c_float),
        ('last_lap_times', ctypes.c_float),
        ('max_rpm', ctypes.c_float),
        ('idle_rpm', ctypes.c_float),
        ('max_gears', ctypes.c_float),
        ('session_type', ctypes.c_float),
        ('drs_allowed', ctypes.c_float),
        ('track_number', ctypes.c_float),
        ('vehicle_fia_flags', ctypes.c_float) 
    ]


teams = {
    0: 'Red Bull',
    1: 'Ferrari',
    2: 'McLaren',
    3: 'Lotus',
    4: 'Mercedes',
    5: 'Sauber',
    6: 'Force India',
    7: 'Williams',
    8: 'Toro Rosso',
    9: 'Catherham',
    10: 'Marussia',
    11: 'Haas',
    12: 'Manor'
}


tracks = {
    0: 'Melbourne',
    1: 'Sepang',
    2: 'Shanghai',
    3: 'Sakhir (Bahrain)',
    4: 'Catalunya',
    5: 'Monaco',
    6: 'Montreal',
    7: 'Silverstone',
    8: 'Hockenheim',
    9: 'Hungaroring',
    10: 'Spa',
    11: 'Monza',
    12: 'Singapore',
    13: 'Suzuka',
    14: 'Abu Dhabi',
    15: 'Texas',
    16: 'Brazil',
    17: 'Austria',
    18: 'Sochi',
    19: 'Mexico',
    20: '(unused)',
    21: 'Baku (Azerbaijan)'
}