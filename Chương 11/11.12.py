a=(3,1,2,4)
print("Tuple a: ",a)
b=(5,7,6,8)
print("Tuple b: ",b)
x=list(a+b)
c=tuple(x)
print("Tuple c: ",c)
x.sort()
d=tuple(x)
print("Tuple d: ",d)
print("Tuple[3]=",d[3])
print("3 phần tử cuối cùng của tuple d :",d[-3:])