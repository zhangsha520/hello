# from functools import wraps

# can_run = True


# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         print(args)
#         print(kwargs)
#         print(111)
#         if not can_run:
#             return("function will not run")
#         return f(*args, **kwargs)
#     return decorated



# @decorator_name
# def func(a, b, c):
#     return("function is running")


# can_run = True
# print(func(a=5, b=6, c=7))
# print(func.__name__)


# can_run = False
# print(func())


# def tracer(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print('%s(%r,%r)->%r'%(func.__name__,args,kwargs,result))
#         return result
#     return wrapper

# @tracer
# def fibonacci(n):
#     if n in (0,1):
#         return n
#     return (fibonacci(n-1)+fibonacci(n-2))


# fibonacci(3)
# print(fibonacci)
# print('help:')
# help(fibonacci)


def hi(name="yas"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yas":
        return greet
    else:
        return welcome


a = hi("as")
print(a())