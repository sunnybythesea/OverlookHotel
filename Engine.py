class Room(object):
    def __init__(self):
        print "I'm virtual"
        self = None

    def Show(self, blurb):
        print blurb

    
class Lobby(Room):
    
    def __init__(self):
        print "Enter lobby"
        self.nextRoom = 'Kitchen'

    def GetNext(self):
        return self.nextRoom
    
    def Play(self, state):
        if state == 'run':
            self.Show('You find yourself rushing to the Kitchen. You can either a:stop or b:keep running')
        elif state == 'stand':
            self.Show('You stand still, holding you breadth. You can \
                      either a:run or b:be still.')
                
        action = raw_input('>')

        if state == 'run' and action == 'a':
            return ('Die', 'Before you know it, a sharp machete cuts across your throat. And you fall dead.', None)
        elif state == 'run' and action == 'b':
            return ('Continue', 'You just barely escape the blade of the machete.', 'near kitchen door')
        elif state == 'stand' and action == 'a':
            self.nextRoom = 'Kitchen'
            return ('Continue', 'You hear an angry panting behind, and you see a door ahead.', 'near kitchen door')
        else:
            return ('Die', 'Bzzzzzz...', None)
        

class Kitchen(Room):
    
    def __init__(self):
        print 'Enter Kitchen'
        self.nextRoom = 'Lobby'

    def GetNext(self):
        return self.nextRoom

    def Play(self, state):
        if state == 'near kitchen door':
            self.Show('You find yourself rushing into the Kitchen. You can \
                      either a:stop or b:keep running')
                        
        action = raw_input('>')

        if action == 'a':
            return ('Die', 'Before you know it, a sharp machete cuts across your throat. And you fall dead.', None)
        elif action == 'b':
            self.nextRoom = 'Lobby'
            return ('Continue', 'You hear an angry panting behind, and you see a door ahead.', 'run')
        else:
            return ('Die', 'you fall dead.', None)
    
        
    
class Pantry(object):
    def __init__(self):
        print 'Enter Pantry'


class Ballroom(object):
    def __init__(self):
        print 'Enter Ballroom'


class Room217(object):
    def __init__(self):
        print 'Enter room 217'

class Maze(object):
    def __init__(self):
        print 'Enter maze'


''' The engine instantiates all the objects
'''
class Engine(object):
   
    def __init__(self):
        print "New engine"
        room = Lobby()
        state = 'run'
        
        while True:
            (result, blurb, state) = room.Play(state)
            print '-------------------------------------------------'
            print 'Result %r, state %r' %(result, state)
            print '-------------------------------------------------'
            if result == 'Continue':
                room = globals()[room.GetNext()]()
            else:
                print 'You suck at this'
                exit(0)


if __name__ == '__main__':
    print('Sorry I am a module')



