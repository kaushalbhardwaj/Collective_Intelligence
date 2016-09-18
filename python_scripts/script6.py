import script5

a=script5.Song("Treat you better")
a.sing_song()

try:
    print "In try block"
except Exception:
    print "In exception"
else:
    print "no exception"
    
