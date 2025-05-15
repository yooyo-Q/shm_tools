# -*- coding: utf-8 -*-

import cv2
import numpy as np
from shm_tools.shmcom import FrameSender,StringSender,ListSender
import datetime

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头，请检查连接。")
else:
    FrameSender = FrameSender(shm_name='shared_frame', frame_shape=(360, 640, 3))
    StringSender = StringSender(shm_name='shared_string', string_length=256)
    ListSender = ListSender(shm_name='shared_list', list_length=256)
    try:
        while True:
            ret, frame = cap.read()
            if ret:
                # 将frame写入共享内存
                frame = cv2.resize(frame, (640, 360))
                FrameSender.send_frame(frame)
                #发送当前时间
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(current_time)
                StringSender.send_string(current_time)
                # 发送当前帧的列表
                ListSender.send_list([1, 2])
                print([1, 2])
                print("发送列表成功")
                

                cv2.namedWindow("RTSP Stream", cv2.WINDOW_NORMAL)
                cv2.imshow("RTSP Stream", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("无法读取视频帧")
                break
    finally:
        FrameSender.cleanup()
        StringSender.cleanup()
        ListSender.cleanup()
        cap.release()
        cv2.destroyAllWindows()
