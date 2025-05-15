# -*- coding: utf-8 -*-
import cv2
import numpy as np
from multiprocessing import shared_memory as shm
from shm_tools.shmcom import FrameReceiver,StringReceiver,ListReceiver


FrameReceiver=FrameReceiver(shm_name='shared_frame', frame_shape=(360, 640, 3))
StringReceiver=StringReceiver(shm_name='shared_string', string_length=256)
ListReceiver=ListReceiver(shm_name='shared_list', list_length=256)

try:
    while True:
        # 从共享内存中读取frame
        frame = FrameReceiver.get_frame()
        x=StringReceiver.get_string()
        list=ListReceiver.get_list()
        print(x)
        print(list)
        cv2.namedWindow("Shared Memory Frame", cv2.WINDOW_NORMAL)
        cv2.imshow("Shared Memory Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cv2.destroyAllWindows()
