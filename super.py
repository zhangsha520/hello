class Root(object):
    def __init__(self):
        print("this is root")

class B(Root):
    def __init__(self):
        print("enter b")
        super().__init__()
        print("leave b")

class C(Root):
    def __init__(self):
        print("enter c")
        super().__init__()
        print("leave c")

class D(B, C):
    pass

d = D()
print(d.__class__.__mro__)