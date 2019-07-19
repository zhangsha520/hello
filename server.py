# import bisect
# t = [2, 4, 6, 8]
# print(t)
# print(bisect.bisect_left(t, 7))
# print(t)
# print(bisect.bisect_left(t, 4))
# print(t)
import mmap
import gevent
mmap_file = None

def get_mmap_info():
    global mmap_file
    ## 第二个参数1024是设定的内存大小，单位：字节。如果内容较多，可以调大一点
    mmap_file = mmap.mmap(-1, 1024, access = mmap.ACCESS_WRITE, tagname = 'share_mmap')
    print("Load data to memory")
    mmap_file.write(b"This is the test data")
    
if __name__=="__main__":
    while True:
        get_mmap_info()
        gevent.sleep(0.001)