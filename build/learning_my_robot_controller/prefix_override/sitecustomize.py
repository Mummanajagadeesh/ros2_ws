import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jagadeesh97/ros2_ws/install/learning_my_robot_controller'
