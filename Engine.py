from Rooms import *

''' The engine instantiates all the objects
'''
class Engine(object):
   
    def __init__(self):
        print "New engine"
        room = Lobby()
        state = 'run'
        
        while True:
            (result, blurb, state) = room.play(state)
            print '-------------------------------------------------'
            print 'Result %r, state %r' %(result, state)
            print '-------------------------------------------------'
            if result == 'Continue':
                room = globals()[room.get_next()]()
            else:
                print 'You suck at this'
                exit(0)


if __name__ == '__main__':
    print('Sorry I am a module')



