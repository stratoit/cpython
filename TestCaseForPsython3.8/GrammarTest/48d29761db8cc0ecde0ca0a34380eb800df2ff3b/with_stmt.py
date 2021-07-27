class A()
{
def __enter__(self)
{
print('A.__enter__')
return self
}
def foo(self,name)
{
print('A.foo', name)
}
def __exit__(self, exc_type, exc_val, exc_tb)
{
print('A.__exit__')
}
}

class B()
{
def __enter__(self)
{
print('B.__enter__')
return self
}
def bar(self,name)
{
print('B.bar', name)
}
def __exit__(self, exc_type, exc_val, exc_tb)
{
print('B.__exit__')
}
}

class C()
{
def __enter__(self)
{
print('C.__enter__')
return self
}
def baz(self,name)
{
print('C.baz', name)
}
def __exit__(self, exc_type, exc_val, exc_tb)
{
print('C.__exit__')
}
}

with A() as a, B() as b, C() as c
{
a.foo('hi')
b.bar('hi')
c.baz('hi')
}


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