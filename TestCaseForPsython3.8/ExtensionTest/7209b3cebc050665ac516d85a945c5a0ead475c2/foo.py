class A:
    pass


print(A())

'''
output :
<__main__.A object at {addr}>

'''



for i in range(10):
    print(i)

'''
output :
0
1
2
3
4
5
6
7
8
9
'''



class Apple():
    def __init__(self):
        print('hi Apple cls.')
    

print(Apple())

'''
output :
hi A cls.
<__main__.A object at {addr}>
'''



if True:
    print('hi if')
elif False:
    print('hi elif1')
elif False:
    print('hi elif2')
elif False:
    print('hi elif3')
elif False:
    print('hi elif4')
elif False:
    print('hi elif5')
else:
    print('hi else')

'''
output :
hi if
# hi elif1
# hi elif2
# hi elif3
# hi elif4
# hi elif5
# hi else
'''



#add class for each Exception.

try:
    raise Exception
except Exception:
    print('exception occured1')
except Exception as err:
    print('exception occured2')
except Exception:
    print('exception occured3')
finally:
    print('finally')

'''
output :
exception ouccured1
# exception ouccured2
# exception ouccured3
finally
'''



a = 10
while a > 0:
    print('cur a : ', a)
    a -= 1

''' 
output :
cur a :  10
cur a :  9
cur a :  8
cur a :  7
cur a :  6
cur a :  5
cur a :  4
cur a :  3
cur a :  2
cur a :  1
'''



class A():
    def __enter__(self):
        print('A.__enter__')
        return self

    def foo(self,name):
        print('A.foo', name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('A.__exit__')
        

class B():
    def __enter__(self):
        print('B.__enter__')
        return self

    def bar(self,name):
        print('B.bar', name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('B.__exit__')


class C():
    def __enter__(self):
        print('C.__enter__')
        return self

    def baz(self,name):
        print('C.baz', name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('C.__exit__')



with A() as a, B() as b, C() as c:
    a.foo('hi')
    b.bar('hi')
    c.baz('hi')

'''
output :
A.__enter__
B.__enter__
C.__enter__
A.foo hi
B.bar hi
C.baz hi
C.__exit__
B.__exit__
A.__exit__
'''