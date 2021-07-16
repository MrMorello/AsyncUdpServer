import socket
import wave
from time import sleep

import os

if __name__ == '__main__':

    # message = b'Hello Russian'
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    filename = 'audiofile_collection/confirmation_main_3.wav'

    with wave.open(filename, 'rb') as file:
        frameCount = file.getnframes()
        bitrate = file.getframerate()
        print(file.getparams())
        curFrame = 0
        frameArray = []
        while curFrame < frameCount:
            frame = file.readframes(1)
            client_socket.sendto(frame, ('127.0.0.1', 5005))
            curFrame += 1

        else:
            client_socket.sendto(b'', ('127.0.0.1', 5005))

    print('finish 3')

