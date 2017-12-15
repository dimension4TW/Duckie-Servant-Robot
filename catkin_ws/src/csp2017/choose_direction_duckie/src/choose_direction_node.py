import rospkg
import rospy
import yaml
from duckietown_msgs.msg import AprilTagDetectionArray, Twist2DStamped, BoolStamped
import numpy as np
import tf.transformations as tr
from geometry_msgs.msg import PoseStamped, Point

class AprilFollow(object):

	def __init__(self):    
	self.node_name = "follow_apriltags_node"
	self.pose = Point()

	# -------- subscriber --------
	self.sub_id = rospy.Subscriber("demo_apriltags_node/id_info", BoolStamped, self.callback, queue_size=1)
	self.sub_switch = rospy.Subscriber("~switch",BoolStamped, self.callback, queue_size=1)

	# -------- publisher --------
	self.pub_car_cmd = rospy.Publisher("~car_cmd", Twist2DStamped, queue_size=1)
	self.pub_finish_turn = rospy.Publisher("~finish_turn", BoolStamped, queue_size=1)

	print ("Start to choose direction")

	def cbswitch(self, msg):
		self.active = msg
		if(!msg.data):
            finish = BoolStamped()
			finish.data = False
			self.pub_finish_turn.publish(finish)

	def callback(self, msg):
		if(self.active.data):
			self.id = msg
			self.car_cmd()
			self.stop()
			finish = BoolStamped()
			finish.data = True
			self.pub_finish_turn.publish(finish)
		else:
			return

	def car_cmd(self):
		
		cmd = Twist2DStamped()
		"""
		if self.pose.z > 0.15:#if the tag is too far
		cmd.v = 0.2
		elif self.pose.z < 0.20: #if the tag is too close
		cmd.v = -0.2
		else: # distance is between 0.15~0.20 
		cmd.v = 0

		if self.pose.x > 0.02: #if the tag is at right side
		cmd.omega = -1.8
		elif self.pose.x < -0.02: #if the tag is at left side
		cmd.omega = 1.8
		else: # do not turn
		cmd.omega = 0
		print(cmd)
		#publish the cmd
		self.pub_car_cmd.publish(cmd)
		"""
		cmd.v = 0.2
		cmd.omega = 5
		self.pub_car_cmd.publish(cmd)
		print(cmd)
		rospy.sleep(1)

	# make the robot stop
	def stop(self):
		rospy.sleep(0.2)
		cmd = Twist2DStamped()
		cmd.v = 0
		cmd.omega = 0
		print(cmd)
		#publish the cmd
		self.pub_car_cmd.publish(cmd)
		

	if __name__ == '__main__': 
		rospy.init_node('AprilPostPros',anonymous=False)
		node = AprilFollow()
		rospy.spin()


