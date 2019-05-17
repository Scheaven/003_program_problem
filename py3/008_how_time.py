G = input().split(" ")
x,f,d,p = map(int,G)
y = (d+f*p)//(x+p)
if y - f >=0:
	print(y)
else:
	print(d//x)