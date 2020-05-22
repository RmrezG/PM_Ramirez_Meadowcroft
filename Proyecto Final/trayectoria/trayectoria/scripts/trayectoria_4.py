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

def poseCallback1(pose_message):
    global x1
    global y1
    global z1
    global theta1
    
    x1 = pose_message.x
    y1 = pose_message.y
    theta1 = pose_message.theta

def poseCallback2(pose_message):
    global x2
    global y2
    global z2
    global theta2
    
    x2 = pose_message.x
    y2 = pose_message.y
    theta2 = pose_message.theta

def poseCallback4(pose_message):
    global x
    global y
    global z
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def poseCallback3(pose_message):
    global x4
    global y4
    global z4
    global theta4
    
    x4 = pose_message.x
    y4 = pose_message.y
    theta4 = pose_message.theta

def poseCallback5(pose_message):
    global x5
    global y5
    global z5
    global theta5
    
    x5 = pose_message.x
    y5 = pose_message.y
    theta5 = pose_message.theta

def poseCallback6(pose_message):
    global x6
    global y6
    global z6
    global theta6
    
    x6 = pose_message.x
    y6 = pose_message.y
    theta6 = pose_message.theta

def orientate (xgoal, ygoal):
    global x
    global y
    global theta
    global desv

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
	dtheta = desired_angle_goal-theta + desv        
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
        kv = 2				
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

def step ():
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    linear_speed = 0.5

    velocity_message.linear.x = linear_speed
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)
    print ('x=', x, 'y=', y)

def safe_distance():
	
	global esquivaX
	global esquivaY
	global anterior
	global targetX
	global targetY
	global desv
	global x
	global y
	global x1
	global y1
	global x2
	global y2
	global x4
	global y4
	global x5
	global y5
	global x6
	global y6
	global theta
	global theta1
	global theta2
	global theta4
	global theta5
	global theta6

	desv = 0
	esquivaX = 0
	esquivaY = 0

	dif_1_x	= x1 - x
	dif_1_y = y1 - y
	dif_2_x	= x2 - x
	dif_2_y = y2 - y
	dif_4_x	= x4 - x
	dif_4_y = y4 - y
	dif_5_x	= x5 - x
	dif_5_y = y5 - y
	dif_6_x	= x6 - x
	dif_6_y = y6 - y
		
	distance_to_1 = abs(math.sqrt(((dif_1_x)**2)+((dif_1_y)**2)))
	distance_to_2 = abs(math.sqrt(((dif_2_x)**2)+((dif_2_y)**2)))
	distance_to_4 = abs(math.sqrt(((dif_4_x)**2)+((dif_4_y)**2)))
	distance_to_5 = abs(math.sqrt(((dif_5_x)**2)+((dif_5_y)**2)))
	distance_to_6 = abs(math.sqrt(((dif_6_x)**2)+((dif_6_y)**2)))

	if(distance_to_1 < 1 or distance_to_2 < 1 or distance_to_4 < 1 or distance_to_5 < 1 or distance_to_6 < 1):

		lista = [distance_to_1, distance_to_2, distance_to_4, distance_to_5, distance_to_6]
		pos = lista.index(min(lista)) + 1

		if(pos == 1):
			real_dif_x = dif_1_x
			real_dif_y = dif_1_y
			real_theta = theta1
		elif(pos == 2):
			real_dif_x = dif_2_x
			real_dif_y = dif_2_y
			real_theta = theta2
		elif(pos == 3):
			real_dif_x = dif_4_x
			real_dif_y = dif_4_y
			real_theta = theta4
		elif(pos == 4):
			real_dif_x = dif_5_x
			real_dif_y = dif_5_y
			real_theta = theta5
		else:
			real_dif_x = dif_6_x
			real_dif_y = dif_6_y
			real_theta = theta6

		esquivaX = -targetX - 3*real_dif_x + x
		esquivaY = -targetY - 3*real_dif_y + y
			
	elif(distance_to_1 < 1.49 or distance_to_2 < 1.49 or distance_to_4 < 1.49 or distance_to_5 < 1.49 or distance_to_6 < 1.49):
		lista = []
		listaD = []

		theta1_pos = math.atan(dif_1_x/dif_1_y)
		if(dif_1_x < 0):
			theta1_pos = theta1_pos + math.pi
		elif(dif_1_y < 0):
			theta1_pos = theta1_pos + math.pi*2

		theta2_pos = math.atan(dif_2_x/dif_2_y)
		if(dif_2_x < 0):
			theta2_pos = theta2_pos + math.pi
		elif(dif_2_y < 0):
			theta2_pos = theta2_pos + math.pi*2

		theta4_pos = math.atan(dif_4_x/dif_4_y)
		if(dif_4_x < 0):
			theta4_pos = theta4_pos + math.pi
		elif(dif_4_y < 0):
			theta4_pos = theta4_pos + math.pi*2

		theta5_pos = math.atan(dif_5_x/dif_5_y)
		if(dif_5_x < 0):
			theta5_pos = theta5_pos + math.pi
		elif(dif_5_y < 0):
			theta5_pos = theta5_pos + math.pi*2

		theta6_pos = math.atan(dif_6_x/dif_6_y)
		if(dif_6_x < 0):
			theta6_pos = theta6_pos + math.pi
		elif(dif_6_y < 0):
			theta6_pos = theta6_pos + math.pi*2


		if(theta >= math.pi/2 and theta <= math.pi*3/2):
			angleMin = theta - math.pi/2
			angleMax = theta + math.pi/2

			if(angleMin <= theta1_pos and theta1_pos <= angleMax):
				listaD.append(distance_to_1)
				lista.append('distance_to_1')
			if(angleMin <= theta2_pos and theta2_pos <= angleMax):
				listaD.append(distance_to_2)
				lista.append('distance_to_2')
			if(angleMin <= theta4_pos and theta4_pos <= angleMax):
				listaD.append(distance_to_4)
				lista.append('distance_to_4')
			if(angleMin <= theta5_pos and theta5_pos <= angleMax):
				listaD.append(distance_to_5)
				lista.append('distance_to_5')
			if(angleMin <= theta6_pos and theta6_pos <= angleMax):
				listaD.append(distance_to_6)
				lista.append('distance_to_6')

		else:
			angleUp = theta + math.pi/2
			angleDown = theta + 3*math.pi/2

			if((0 <= theta1_pos and theta1_pos <= angleUp) or (2*math.pi >= theta1_pos and theta1_pos >= angleDown)):
				listaD.append(distance_to_1)
				lista.append('distance_to_1')
			if((0 <= theta2_pos and theta2_pos <= angleUp) or (2*math.pi >= theta2_pos and theta2_pos >= angleDown)):
				listaD.append(distance_to_2)
				lista.append('distance_to_2')
			if((0 <= theta4_pos and theta4_pos <= angleUp) or (2*math.pi >= theta4_pos and theta4_pos >= angleDown)):
				listaD.append(distance_to_4)
				lista.append('distance_to_4')
			if((0 <= theta5_pos and theta5_pos <= angleUp) or (2*math.pi >= theta5_pos and theta5_pos >= angleDown)):
				listaD.append(distance_to_5)
				lista.append('distance_to_5')
			if((0 <= theta6_pos and theta6_pos <= angleUp) or (2*math.pi >= theta6_pos and theta6_pos >= angleDown)):
				listaD.append(distance_to_6)
				lista.append('distance_to_6')

		if len(lista) > 0:
			num = listaD.index(min(listaD))
			pos = lista[num]

			if(pos == 'distance_to_1'):
				anterior = 1
				real_dif_x = dif_1_x
				real_dif_y = dif_1_y
				real_theta = theta1
			elif(pos == 'distance_to_2'):
				anterior = 2
				real_dif_x = dif_2_x
				real_dif_y = dif_2_y
				real_theta = theta2
			elif(pos == 'distance_to_4'):
				anterior = 3
				real_dif_x = dif_4_x
				real_dif_y = dif_4_y
				real_theta = theta4
			elif(pos == 'distance_to_5'):
				anterior = 4
				real_dif_x = dif_5_x
				real_dif_y = dif_5_y
				real_theta = theta5
			elif(pos == 'distance_to_6'):
				anterior = 5
				real_dif_x = dif_6_x
				real_dif_y = dif_6_y
				real_theta = theta6

			if(theta - real_theta >= 0):
				desv = math.pi/9
			else:
				desv = -math.pi/9							

if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle4/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic1 = "/turtle1/pose"
        pose_subscriber1 = rospy.Subscriber(position_topic1, Pose, poseCallback1)  

        position_topic2 = "/turtle2/pose"
        pose_subscriber2 = rospy.Subscriber(position_topic2, Pose, poseCallback2)  

        position_topic3 = "/turtle3/pose"
        pose_subscriber3 = rospy.Subscriber(position_topic3, Pose, poseCallback3)  

        position_topic4 = "/turtle4/pose"
        pose_subscriber4 = rospy.Subscriber(position_topic4, Pose, poseCallback4)  

        position_topic5 = "/turtle5/pose"
        pose_subscriber5 = rospy.Subscriber(position_topic5, Pose, poseCallback5)  

        position_topic6 = "/turtle6/pose"
        pose_subscriber6 = rospy.Subscriber(position_topic6, Pose, poseCallback6)  
	
	global x
    	global y
    	global theta
	global targetX
	global targetY
	global desv
	global esquivaX
	global esquivaY
	
	targetX = 1
	targetY = 10
	desv = 0
	esquivaX = 0
	esquivaY = 0

	distance = abs(math.sqrt(((targetX-x)**2)+((targetY-y)**2)))
	time.sleep(0.1)

	while(distance>0.5):	
		safe_distance()
		orientate(esquivaX + targetX, esquivaY + targetY)
		step()
		distance = abs(math.sqrt(((targetX-x)**2)+((targetY-y)**2)))
	
	go_to_goal(targetX,targetY)
	time.sleep(0.5)
	orientate(4,11)
	time.sleep(0.5)
	orientate(4,11)

    except rospy.ROSInterruptException:        
	pass
