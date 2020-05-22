#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
theta = 0

def poseCallback(pose_message):
    global x
    global y
    global z
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def orientate (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        ka = 4.0
        if (xgoal - x == 0 and ygoal - y < 0):
		desired_angle_goal = -math.pi/2
	if (xgoal - x == 0 and ygoal - y > 0):
		desired_angle_goal = math.pi/2
	else:
		desired_angle_goal = math.atan2(ygoal-y, xgoal-x)	
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = 0.0
        velocity_message.angular.z = angular_speed
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (dtheta < 0.01):
            break

def go_to_goal (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        kv = 0.5				
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 4.0
        if (xgoal - x == 0 and ygoal - y < 0):
		desired_angle_goal = -math.pi/2
	if (xgoal - x == 0 and ygoal - y > 0):
		desired_angle_goal = math.pi/2
	else:
		desired_angle_goal = math.atan2(ygoal-y, xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (distance < 0.01):
            break

if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)     
	
	global x
    	global y
    	global theta
	
	print('Inserta radio: ')
	r = input()	

	phase = math.atan2(y-5.5, x-5.5)
	h = 5.5
	k = 5.5
	thI = theta
	
	print('Inserta modalidad de trayectoria (Horario = -1 / Antihorario = 1): ')
	modo = input()	
	
	for i in range(0,361,5):
		xg = r*math.cos(phase + modo*i*math.pi/180)
		yg = r*math.sin(phase + modo*i*math.pi/180)
		orientate(h + xg,k + yg)
		time.sleep(0.3)
		orientate(h + xg,k + yg)
		time.sleep(0.01)
		go_to_goal(h + xg,k + yg)
		time.sleep(0.1)

    except rospy.ROSInterruptException:        
	pass
