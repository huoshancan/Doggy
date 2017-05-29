# -*- coding: utf-8 -*-
from location import *;
import cv2
import glob
import subprocess
import time
import os
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

if __name__ == '__main__':
    while True:
        img=cv2.imread('hc.jpg')
        sp=img.shape
        print sp
        sy=sp[0]/2    #y
        sx=sp[1]/2    #x
        print 'sx/2:%d sy/2:%d '%(sx,sy)
        fileHan=open('zhongxin.txt','r')
        begin=fileHan.read()
        x=int(begin[0:3:])
        y=int(begin[4:7:])
        z=int(begin[8:10:])
        print 'x:%d y:%d'%(x,y)
        dx=x-sx
        dy=y-sy
        print 'dx:%d  dy : %d' %(dx,dy)
        if dx<0:
            ser.write('r')
            print 'r'
        elif dx>0:
            ser.write('l')
            print 'l'
        k = cv2.waitKey(0)
        if k == 27:         # ESC键退出
            cv2.destroyAllWindows()
