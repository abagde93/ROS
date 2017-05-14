#!/usr/bin/env python
# license removed for brevity
import rospy
from image_pipeline.msg import Floats
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import String
#from std_msgs.msg import Float32

import numpy
import PIL
from PIL import Image

#To get images from path
from scipy import misc
import glob

import matplotlib.pyplot as plt

class Imagesub:

    def callback(self, data):
        print rospy.get_name(), "I heard %s"%str(data.data)

    def image_subscriber(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("single_image", numpy_msg(Floats), self.callback)
        rospy.spin()





if __name__ == '__main__':
    try:
	objName = Imagesub()
        objName.image_subscriber()
    except rospy.ROSInterruptException:
        pass
