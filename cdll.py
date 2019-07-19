from ctypes import *
libc = cdll.msvcrt
# print(windll.kernel32)
# print(windll.msvcrt)
# print(windll.kernel32.GetModuleHandleA)
# p = create_string_buffer(3)
# print(sizeof(p), repr(p.raw))
printf = libc.printf
printf.argtypes=[c_char_p, c_char_p, c_int, c_double]

# 字符串前加上b，表示bytes的意思，就是原始字节的意思
# 不加的是编码过的字符串
# 😄
printf(b"String %s, Int %d, Double %f\n", b"Hi", 10, 2.2)