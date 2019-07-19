# import functools

# def add(a, b):
#     print(a + b)
#     return a + b

# addplus3 = functools.partial(add, 3)
# result = addplus3(7)

# from functools import wraps

# def sum_add( *args1):
#     def decorator(func):
#         @wraps(func)
#         def my_sum(*args2):
#             print("in my_sum ===")
#             my_s = 0
#             for n in args1:
#                 my_s = my_s + n
#             return func(*args2)+my_s
#         return my_sum
#     return decorator

# @sum_add(10, 20)
# def sum(*args):
#     print("in sum ===")
#     s = 0
#     for n in args:
#         s = s + n
#     return s

# print(sum(1, 2, 3, 4, 5))
# print(sum.__name__)

# from functools import partial

# def sum(*args):
#     s = 0
#     for n in args:
#         s = s + n
#     return s

# sum_add_10 = partial(sum, 10)
# sum_add_10_20 = partial(sum, 10, 20)

# print(sum)
# print(partial(sum, 10))

# from functools import partial

# l = list(range(1, 11))

# slice_5_10 = partial(slice, 5, 10)
# print(l[slice_5_10()])

import functools

def mod(m, *, key=2):
    print("=== ", m, key)
    return m % key == 0

mod_to_2 = functools.partial(mod, key=2)
print(mod_to_2(3))