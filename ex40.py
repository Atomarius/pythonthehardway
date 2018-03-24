import mystuff

mystuff.apple()
print mystuff.tangerine


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right here"])

bulls_on_parade = Song(["They rally round tha family", "With pockets full of shells"])

happy_bday.sing()
bulls_on_parade.sing()
