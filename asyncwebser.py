import asyncio
import socket

async def handle_client(client_reader,client_writer):
    data = await client_reader.read(1024)
    message = data.decode()
    addr = client_writer.get_extra_info('peername')
    print(f"Received {message!r} from {addr!r}")
    client_writer.close()

async def main():
    server = await asyncio.start_server(handle_client,'127.0.0.1',8888)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())