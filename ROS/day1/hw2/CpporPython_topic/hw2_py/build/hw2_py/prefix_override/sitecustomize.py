import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mso/Desktop/intern_ws/ROS/day1/hw2_py/install/hw2_py'
