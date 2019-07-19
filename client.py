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


## 从内存中读取信息，
def read_mmap_info():    
    global mmap_file
    mmap_file.seek(0)
    ## 把二进制转换为字符串
    info_str = mmap_file.read().translate(None, b'\x00').decode()
    print("in read_mmap_info")
    print(info_str)
## 如果内存中没有对应信息，则向内存中写信息以供下次调用使用
def get_mmap_info():
    global mmap_file
    ## 第二个参数1024是设定的内存大小，单位：字节。如果内容较多，可以调大一点
    mmap_file = mmap.mmap(-1, 1024, access = mmap.ACCESS_READ, tagname = 'share_mmap')
    ##读取有效比特数，不包括空比特
    while True:
        read_mmap_info()
        gevent.sleep(0.001)

if __name__=="__main__":
    get_mmap_info()