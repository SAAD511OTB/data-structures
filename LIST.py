list1=['alpha','A',1145,5.6,'Delta']
SAAD=list1.copy()
print(SAAD)
print('\nFirst- : \n',list1[1:4],'how about negative? : ', list1[-1])

LAB= list(['J','J','j'])
print('\bConstructor \b ', LAB)
#------------------
list2=['Woow',5,4,3,1,1,1,1,66]
list2.extend(list1)
del list2[0]
print('\n Second-  :\n',list2,'1 count is : ',list2.count(1))
#------------------
list3=[1,3,4,7,8]
list3.insert(1,2)
list3.append(5)
list3.remove(7)
list3.pop(4)
print('\n third- :\n', list3)
#------------------
list5=[1,2,3,4,5,6,7,8,9,0]
i=0
print('\n4TH')
while i<len(list5):
    print(list5[i])
    i= i+1
list5.reverse() # reverse ex 1
print(list5)
#----------------------

moh=['Y','ar']
ohio=['ou','e',]
list6 = [i + m for i, m in zip(moh, ohio)]
print('\n 5th :\n',list6)
mwmw=zip(moh,ohio)
print('Doctor way ',list(mwmw))
#-----------------------
ultList=[]
for x in list1,list2,list3,list5:
    if 1 in x:
        ultList.append(x)
print(ultList)
#------------------------
listSquare=[1,2,3,4,5]
sal=[]
for o in listSquare:
    sal.append(o*o)
print(sal)
#---------------------












