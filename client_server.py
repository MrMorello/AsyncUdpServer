import socket
import wave
from select import select

connections = {}


def event_loop():
    while True:
        try:
            ready_to_read, _, _ = select(to_monitoring, [], [])  # read write error

            for sock in ready_to_read:
                if sock is server_socket:
                    accept_data(sock)
        except ValueError as e:
            print('all connections closed')
            server_socket.close()
            return


def sock_address_to_str(addr):
    return f'{addr[0]}_{str(addr[1])}'


def accept_data(sock):
    data, addr = server_socket.recvfrom(1024)
    if sock_address_to_str(addr) not in connections:
        create_file(data, addr)
        filename = connections.get(sock_address_to_str(addr))
        # with wave.open(filename, 'wb') as wavFile:
        if data:
            filename.writeframes(data)
        else:
            filename.close()
    else:
        filename = connections.get(sock_address_to_str(addr))
        # with wave.open(filename, 'wb') as wavFile:
        if data:
            filename.writeframes(data)
        else:
            filename.close()
    # if not data:
    #     wavFile.close()
    #     server_socket.close()
    # else:
    #     print(f"received message: {addr}, {data}")
    #     wavFile.writeframes(data)


def create_file(data, addr):
    filename = f'{sock_address_to_str(addr)}.wav'
    key = f'{addr[0]}_{str(addr[1])}'

    wav_file = wave.open(filename, 'wb')
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(8000)
    wav_file.writeframes(data)

    item = {key: wav_file}
    connections.update(item)
    # wavFile.close()


if __name__ == '__main__':
    to_monitoring = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    to_monitoring.append(server_socket)
    server_socket.bind(('127.0.0.1', 5005))

    # ep = 0
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


# class VawFile:
#     def __init__(self, ip_port, :
