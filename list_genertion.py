#!/usr/bin/env python3
# encoding:utf-8
 
#一般生成一个list，可以这样做
print('A---------------------list(range(m,n))')
L = list(range(1,11))
print(L)
 
#生成x*x的，我们可以加个for循环实现
print('B---------------------for x in range(m,n)')
L = []
for x in range(1,11):
    L.append(x*x)
print(L)
 
#生成x*x的list，我们可以这样做
print('C---------------------[x*x for x in range(m,n)]')
L = [x*x for x in range(1,11)]
print(L)
 
#生成x*x的list，我们只要能够被3整除的部分
print('D---------------------[x*x for x in range(m,n) if 条件]')
L = [x*x for x in range(1,11) if x%3 == 0]
print(L)
 
 
#通过两个变量，利用列表生成式生成一个结构为[x=y]的list，我们可以用字符串进行拼接得到
print("E---------------------[x+'='+y for x,y in D.items()]")
D = {"Name":"appleyk",'age':26,'sex':'F'}#这里注意：age的value值是一个int类型
L = [x+'='+y for x,y in D.items() if not isinstance(y,int)] # 同时访问 dict的key和value，并将key和value组合成新的list元素
#上面我们加了条件限制，也就是只要value是int类型的，我们不组合，因为x+'='+y只针对字符串加可以，如果y是int，+号就会成为定时炸弹
print(L)
 
#转化list元素为小写
print("F---------------------[s.lower() for s in L]")
L = [s.lower() for s in ['Hello', 'World', 18, 'Apple',None] if (s is not None and not isinstance(s,int))]
#注意，这里我们也加了条件限制，因为int类型和None没有lower属性，且None只能用is来判断，它没有具体的类型！
print(L)
 
 
'''
全排列集合：
[x+y+z+.... for x in.. for y in .. for z in .. .....]
一般使用两层就够了，超过三层以上，就有点太庞大了，自己验证
'''
print('G---------------------x+y+z+... for x in .. for y in .. for z in .. ......')
L = [m+n for m in "ABC" for n in "abc"]
print(L)
 
 
print("H--------输出指定目录下的所有文件：")
 
import os  #  output stream 输出流
 
L = [dir for dir in os.listdir('D:\\')]#listdir函数接收FilePath路径，并返回一个list对象，元素是文件名
print(L)
 
