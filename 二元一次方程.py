import math
a=eval(input("请输入a的值："))
b=eval(input("请输入b的值："))
c=eval(input("请输入c的值："))
d=b*b-4*a*c

if d>=0:
   x1=(-b+math.sqrt(d))/2*a
   x2=(-b-math.sqrt(d))/2*a
   print("一元二次方程的解为x1={:.2f},x2={:.2f}".format(x1,x2))
else:
   print("此方程无解")
