import asyncio
import queue
import wave

connections = {}


def sock_address_to_str(addr):
    return f'{addr[0]}_{str(addr[1])}'


def create_file(data, addr):
    filename = f'saved_audio_files/{sock_address_to_str(addr)}.wav'
    key = f'{addr[0]}_{str(addr[1])}'

    wav_file = wave.open(filename, 'wb')
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(8000)
    wav_file.writeframes(data)

    item = {key: wav_file}
    connections.update(item)


class EchoServerProtocol:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        key = sock_address_to_str(addr)
        if data:
            if key not in connections:
                item = {key: queue.Queue()}
                item[key].put(data)
                connections.update(item)
                self.transport.sendto(b'1', addr)
            else:
                connections[key].put(data)
                self.transport.sendto(b'1', addr)
        else:
            filename = f'saved_wav_files/{key}.wav'
            queue_obj = connections.get(key)
            wav_file = wave.open(filename, 'wb')
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(8000)

            while not queue_obj.empty():
                queue_elem = queue_obj.get()
                wav_file.writeframes(queue_elem)

            print(f'file for {key} ready')
            wav_file.close()
            self.transport.sendto(b'1', addr)


async def main():
    print("Starting UDP server")

    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    # One protocol instance will be created to serve all
    # client requests.
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr=('127.0.0.1', 9999))

    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()


if __name__ == '__main__':
    asyncio.run(main())
