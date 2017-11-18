# coding: utf-8
def calcu_tri(x,y):
    print "Now in function"
    return  1.0*x*y/2.0

print "计算中"
a=0
h=0
area=0.0
a=input("a=")
h=input("h=")
area=calcu_tri(a,h)
print "Area is"+`area`