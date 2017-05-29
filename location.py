#coding=utf-8
import cv2
import cv2.cv as cv
def location(pic):
        img=pic
        #转换为灰度图
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #直方图均衡处理
        gray = cv2.equalizeHist(gray)
        #脸部特征分类地址，里面还有其他
        cascade_fn = '/Users/huoshan/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt.xml'
        #读取分类器,CascadeClassifier下面有一个detectMultiScale方法来得到矩形
        cascade = cv2.CascadeClassifier(cascade_fn) 
        #通过分类器得到rects
        '''
        detectMultiScale函数中smallImg表示的是要检测的输入图像为smallImg，
        faces表示检测到的人脸目标序列，1.3表示每次图像尺寸减小的比例为1.3，
        4表示每一个目标至少要被检测到3次才算是真的目标
        (因为周围的像素和不同的窗口大小都可以检测到人脸),
        CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像
        Size(20, 20)为目标的最小最大尺寸
        '''
        rects = cascade.detectMultiScale(img, scaleFactor=1.3,
                                        minNeighbors=5, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
        if len(rects) == 0:
            return []
        print rects
        rects[:,2:] += rects[:,:2]
        print rects
      
     
    #在img上绘制矩形
        def draw_rects(img, rects, color):
            for x1, y1, x2, y2 in rects:
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            
    #vis为img副本
    #以下文件操作部分可以删除，功能只是要读取上一次的人脸位置重心

        vis = img.copy()
        txt = str(rects)
        fileHandle = open ( 'weizhi.txt', 'w' )
        fileHandle.write(txt)
        fileHandle.close()

        fileHandle = open ( 'weizhi.txt', 'r' )
        begin = fileHandle.read()
        fileHandle.close()

        x =int(begin[2:5:]) 
        y =int(begin[6:9:])
        z =int(begin[10:13:])/2
        x = x + z 
        y = y + z 
        print("x=",x,"y=",y,"z=",z)
        f = open('zhongxin.txt','w')
        f.write(str(x)+" "+str(y)+" "+str(z))
        f.close()

        #画矩形
        draw_rects(vis, rects, (0, 255, 0))
         
        cv2.imshow('facedetect', vis)
         
        cv2.waitKey(0)
        cv2.destroyAllWindows()
