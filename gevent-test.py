# import gevent
# def foo():
#     """ FOO """
#     print('running in foo')
#     gevent.sleep(0)  # 让当前的greenlet睡眠n秒，这0标识控制其他协程而不会让其他协程睡眠
#     print('explict context switch too foo again')

# def bar():
#     """" BAR """
#     print('explict context to bar')
#     gevent.sleep(0)
#     print('implict context switch back to bar')

# gevent.joinall([gevent.spawn(foo),gevent.spawn(bar)])

# import gevent
# import time
# from gevent import select

# start = time.time()
# tic = lambda: 'at %1.1f seconds' % (time.time() - start)

# def gr1():
#     print("start polling: ", tic)

# def gr2():
#     print("started polling: ", tic)
#     select.select([], [], [], 2)
#     print("started polling: ", tic)

# def gr3():
#     print("hey lets do some stuff while the greenlets poll, at", tic())
#     gevent.sleep(1)

# import gevent

# import gevent
# import random

# def task(pid):
#     gevent.sleep(random.randint(0, 2) * 0.001)
#     print('Task', pid, 'done')

# def synchronous():
#     # 同步
#     for i in range(1, 10):
#         task(i)

# def asynchronous():
#     # 异步
#     threads = [gevent.spawn(task, i) for i in range(10)]
#     gevent.joinall(threads)

# print("synchronous:")
# synchronous()

# print("asychronous:")
# asynchronous()

# import gevent
# from gevent import Greenlet

# def foo(message, n):
#     gevent.sleep(n)
#     print(message)

# thread1 = Greenlet.spawn(foo, 'hello', 1)
# thread2 = gevent.spawn(foo, 'i live', 2)
# thread3 = gevent.spawn(lambda x: (x+1), 2)

# threads = [thread1, thread2, thread3]
# gevent.joinall(threads)

# import gevent
# def win():
#     return 'you win!'

# def fail():
#     raise Exception('you fail at failing.')

# winner = gevent.spawn(win)
# loser = gevent.spawn(fail)

# print(winner.started)
# print(loser.started)

# try:
#     gevent.joinall([winner, loser])
# except Exception as e:
#     print('this will never be reached')

# print(winner.value)
# print(loser.value)

# print(winner.ready())
# print(loser.ready())

# print(winner.successful())
# print(loser.successful())
# print(loser.exception)

# import gevent
# from gevent import Timeout

# seconds = 10

# timeout = Timeout(seconds)

# timeout.start()

# print('finish', time.time())
# def wait():
#     gevent.sleep(9)
#     print('sleep 5', time.time())

# try:
#     gevent.spawn(wait).join()
# except Timeout:
#     print(' could not complete')

# import gevent
# from gevent import Timeout

# time_to_wait = 5
# class TooLong(Exception):
#     pass

# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(10)

# import gevent
# from gevent import Timeout

# def wait():
#     gevent.sleep(2)

# timer = Timeout(1).start()
# thread1 = gevent.spawn(wait)

# try:
#     thread1.join(timeout=timer)
# except Timeout:
#     print('thread 1 time out')

# timer = Timeout.start_new(1)
# thread2 = gevent.spawn(wait)

# try:
#     thread2.get(timeout=timer)
# except Timeout:
#     print('Thread 2 timed out')

# try:
#     gevent.with_timeout(1, wait)
# except Timeout:
#     print("thread 3 timed out")

# import gevent
# from gevent.event import AsyncResult
# a = AsyncResult()

# def setter():
#     gevent.sleep(3)
#     a.set("helloe")

# def waiter():
#     print(a.get())

# gevent.joinall([gevent.spawn(setter), gevent.spawn(waiter)])

# import gevent
# from gevent.queue import Queue

# tasks = Queue()

# def worker(n):
#     while not tasks.empty():
#         task = tasks.get()
#         print('worker %s got task %s' %(n, task))
#         gevent.sleep(0)
#     print('quitting time!')

# def boss():
#     for i in range(1, 25):
#         tasks.put_nowait(i)

# gevent.spawn(boss).join()
# gevent.joinall([
#     gevent.spawn(worker, 'steve'),
#     gevent.spawn(worker, 'john'),
#     gevent.spawn(worker, 'nancy')
# ])

# import gevent
# from gevent.queue import Queue, Empty

# tasks = Queue(maxsize=3)

# def worker(n):
#     try:
#         while True:
#             task = tasks.get(timeout=1)
#             print("worker %s got task %s" % (n, task))
#             gevent.sleep(0)
#     except Empty:
#         print('quiting time')

# def boss():
#     for i in range(1, 10):
#         tasks.put(i)
#     print('assigned all work in iteration 1')

#     for i in range(10, 20):
#         tasks.put(i)
#     print("assigned all work in iteration 2")

# gevent.joinall([
#     gevent.spawn(boss),
#     gevent.spawn(worker, 'steve'),
#     gevent.spawn(worker, 'john'),
#     gevent.spawn(worker, 'bob')
# ])

# import gevent
# from gevent import getcurrent
# from gevent.pool import Group
# group = Group()

# def hello_form(n):
#     print('size of group', len(group))
#     print('hello from Greentlet %s' % id(getcurrent()))

# group.map(hello_form, range(3))

# def intensive(n):
#     gevent.sleep(3-n)
#     return 'task', n

# print('ordered')

# ogroup = Group()
# for i in ogroup.imap(intensive, range(3)):
#     print(i)

# print('Unordered')

# igroup = Group()
# for i in igroup.imap_unordered(intensive, range(3)):
#     print(i)

# import gevent
# import socket

# print(socket.socket)
# print("after monkey patch")
# from gevent import monkey
# monkey.patch_socket()
# print(socket.socket)

# import select
# print(select.select)
# monkey.patch_select()
# print('after monkey patch')
# print(select.select)

# from gevent.pool import Pool
# class SocketPool(object):
#     def __init__(self):
#         self.pool = Pool(1000)
#         self.pool.start()
    
#     def listen(self, socket):
#         while True:
#             socket.recv()
    
#     def add_handler(self, socket):
#         if self.pool.full():
#             raise Exception('at maximum pool size')
#         else:
#             self.pool.spawn(self.listen, socket)

#     def shutdown(self):
#         self.pool.kill()

# from gevent import sleep
# from gevent.pool import Pool
# from gevent.lock import BoundedSemaphore

# sem = BoundedSemaphore(2)

# def worker1(n):
#     sem.acquire()
#     print('worker1 %i acquired semaphore' % n)
#     sleep(0)
#     sem.release()
#     print("worker1 %i released semphore" % n)

# def worker2(n):
#     with sem:
#         print('worker2 %i acquired semphore' % n)
#         sleep(1)
#     print('worker2 %i released semphore' % n)

# pool = Pool()
# pool.map(worker1, range(0, 2))
# pool.map(worker2, range(3, 6))


# coding=utf8

# import errno
# import socket
# import select
# import greenlet as rawgreenlet
# from greenlet import greenlet


# class Sock(object):
#     def __init__(self, socket_=None):
#         if socket_ is None:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         else:
#             sock = socket_
#         sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         sock.setblocking(0)
#         self.sock = sock

#     def listen(self, backlog):
#         self.sock.listen(backlog)

#     def bind(self, host, port):
#         self.sock.bind((host, port))

#     def accept(self):
#         while True:
#             try:
#                 print("accept")
#                 client_sock, address = self.sock.accept()
#                 break
#             except socket.error as e:
#                 print(e)
#                 if e.args[0] != errno.EAGAIN:
#                     raise
#             switch = rawgreenlet.getcurrent().switch
#             ioloop.wait(self.sock, switch, ioloop.READ)

#         return Sock(client_sock), address

#     def recv(self, *args):
#         while True:
#             try:
#                 print("recv")
#                 return self.sock.recv(*args)
#             except socket.error as e:
#                 print(e)
#                 if e.args[0] != errno.EAGAIN:
#                     raise
#             switch = rawgreenlet.getcurrent().switch
#             ioloop.wait(self.sock, switch, ioloop.READ)


# def spawn(f):
#     g = greenlet(f, parent=ioloop)
#     ioloop.add_callback(g.switch)
#     return g


# class IOLoop(greenlet):
#     """"main greenlet"""
#     READ = select.EPOLLIN
#     WRITE = select.EPOLLOUT
#     ERROR = select.EPOLLERR | select.EPOLLHUP

#     def __init__(self):
#         self.poller = select.epoll()
#         self.handler = {}
#         self.callbacks = []

#     def wait(self, sock, callback, event):
#         """wait until waiter avaliable"""
#         self.add_handler(sock, callback, event)
#         self.switch()

#     def add_handler(self, sock, callback, event):
#         """
#         fd: file description
#         callback: when event avaliable, invoke callback
#         evnet: poll evnet
#         """
#         fd = sock.fileno()
#         if fd in self.handler:
#             self.poller.unregister(fd)
#         self.poller.register(fd, event)
#         self.handler[fd] = callback

#     def add_callback(self, callback):
#         self.callbacks.append(callback)

#     def start(self):
#         self.switch()

#     def run(self):
#         print("ioloop run")
#         while True:
#             # invoke callback
#             while self.callbacks:
#                 callback = self.callbacks.pop()
#                 callback()

#             # poller
#             events = self.poller.poll(1)
#             print("poller:", events)
#             for fd, event in events:
#                 if event & self.READ:
#                     handler = self.handler[fd]
#                     handler()

# ioloop = IOLoop()


# def f():
#     sock = Sock()
#     sock.bind("localhost", 8088)
#     sock.listen(5)
#     client_sock, address = sock.accept()
#     print("connection from:", address)
#     while 1:
#         print(client_sock.recv(10))

#     # return this greenlet will dead

# spawn(f)
# ioloop.start()

# import gevent
# from gevent.subprocess import Popen, PIPE

# def cron():
#     while True:
#         print('cron')
#         gevent.sleep(0.2)

# g = gevent.spawn(cron)
# sub = Popen(['sleep1; uname'], stdout= PIPE, shell=True)
# out, err = sub.communicate()
# g.kill()
# print(out.rstrip())

# import gevent
# from multiprocessing import Process, Pipe
# from gevent.socket import wait_read, wait_write

# a, b = Pipe()
# c, d = Pipe()

# def relay():
#     for i in range(10):
#         msg = b.recv()
#         c.send(msg + 'in' + str(i))

# def put_msg():
#     for i in range(10):
#         wait_write(a.fileno())
#         a.send('hi')

# def get_msg():
#     for i in range(10):
#         wait_read(d.fileno())
#         print(d.recv())

# if __name__ == '__main__':
#     proc = Process(target=relay)
#     proc.start()

#     g1 = gevent.spawn(get_msg)
#     g2 = gevent.spawn(put_msg)
#     gevent.joinall([g1, g2], timeout=1)

# import time
# import asyncio
 
# now = lambda : time.time()
 
# async def do_some_work(x):
#     print('Waiting: ', x)
 
# start = now()
 
# coroutine = do_some_work(2)
 
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
 
# print('TIME: ', now() - start)