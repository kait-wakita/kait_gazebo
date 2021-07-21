#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


rospy.init_node('keyboard_cmd_vel')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
while not rospy.is_shutdown():
    vel=Twist()
    direction = raw_input('w: forward z:backward a:left d:right Enter:stop q:quit> ')
    if 'w' in direction:
        vel.linear.x = 0.5
    if 'z' in direction:
        vel.linear.x = -0.5
    if 'a' in direction:
        vel.linear.x = 0.5
        vel.angular.z = 3.14/8
    if 'd' in direction:
        vel.linear.x = 0.5
        vel.angular.z = -3.14/8
    if 'q' in direction:
        break
    print vel
    pub.publish(vel)
