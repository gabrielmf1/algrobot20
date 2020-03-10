#!/usr/bin/python
#-*- coding:utf-8 -*-


# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math
import Entrega3
import imutils

if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "./V1.mp4"

    src = cv2.VideoCapture(fn)
    dst = imutils.auto_canny(src, 50, 200) # aplica o detector de bordas de Canny à imagem src
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR) # Converte a imagem para BGR para permitir desenho colorido

    if True: # HoughLinesP
        lines = cv2.HoughLinesP(dst, 10, math.pi/180.0, 100, np.array([]), 5, 5)
        print("Used Probabilistic Rough Transform")
        print("The probabilistic hough transform returns the end points of the detected lines")
        a,b,c = lines.shape
        print("Valor de A",a, "valor de lines.shape", lines.shape)
        for i in range(a):
            # Faz uma linha ligando o ponto inicial ao ponto final, com a cor vermelha (BGR)
            cv2.line(cdst, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)

    else:    # HoughLines
        # Esperemos nao cair neste caso
        lines = cv2.HoughLines(dst, 1, math.pi/180.0, 10, np.array([]), 0, 0)
        a,b,c = lines.shape
        for i in range(a):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            m = math.cos(theta)
            h = math.sin(theta)
            x0, y0 = m*rho, h*rho
            pt1 = ( int(x0+1000*(-h)), int(y0+1000*(m)) )
            pt2 = ( int(x0-1000*(-h)), int(y0-1000*(m)) )
            if m <= (-0.55) and m >= (-2.03):
                cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
        print("Used old vanilla Hough transform")
        print("Returned points will be radius and angles")

    cv2.imshow("source", src)
    cv2.imshow("detected lines", cdst)
    cv2.waitKey(0)
