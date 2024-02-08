#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2


class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        self.pose = data

    def steering_angle(self):
        return atan2(self.pose.y - 5.5, self.pose.x - 5.5)

    def move_in_circle(self):
        twist = Twist()
        twist.linear.x = 1.0  # linear velocity
        twist.angular.z = 0.5  # Constant angular velocity to make the turtle move in a circle
        while not rospy.is_shutdown():
            self.velocity_publisher.publish(twist)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move_in_circle()
    except rospy.ROSInterruptException:
        pass
