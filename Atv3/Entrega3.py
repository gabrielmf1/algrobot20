#! /usr/bin/env python
# -*- coding:utf-8 -*-

#Imports
from __future__ import print_function

import cv2
import imutils
import numpy as np
import math
from math import acos, degrees, sqrt
import sys

#Parametros de teste
#p1 = [3.0,2.5]
#p2 = [4.0,0.6]
#q1 = [1.0,2.4]
#q2 = [0.6,1.1]

#m1, h1 = coeficiente(p1,p2)
#m2, h2 = coeficiente(q1,q2)

#print(Intersecao(h1,h2,m1,m2))

#Abrindo videos

cap = cv2.VideoCapture("V1.mp4")
video2 = cv2.VideoCapture("V2.mp4")
video3 = cv2.VideoCapture("V3.mp4")

# Definindo os limites das cores:
# HSV -> Hue Sat Value
lower = np.array([57, 50, 50])
upper = np.array([67, 255, 255])

#Funções

def coeficiente (P1, P2):
	
	ax = P1[0]
	ay = P1[1]

	bx = P2[0]
	by = P2[1]


	deltax = bx - ax
	deltay = by - ay

	m = deltay/deltax

	h = ay - (m * ax)

	return m, h

def Intersecao (h1, h2, m1, m2):

	xi = (h2 - h1)/(m1 - m2)

	yi = m1 * xi + h1

	return xi, yi


if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Convertendo o frame para HSV:
  frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # Fazendo a mascara:
  mask = cv2.inRange(frame_hsv, lower, upper)

  # Sobrepondo a mascara com a imagem original para pegar as cores
  # da imagem original:
  output = cv2.bitwise_and(frame, frame, mask=mask)

  # Convertendo o frame para GRAY:
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Tirando os ruidos da imagem:
  frame_blur = cv2.GaussianBlur(frame_gray,(5,5),0)
    
  # Retirando as bordas do frame:
  edges = cv2.Canny(frame_blur, 25, 75)

  # Bordas com cor:
  edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

  # Mostrando o resultado:
  cv2.imshow("Output", edges)

  # Apertar Q para sair do loop principal:
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# Fechando as janelas e desligando a webcam:
cv2.destroyAllWindows()
cap.release()
























#  if ret == True:

    # Mostrando o resultado:
#    cv2.imshow("Output", frame)

    # Apertar Q para sair do loop principal:
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

# Fechando as janelas e desligando a webcam:
#cv2.destroyAllWindows()
#cap.release()