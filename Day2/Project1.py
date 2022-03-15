a=5
print(type(a))

a=5.5
print(type(a))

a=True
print(type(a))

a="True"
print(type(a))

a='True'
print(type(a))

a=5+4j
print(type(a))

#List
a=[5,6,7]
print(type(a))

#Tuple
a=(5,6,7)
print(type(a))

#Set
a={5,6,7}
print(type(a))

#List with mixed datatype values
a=[5,6.5,True,"Abc",5+4j]
print(a)

a=[56,78,99,24]
print(a)
#print(id(a))
a.append(4)
print(a)
print(id(a))
print(len(a))


