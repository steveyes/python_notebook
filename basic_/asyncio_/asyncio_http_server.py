#!/usr/bin/env python3
#


import asyncio


# 通过async声明一个协程
async def handle_echo(reader, writer):
    # 将需要io的函数使用 await 等待, 那么此函数就会停止
    # 当IO操作完成会唤醒这个协程，await 在旧版中为 yield from
    #
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    writer.write(data)
    print("Send: %r" % message)

    # 刷新底层传输的写缓冲区。也就是把需要发送出去的数据，从缓冲区发送出去。手动刷新。
    await writer.drain()

    print("Close the client socket")
    writer.close()


if __name__ == '__main__':
    # 创建事件循环
    loop = asyncio.get_event_loop()

    # 通过asyncio.start_server方法创建一个协程
    coro = asyncio.start_server(handle_echo, '0.0.0.0', 8888, loop=loop)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print(f'serving on {server.sockets[0].getsockname()}')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
