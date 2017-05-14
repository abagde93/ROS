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

class Imagepub:

	pub = rospy.Publisher('single_image', numpy_msg(Floats), queue_size=10)
	rospy.init_node('image_streamer', anonymous=True)


	def image_publisher(self, img):
		rate = rospy.Rate(10)
		self.pub.publish(img)
		rate.sleep()

	def get_image(self):
		for image_path in glob.glob("/home/abagde/machine_learning_algorithms/Test/*.png"):
			rospy.logwarn(image_path)
			#Open image, and save as greyscale, "L" option
			img = PIL.Image.open(image_path).convert("L")
			img_array = numpy.array(img, dtype=numpy.float32)
			self.image_publisher(img_array)




if __name__ == '__main__':
    try:
	objName = Imagepub()
    	objName.get_image()
    except rospy.ROSInterruptException:
        pass
