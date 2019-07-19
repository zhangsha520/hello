"""电阻"""


# class Resistor(object):
#     """电阻"""
#     def __init__(self, ohms):
#         self.ohms = ohms
#         self.voltage = 0
#         self.current = 0


# class VolatgeResistance(Resistor):
#     """电压电阻"""
#     def __init__(self, ohms):
#         super().__init__(ohms)
#         self._voltage = 0

#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.setter
#     def voltage(self, voltage):
#         self._voltage = voltage
#         self.current = self._voltage / self.ohms

# r2 = VolatgeResistance(1e3)
# print('before: %5r amps' % r2.current)

# r2.voltage = 10
# print('after: %5r amps' % r2.current)

# class ValidatePolygon(type):
#     def __new__(meta, name, bases, class_dict):
#         if bases != (object,):
#             if class_dict['sides'] < 3:
#                 raise ValueError('Polygons need 3+ sides')
#         return type.__new__(meta, name, bases, class_dict)

# class Polygon(object, metaclass=ValidatePolygon):
#     sides = None

#     @classmethod
#     def interior_angles(cls):
#         return (cls.sides - 2) * 180

# class Triangle(Polygon):
#     sides = 3

# a = Triangle()

# from queue import Queue
# from threading import Thread

# queue = Queue()

# def consumer():
#     print('consumer waiting')
#     queue.get()
#     print('consumer done')

# thread = Thread(target=consumer)
# thread.start()
# print('Producer putting')
# queue.put(object())
# thread.join()
# print('Producer done')

from threading import *


# class Mythread(Thread):
#     def __init__(self, name, *args):
#         super(Mythread, self).__init__(name=name)
#         self.data = args

#     def run(self):
#         print(self.data[0])

# Mythread('abc', range(10)).start()

# from time import sleep


# def test():
#     print("___thread_start___")
#     sleep(10)
#     print("___thread_stop___")


# def run():
#     t = Thread(target=test)
#     t.start()
#     t.join(2)  # 设置超时时间为2s

#     print(t.isAlive())  # 检查线程状态
#     t.join()  # 再次等待

#     print("over")

# run()


# def my_coroutine():
#     while True:
#         received = yield
#         print("received: ", received)

# it = my_coroutine()
# next(it)

# it.send('first')
# it.send('second')


# def minimize():
#     print("in minimize")
#     current = yield
#     while True:
#         print("current = ", current)
#         value = yield current
#         print("current after = ", current, value)
#         current = min(value, current)

# it = minimize()
# next(it)
# # print(it.send(10))
# print(it.send(2))
# print(it.send(5))
# print(it.send(1))

# import os
# import sys

# def split_fully(path):
#     parent_path, name = os.path.split(path)
#     if name == "":
#         return(parent_path, )
#     else:
#         return split_fully(parent_path) + (name, )

# path = sys.path[0] + sys.path[1]
# print(split_fully(path))
# print(split_fully(__file__))

import sys


f = range(10, 20)
print(*f)
print(dir(f))
print(sys.byteorder)
