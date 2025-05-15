# MIT License
# 
# Copyright (c) 2025 kexin—Young
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -*- coding: utf-8 -*-
import cv2
import numpy as np
from multiprocessing import shared_memory, resource_tracker
import os

#发送opencv视频帧和字符串到共享内存
class FrameSender:
    def __init__(self, shm_name='shared_frame', frame_shape=(360, 640, 3)):
        self.shm_name = shm_name
        self.frame_shape = frame_shape
        self.shm = shared_memory.SharedMemory(create=True, size=np.prod(frame_shape) * np.dtype(np.uint8).itemsize, name=shm_name)
        self.frame_buffer = np.ndarray(frame_shape, dtype=np.uint8, buffer=self.shm.buf)
        os.chmod(f'/dev/shm/{shm_name}', 0o777)

    def send_frame(self,frame):
        if frame is not None:
            frame = cv2.resize(frame, (self.frame_shape[1], self.frame_shape[0]))
            np.copyto(self.frame_buffer, frame)
        else:
            print("无法读取视频帧")
    def cleanup(self):
        self.shm.close()
        self.shm.unlink()

#接收opencv视频帧和字符串从共享内存 
class FrameReceiver:
    def __init__(self, shm_name='shared_frame', frame_shape=(360, 640, 3)):
        self.shm_name = shm_name
        self.frame_shape = frame_shape
        self.shm = shared_memory.SharedMemory(name=shm_name)
        resource_tracker.unregister(self.shm._name, 'shared_memory')
        self.frame_buffer = np.ndarray(frame_shape, dtype=np.uint8, buffer=self.shm.buf)

    def get_frame(self):
        return np.copy(self.frame_buffer)

#接收字符串从共享内存
class StringSender:
    def __init__(self, shm_name='shared_string', string_length=256):
        self.shm_name = shm_name
        self.string_length = string_length
        self.shm = shared_memory.SharedMemory(create=True, size=string_length, name=shm_name)
        os.chmod(f'/dev/shm/{shm_name}', 0o777)

    def send_string(self, string):
        if string is not None:
            encoded_string = string.encode('utf-8')
            if len(encoded_string) > self.string_length:
                raise ValueError("字符串长度超过共享内存限制")
            # 将字符串写入共享内存
            self.shm.buf[:len(encoded_string)] = encoded_string
            # 填充剩余部分为 0
            self.shm.buf[len(encoded_string):self.string_length] = b'\x00' * (self.string_length - len(encoded_string))
        else:
            print("无法读取字符串")

    def cleanup(self):
        self.shm.close()
        self.shm.unlink()
#发送字符串到共享内存
class StringReceiver:
    def __init__(self, shm_name='shared_string', string_length=256):
        self.shm_name = shm_name
        self.string_length = string_length
        self.shm = shared_memory.SharedMemory(name=shm_name)
        resource_tracker.unregister(self.shm._name, 'shared_memory')

    def get_string(self):
        # 从共享内存中读取字符串
        encoded_string = bytes(self.shm.buf[:self.string_length]).decode('utf-8').rstrip('\x00')
        return encoded_string
    def cleanup(self):
        self.shm.close()
        self.shm.unlink()
#发送列表到共享内存
class ListSender:
    def __init__(self, shm_name='shared_list', list_length=256):
        self.shm_name = shm_name
        self.list_length = list_length
        self.shm = shared_memory.SharedMemory(create=True, size=list_length, name=shm_name)
        os.chmod(f'/dev/shm/{shm_name}', 0o777)

    def send_list(self, lst):
        if lst is not None:
            encoded_list = str(lst).encode('utf-8')
            if len(encoded_list) > self.list_length:
                raise ValueError("列表长度超过共享内存限制")
            # 将列表写入共享内存
            self.shm.buf[:len(encoded_list)] = encoded_list
            # 填充剩余部分为 0
            self.shm.buf[len(encoded_list):self.list_length] = b'\x00' * (self.list_length - len(encoded_list))
        else:
            print("无法读取列表")

    def cleanup(self):
        self.shm.close()
        self.shm.unlink()
        
class ListReceiver:
    def __init__(self, shm_name='shared_list', list_length=256):
        self.shm_name = shm_name
        self.list_length = list_length
        self.shm = shared_memory.SharedMemory(name=shm_name)
        resource_tracker.unregister(self.shm._name, 'shared_memory')

    def get_list(self):
        # 从共享内存中读取列表
        encoded_list = bytes(self.shm.buf[:self.list_length]).decode('utf-8').rstrip('\x00')
        return eval(encoded_list)
    def cleanup(self):
        self.shm.close()
        self.shm.unlink()

# Example usage
if __name__ == "__main__":
    # Example usage of FrameSender and FrameReceiver
    sender = FrameSender()
    receiver = FrameReceiver()

    # Example usage of StringSender and StringReceiver
    string_sender = StringSender()
    string_receiver = StringReceiver()

    # Example usage of ListSender and ListReceiver
    list_sender = ListSender()
    list_receiver = ListReceiver()

    # Clean up resources
    sender.cleanup()
    receiver.cleanup()
    string_sender.cleanup()
    string_receiver.cleanup()
    list_sender.cleanup()
    list_receiver.cleanup()

import cv2
import numpy as np
from multiprocessing import shared_memory, resource_tracker
import os

#发送opencv视频帧和字符串到共享内存
class FrameSender:
    def __init__(self, shm_name='shared_frame', frame_shape=(360, 640, 3)):
        self.shm_name = shm_name
        self.frame_shape = frame_shape
        self.shm = shared_memory.SharedMemory(create=True, size=np.prod(frame_shape) * np.dtype(np.uint8).itemsize, name=shm_name)
        self.frame_buffer = np.ndarray(frame_shape, dtype=np.uint8, buffer=self.shm.buf)
        os.chmod(f'/dev/shm/{shm_name}', 0o777)

    def send_frame(self,frame):
        if frame is not None:
            frame = cv2.resize(frame, (self.frame_shape[1], self.frame_shape[0]))
            np.copyto(self.frame_buffer, frame)
        else:
            print("无法读取视频帧")
    def cleanup(self):
        self.shm.close()
        self.shm.unlink()

#接收opencv视频帧和字符串从共享内存 
class FrameReceiver:
    def __init__(self, shm_name='shared_frame', frame_shape=(360, 640, 3)):
        self.shm_name = shm_name
        self.frame_shape = frame_shape
        self.shm = shared_memory.SharedMemory(name=shm_name)
        resource_tracker.unregister(self.shm._name, 'shared_memory')
        self.frame_buffer = np.ndarray(frame_shape, dtype=np.uint8, buffer=self.shm.buf)

    def get_frame(self):
        return np.copy(self.frame_buffer)

#接收字符串从共享内存
class StringSender:
    def __init__(self, shm_name='shared_string', string_length=256):
        self.shm_name = shm_name
        self.string_length = string_length
        self.shm = shared_memory.SharedMemory(create=True, size=string_length, name=shm_name)
        os.chmod(f'/dev/shm/{shm_name}', 0o777)

    def send_string(self, string):
        if string is not None:
            encoded_string = string.encode('utf-8')
            if len(encoded_string) > self.string_length:
                raise ValueError("字符串长度超过共享内存限制")
            # 将字符串写入共享内存
            self.shm.buf[:len(encoded_string)] = encoded_string
            # 填充剩余部分为 0
            self.shm.buf[len(encoded_string):self.string_length] = b'\x00' * (self.string_length - len(encoded_string))
        else:
            print("无法读取字符串")

    def cleanup(self):
        self.shm.close()
        self.shm.unlink()
#发送字符串到共享内存
class StringReceiver:
    def __init__(self, shm_name='shared_string', string_length=256):
        self.shm_name = shm_name
        self.string_length = string_length
        self.shm = shared_memory.SharedMemory(name=shm_name)
        resource_tracker.unregister(self.shm._name, 'shared_memory')

    def get_string(self):
        # 从共享内存中读取字符串
        encoded_string = bytes(self.shm.buf[:self.string_length]).decode('utf-8').rstrip('\x00')
        return encoded_string
    def cleanup(self):
        self.shm.close()
        self.shm.unlink()
#发送列表到共享内存
class ListSender:
    def __init__(self, shm_name='shared_list', list_length=256):
        self.shm_name = shm_name
        self.list_length = list_length
        self.shm = shared_memory.SharedMemory(create=True, size=list_length, name=shm_name)
        os.chmod(f'/dev/shm/{shm_name}', 0o777)

    def send_list(self, lst):
        if lst is not None:
            encoded_list = str(lst).encode('utf-8')
            if len(encoded_list) > self.list_length:
                raise ValueError("列表长度超过共享内存限制")
            # 将列表写入共享内存
            self.shm.buf[:len(encoded_list)] = encoded_list
            # 填充剩余部分为 0
            self.shm.buf[len(encoded_list):self.list_length] = b'\x00' * (self.list_length - len(encoded_list))
        else:
            print("无法读取列表")

    def cleanup(self):
        self.shm.close()
        self.shm.unlink()
        
class ListReceiver:
    def __init__(self, shm_name='shared_list', list_length=256):
        self.shm_name = shm_name
        self.list_length = list_length
        self.shm = shared_memory.SharedMemory(name=shm_name)
        resource_tracker.unregister(self.shm._name, 'shared_memory')

    def get_list(self):
        # 从共享内存中读取列表
        encoded_list = bytes(self.shm.buf[:self.list_length]).decode('utf-8').rstrip('\x00')
        return eval(encoded_list)
    def cleanup(self):
        self.shm.close()
        self.shm.unlink()

# Example usage
if __name__ == "__main__":
    # Example usage of FrameSender and FrameReceiver
    sender = FrameSender()
    receiver = FrameReceiver()

    # Example usage of StringSender and StringReceiver
    string_sender = StringSender()
    string_receiver = StringReceiver()

    # Example usage of ListSender and ListReceiver
    list_sender = ListSender()
    list_receiver = ListReceiver()

    # Clean up resources
    sender.cleanup()
    receiver.cleanup()
    string_sender.cleanup()
    string_receiver.cleanup()
    list_sender.cleanup()
    list_receiver.cleanup()
