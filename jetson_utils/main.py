import sys, os
import cv2

from jetson_utils.csicam_single import run_csicam
from jetson_utils.dual_camera import run_cameras
        
def run_camera(opt, client):
    H, W = opt.height, opt.width
    i=0
    if opt.video_path:
        cap = cv2.VideoCapture(opt.video_path)
    elif opt.usb:
        cap = cv2.VideoCapture(2)

    while True:
        ret, frame = cap.read()
        i +=1
        if i % 50 == 0:
            frame = cv2.resize(frame, (int(W/4), int(H/4)))
            client.send(frame)
            #cv2.imshow('camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
 
def jetson_main(opt, client, hyp=None, plot=None):
    if opt.usb:
    	run_camera(opt, client)
    elif opt.csi:
        run_csicam(hyp, client=client, plot=plot)
    elif opt.dual:
        run_cameras(opt)


