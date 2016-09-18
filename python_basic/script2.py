from sys import argv

#print "input the data"
#a=raw_input()
#print "value of a=%r" %a
#b=raw_input("Name ? ")
#print "your name is %r"%b

#s,f,second,th=argv
#print s,f,second,th
#c,d,e=10,20,30
#print "this type of assignment is possible",c,d,e

f=open("script2_text.txt")
print "the data of text file is ==>>",f.read()
f.close()
f=open("script2_text.txt",'r+')
print "New edited file is==> ",f.read()
f.write("new data")
print ("This operation made cursor to go at last of file so no read occur in last process")
f.close()
