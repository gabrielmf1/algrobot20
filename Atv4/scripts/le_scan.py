#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy

import numpy as np

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

valor_dist = 0
def scaneou(dado):
	print("Faixa valida: ", dado.range_min , " - ", dado.range_max )
	print("Leituras:")
	print(np.array(dado.ranges).round(decimals=2))
	#print("Intensities")
	#print(np.array(dado.intensities).round(decimals=2))
	global valor_dist
	if dado.range_min < dado.ranges[0] < dado.range_max:
		valor_dist = dado.ranges[0]

	


if __name__=="__main__":

	rospy.init_node("le_scan")

	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
	recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)



	while not rospy.is_shutdown():
		print("Oeee")

		if valor_dist > 1.02:
			velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0))

		elif valor_dist < 1.0:
			velocidade = Twist(Vector3(-0.1, 0, 0), Vector3(0, 0, 0))



		velocidade_saida.publish(velocidade)
		rospy.sleep(0.5)
