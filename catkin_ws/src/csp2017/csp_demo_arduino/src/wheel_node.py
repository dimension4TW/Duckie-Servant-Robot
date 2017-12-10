#!/usr/bin/env python
import rospy
import numpy as np
from duckietown_msgs.msg import BoolStamped, Twist2DStamped

class arduinoWheel(object):
    def __init__(self):
        self.check = BoolStamped()
        # =========== publisher ===========
        # publish to topic "car_cmd" (you may have to see the code last week)
        self.pub_car_cmd = rospy.Publisher("~cbresult", Twist2DStamped, queue_size = 1)
        print 'here1'
        # =========== subscriber ===========
        # subscribe to topic "result" (you should see arduino_node.py)
        self.sub_result = rospy.Subscriber("~result", BoolStamped, self.callback, queue_size = 1)
        print 'here2'


    def callback(self, msg):
        self.check = msg
        self.cbresult()
        self.stop()

   # =========== subscribe distance from arduino ===========
    def cbresult(self):
        print 'here3', self.check.data
        cmd = Twist2DStamped()
        if self.check.data == False:
            print 'A'
            cmd.v = 0.2
            cmd.omega = 0
            self.pub_car_cmd.publish(cmd)
            #print self.dis, "go forward"
        else:
            print 'B'
            cmd.v = -0.2
            cmd.omega = 0
            self.pub_car_cmd.publish(cmd)
            #print self.dis, "go backward"
        #print self.pub_car_cmd

    def stop(self):
        rospy.sleep(0.2)
        cmd = Twist2DStamped()
        cmd.v = 0
        cmd.omega = 0
        self.pub_car_cmd.publish(cmd)

if __name__ == "__main__":
    rospy.init_node("arduino_wheel", anonymous = False)
    arduino_node = arduinoWheel()
    #while True:
    #    arduino_node.cbresult()
    rospy.spin()
