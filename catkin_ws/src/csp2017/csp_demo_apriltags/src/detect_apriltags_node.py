#!/usr/bin/env python
import rospkg
import rospy
import yaml
from duckietown_msgs.msg import AprilTagDetectionArray, BoolStamped
import numpy as np
import tf.transformations as tr
from geometry_msgs.msg import PoseStamped, Point
from std_msgs.msg import Float32, Int32

class AprilPostPros(object):

    def __init__(self):    
        self.node_name = "detect_apriltags_node"

        # -------- subscriber --------
        self.sub_prePros = rospy.Subscriber("~tag_info", AprilTagDetectionArray, self.callback, queue_size=1)

        # -------- publisher --------
        self.pub_info = rospy.Publisher("~position_info", Point, queue_size=1)
        self.pub_id = rospy.Publisher("~id_info", Int32, queue_size=1) #publish apriltags id
        self.pub_turn = rospy.Publisher("~turn_info",BoolStamped, queue_size=1)

        print ("Start to detect apriltags:")

    def callback(self, msg):
        # Load tag detections message
        turn = BoolStamped()
        turn.data = False
        if(len(msg.detections) == 0):
            turn.data = False
        for detection in msg.detections:
            #Try to print the ID and position of the apriltags
            tag_id = detection.id
            x = detection.pose.pose.position.x
            y = detection.pose.pose.position.y
            z = detection.pose.pose.position.z
            print ("ID: ", tag_id)
            print ("(x,y,z): ", x, y, z)

            #send the msg of the poing
            #pos = Point()
            pos = detection.pose.pose.position
            self.pub_info.publish(pos)
            #publish ID
            aid = tag_id
            self.pub_id.publish(aid)
            turn.data = True
            self.pub_turn.publish(turn)

        
if __name__ == '__main__': 
    rospy.init_node('AprilPostPros',anonymous=False)
    node = AprilPostPros()
    rospy.spin()
