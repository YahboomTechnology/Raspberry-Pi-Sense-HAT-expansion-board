#!/usr/bin/python
from sense_hat import SenseHat
import time

sense = SenseHat()

# imu setting（compass_enabled, gyro_enabled, accel_enabled）
# The following settings only turn on gyroscope test data, 
# you need to turn off the magnetometer and accelerometer
sense.set_imu_config(False, True, False)

while True:
    # Obtain gyroscope raw xyz axis data
    # raw = sense.gyro_raw
    # raw = sense.gyroscope_raw
    # raw = sense.get_gyroscope_raw()

    # Read radians value of imu Chip,roll->x, pitch->y, yaw->z
    # Need to match the set_imu_config settings, the content displayed
    # gyr_radians = sense.orientation_radians
    # gyr_radians = sense.get_orientation_radians()

    # Read the angle of the imu chip, set_imu_config modify the settings
    # gyr_degrees = sense.orientation
    # gyr_degrees = sense.get_orientation()

    # The angle of the read-only gyroscope, starting at each start position (0,0,0)
    # gyr_degrees = sense.gyro
    # gyr_degrees = sense.gyroscope
    gyr_degrees = sense.get_gyroscope()

    # Print data
    # print("x: {x}, y: {y}, z: {z}".format(**raw))
    print("p_deg: {pitch}, r_deg: {roll}, y_deg: {yaw}".format(**gyr_degrees))
    # print("p_rad: {pitch}, r_rad: {roll}, y_rad: {yaw}".format(**gyr_radians))

    # Delay 0.2 seconds to avoid sending too fast
    time.sleep(0.2)
