
class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    
    def sing_song(self):
        print self.lyrics
        
        
class Song2(Song):
    __privateData=10
        
obj=Song("We dont talk anymore")
obj.sing_song()
print obj.lyrics


obj2=Song2("New Song ")
obj2.sing_song()
