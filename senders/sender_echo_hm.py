import asyncio
import socket
import wave


def send_frame(frame, client_socket):
    client_socket.sendto(frame, ('127.0.0.1', 9999))


def get_udp_response(client_socket):
    client_socket.recv(1024)


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    filename = '/home/ds/PycharmProjects/MediaServer_test_task/audiofile_collection/hello_main.wav'

    with wave.open(filename, 'rb') as file:
        frameCount = file.getnframes()
        print(file.getparams())
        curFrame = 0
        while curFrame < frameCount:
            frame = file.readframes(2)
            send_frame(frame, client_socket)
            get_udp_response(client_socket)
            # event.set()
            curFrame += 2
        client_socket.sendto(b'', ('127.0.0.1', 9999))
    print('finish')

if __name__ == '__main__':
    main()

