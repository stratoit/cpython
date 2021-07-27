#add class for each Exception.

try
{
raise Exception
}
except Exception
{
print('exception occured1')
}
except Exception as err
{
print('exception occured2')
}
except Exception
{
print('exception occured3')
}
finally
{
print('finally')
}

'''
output :
exception ouccured1
# exception ouccured2
# exception ouccured3
finally
'''