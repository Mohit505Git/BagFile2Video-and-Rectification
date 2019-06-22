#!/usr/bin/env python
from __future__ import print_function
    
import roslib
# roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (752,480),False)
   
class image_converter:
	def __init__(self):
		self.bridge = CvBridge()
		# self.bridge2 = CvBridge()
		self.left_image_sub = rospy.Subscriber("stereo/right/image",Image,self.left_callback)
   
	def left_callback(self,data):
		
		cv_image = self.bridge.imgmsg_to_cv2(data, "mono8")
   		out.write(cv_image)

		cv2.imshow("Image window", cv_image)
		cv2.waitKey(3)

def main():
	ic = image_converter()
	rospy.init_node('image_converter', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	out.release()	
	cv2.destroyAllWindows()
   
if __name__ == '__main__':
	main()