#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from geometry_msgs.msg import Twist, Vector3

v = 10  # Velocidade linear
w = 3.1415  # Velocidade angular

def andar(v, tempo):
	global pub
	vel =  Twist(Vector3(v,0,0), Vector3(0,0,0))
	pub.publish(vel)
	rospy.sleep(tempo)

def parar(tempo):
    global pub

    vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
    pub.publish(vel)

    rospy.sleep(tempo)

def virar(v, tempo):
    global pub
    vel = Twist(Vector3(0,0,0), Vector3(0,0,v))
    pub.publish(vel)
    rospy.sleep(tempo)

if __name__ == "__main__":
    rospy.init_node("roda_exemplo")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)

    try:
        while not rospy.is_shutdown():
            parar(1.0)
            andar(v, 4.0)
            parar(1.0)
            virar(w, 1.0)
            parar(1.0)
    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")