#!/usr/bin/env python

# import debugpy
# print("Waiting for VSCode debugger...")
# debugpy.listen(5678)
# debugpy.wait_for_client()

import rospy
import rospkg

from sensor_msgs.msg import Image
from std_msgs.msg import String

from cv_bridge import CvBridge, CvBridgeError
import cv2 as cv

import os

class DeepDreamNode():
    """Handles tasks related to dreaming
    """

    def __init__(self, image_topic):
        rospy.init_node('deep_dream_node')

        self.dream_path = "~/py_dream"
        self.python_file = self.dream_path + "/deepdream.py"

        self.rospack = rospkg.RosPack()
        self.deepdream_pkg_path = self.rospack.get_path('deepDreamEZ')
        self.init_img_path = self.deepdream_pkg_path + "/checkers_dream.jpg"

        self.ros_rate = rospy.Rate(10.0)

        self.zedSub                 = rospy.Subscriber(image_topic, Image, self.camera_callback)
        self.resetSub               = rospy.Subscriber('/dream/run', String, self.doDream)

        self.deep_dream_pub            = rospy.Publisher('/dream/img', Image, queue_size= 1)

        self.bridge = CvBridge()

        # First initialization of image shape
        rospy.loginfo("Waiting for the first image msg...")
        first_image_msg = rospy.wait_for_message(image_topic, Image)
        rospy.loginfo("Msg received!")

        self.cv_image = self.bridge.imgmsg_to_cv2(first_image_msg, "passthrough")
        self.image_shape = self.cv_image.shape

        self.dream_img = cv.imread(self.init_img_path)

    def cv_image_publisher(self, publisher, image, msg_encoding="bgra8"):
        """
        Takes a cv::Mat image object, converts it into a ROS Image message type, and publishes it using the specified publisher.
        """
        msgified_img = self.bridge.cv2_to_imgmsg(image, encoding=msg_encoding)
        publisher.publish(msgified_img)
    
    def spin(self):
        while not rospy.is_shutdown():            
            if self.cv_image is not None:
                self.cv_image_publisher(self.deep_dream_pub, self.dream_img, "bgr8")


    def camera_callback(self, img_msg):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(img_msg, "passthrough")
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))

    def doDream(self, msg):
        rospy.loginfo("DREAM")
        cv.imwrite(self.deepdream_pkg_path + "/img_to_dreamify.jpg", self.cv_image)

        if msg.data == "" or msg.data == "relu4_3":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg")
        elif msg.data == "relu5_3":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name VGG16_EXPERIMENTAL --layers_to_use relu5_3")
        elif msg.data == "relu5_1":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name VGG16_EXPERIMENTAL --layers_to_use relu5_1")
        elif msg.data == "relu4_1":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name VGG16_EXPERIMENTAL --layers_to_use relu4_1")
        elif msg.data == "relu3_3":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name VGG16_EXPERIMENTAL --layers_to_use relu3_3")
        elif msg.data == "inception4e":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name GOOGLENET --layers_to_use inception4e")
        elif msg.data == "inception4d":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name GOOGLENET --layers_to_use inception4d")
        elif msg.data == "inception4c":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name GOOGLENET --layers_to_use inception4c")
        elif msg.data == "alexnet4":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name ALEXNET --layers_to_use relu4")
        elif msg.data == "alexnet5":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name ALEXNET --layers_to_use relu5")
        elif msg.data == "alexnet3":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name ALEXNET --layers_to_use relu3")
        elif msg.data == "resnet4":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name RESNET50 --layers_to_use layer4")
        elif msg.data == "resnet3":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name RESNET50 --layers_to_use layer3")
        elif msg.data == "resnet2":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name RESNET50 --layers_to_use layer2")
        elif msg.data == "resnet1":
            os.system("python3 " + self.python_file + " --input " + self.deepdream_pkg_path + "/img_to_dreamify.jpg --model_name RESNET50 --layers_to_use layer1")
        else:
            rospy.logwarn("INCORRECT COMMAND")


        self.dream_img = cv.imread(self.deepdream_pkg_path + "/dreamified_img.jpg")


    def dynam_reconfigure_callback(self, config):
        self.canny_threshold1 = config.canny_threshold1
        self.canny_threshold2 = config.canny_threshold2
        self.canny_aperture = config.canny_aperture_size


if __name__ == '__main__':
    try:
        deep_dream_node = DeepDreamNode(image_topic='/zed2i/zed_node/rgb/image_rect_color')
        # rospy.spin()
        deep_dream_node.spin()

    except rospy.ROSInterruptException:
        pass