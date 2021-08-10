import socket
import wave
from time import sleep

if __name__ == '__main__':

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    filename = '/home/ds/PycharmProjects/MediaServer_test_task/audiofile_collection/hello_main.wav'

    with wave.open(filename, 'rb') as file:
        frameCount = file.getnframes()
        bitrate = file.getframerate()
        print(file.getparams())
        curFrame = 0
        frameArray = []
        while curFrame < frameCount:
            frame = file.readframes(1)
            client_socket.sendto(frame, ('127.0.0.1', 9999))
            curFrame += 1
            sleep(1/200000)
        else:
            client_socket.sendto(b'', ('127.0.0.1', 9999))

    print('finish hm')