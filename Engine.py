# Engine class
''' The engine instantiates all the objects
'''

''' Basic room. This is mostly a virtual class.

'''
class Room(object):
    def __init__(self):
        print "New room"
        
    def GetNext(self):
        print 'Virtual'

    def Play(self):
        print 'Virtual'
        #return ('Nothing', '...', 'No state')

    #def GetRoom(self):
    #    return self.__class__
    def Show(self, blurb):
        print '\n--- %r\n ---' %(blurb)
        
class Lobby(Room):
    def __init__(self):
        print "Enter lobby"

    def Play(self):
        self.Show('You find yourself in the lobby')
        raw_input('>')
        return ('Win', 'You won', None)
   
class Engine(object):
   
    def __init__(self):
        print "New engine"
        room = Lobby()

        (result, blurb, state) = room.Play()

        print '-------------------------------------------------'
        print 'Result %r, state %r' %(result, state)
        print '-------------------------------------------------'








