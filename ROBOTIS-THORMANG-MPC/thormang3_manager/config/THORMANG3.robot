[ control info ]
control_cycle = 8   # milliseconds

[ port info ]
# PORT NAME  | BAUDRATE | DEFAULT JOINT
/dev/ttyUSB0 | 1000000  | r_leg_hip_p


[ device info ]
# TYPE    | PORT NAME    | ID  | MODEL          | PROTOCOL | DEV NAME     | BULK READ ITEMS

dynamixel | /dev/ttyUSB0 | 1   | MX-64          | 1.0      | r_leg_hip_p  | present_position, present_voltage
dynamixel | /dev/ttyUSB0 | 2   | MX-64          | 1.0      | l_leg_hip_p  | present_position, present_voltage

