if True:
    print "In if condition"
    if True:
        print "In nested if"
    else: 
        print "In nested else of if"
elif False:
    print "In else if condition of if"
else:
    print "else of elif"
    
listex=["kaushal",2,3.5]
print listex
for i in listex:
    print i
    
element=[]
    
for i in range(0,6):
    print "count is",i
    element.append(i)
    
print element

i=0
while i<6:
    print i
    i=i+1
    
a="This is a string used to discuss functions of string"
print a[3:7]
print len(a)
print a[2]
print a*2
print cmp(element,[2,3,4])
print len(element)
element[3]=7.5
print element[1:3]
twod=[[2,3,4],["adsf","kaushal"]]
print twod

dic={'a':1,'b':2,'kaushal':"greatest"}
print dic
dic['a']="kaushal"
print dic.values()
print dic.keys()
print len(dic)

dictd={'a':["kaushal",3,54],
       'b':{'a':2,'b':6,'kaushal':"kaus"} }
print dictd['b']['b']
print "Great work"

print "tuple cannot be changed its immutable"
d=(2,4,5,6)
print d
    