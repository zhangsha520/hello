# import time
# def timer(func):
#     def deco(*args, **kwargs):  
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time()
#         print(stop-start)
#     return deco

# @timer
# def test(): #8
#     time.sleep(2)
#     print("test is running!")   
# test()
import time

def timer(parameter):

    def outer_wrapper(func):

        def wrapper(*args, **kwargs):
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task1 run time is :", stop - start)
            elif parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task2 run time is :", stop - start)

        return wrapper

    return outer_wrapper

@timer(parameter='task1')
def task1():
    time.sleep(2)
    print("in the task1")

@timer(parameter='task2')
def task2():
    time.sleep(2)
    print("in the task2")

task1()
task2()