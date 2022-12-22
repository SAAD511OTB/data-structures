from array import *

array6=array('i',[1,2,3,4,6])
for i in array6:
    print(i)
#---------------------------------------
array5=array('d',[1,2,3,4,6])
array5.reverse()
for i in array5:
    print(i)

#---------------------------------------
array4=array('i',[1,2,3,4,6])
print(array4.buffer_info() * array4.itemsize)

#---------------------------------------
array3=array('i',[1,2,3,3,4,6])
print(array3.count(3))

#---------------------------------------
array2=array('i',[1,3,5,7,9])
array2.extend(array2)
print(array2)
#---------------------------------------
array1=array('i',[1,3,5,7,9])
array1.extend(array1)
for i in array1:
    print(i)
#---------------------------------------

x=array('i',[1,2,3,4,5,6,7,8,111,123,123,22])
s=x.tobytes()
print(s)


#-------------------------------
x2=array('b',[83,65,65,68])
s2=x.tobytes()
print(s)
#--------------------------------------

List=[1,2,3,4,5,6,7,8,9]
M=array('i',[])
M.fromlist(List)
for i in M:
    print(i)
print(M)

#-------------------------
Meo=array('i',[1,3,6,5])
Meo.insert(1,4)
for i in Meo:
    print(i)

#-------------------------
Meow=array('i',[1,3,6,5,3,3])
Meow.remove(5)
for i in Meow:
    print(i)

#---------------------------------

from array import *
Meo=array('i',[1,3,6,5,3,3])
Meo.remove(3)
for i in Meo:
    print(i)
