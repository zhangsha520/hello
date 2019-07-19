# def fn(self, name="world"):
#     print("hello, %s" % name)

# def by(self, name="bye"):
#     print("hello, %s" % name)
# Hello = type("hello", (object,), dict(say_hello=fn, say_bye=by))
# hello = Hello()
# hello.say_hello()
# hello.say_bye()

# class SayMetaClass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs["say_"+name] = lambda self, value, saying=name: print(saying+','+value+'!')
#         return type.__new__(cls, name, bases, attrs)

# class Hello(object, metaclass=SayMetaClass):
#     def hahha(self):
#         print("hhh")
#     pass

# hello = Hello()
# hello.say_Hello("world")

# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)

# class MyList(list, metaclass=ListMetaclass):
#     pass

# L = MyList()

# L.add(1)
# print(L)

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>'% (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100')

class InterField(Field):
    def __init__(self, name):
        super(InterField, self).__init__(name, 'bigint')

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('found mapping: %s ===> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwarg):
        super(Model, self).__init__(**kwarg)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(" 'Model' object has no attribute '%s' " % key)
    
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ",".join(fields), ','.join([str(i) for i in args]))
        print('sql: %s' % sql)
        print('args: %s' % str(args))


class User(Model):
    id = InterField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Batman', email='batman@nasa.org', password='iamback')
u.save()