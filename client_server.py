import socket
import wave
from select import select


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitoring, [], [])  # read write error

        for sock in ready_to_read:
            if sock is server_socket:
                accept_data(sock, ep )


def accept_data(sock, ep):
    data, addr = server_socket.recvfrom(1024)
    if not data:
        wavFile.close()
        server_socket.close()
    ep += 1
    print(f"received message: {ep}, {data}")
    wavFile.writeframes(data)


if __name__ == '__main__':
    to_monitoring = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    to_monitoring.append(server_socket)
    server_socket.bind(('127.0.0.1', 5005))
    newFile = 'new_file.wav'
    wavFile = wave.open(newFile, 'wb')
    wavFile.setnchannels(1)
    wavFile.setsampwidth(2)
    wavFile.setframerate(8000)
    ep = 0
    event_loop()
    # while True:
    #     data, addr = server_socket.recvfrom(1024)
    #     if not data:
    #         wavFile.close()
    #         server_socket.close()
    #         break
    #     ep += 1
    #     print(f"received message: {ep}, {data}")
    #     wavFile.writeframes(data)


