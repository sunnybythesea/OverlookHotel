# Rooms
class Room(object):
    def __init__(self):
        print "I'm virtual"
        self = None

    def show(self, blurb):
        print blurb

    
class Lobby(Room):
    
    def __init__(self):
        print "Enter lobby"
        self.next_room = 'Kitchen'

    def get_next(self):
        return self.next_room
    
    def play(self, state):
        if state == 'run':
            self.show('You find yourself rushing to the Kitchen. You can either a:stop or b:keep running')
        elif state == 'stand':
            self.show('You stand still, holding you breadth. You can \
                      either a:run or b:be still.')
                
        action = raw_input('>')

        if state == 'run' and action == 'a':
            return ('Die', 'Before you know it, a sharp machete cuts across your throat. And you fall dead.', None)
        elif state == 'run' and action == 'b':
            return ('Continue', 'You just barely escape the blade of the machete.', 'near kitchen door')
        elif state == 'stand' and action == 'a':
            self.next_room = 'Kitchen'
            return ('Continue', 'You hear an angry panting behind, and you see a door ahead.', 'near kitchen door')
        else:
            return ('Die', 'Bzzzzzz...', None)
        

class Kitchen(Room):
    
    def __init__(self):
        print 'Enter Kitchen'
        self.next_room = 'Lobby'

    def get_next(self):
        return self.next_room

    def play(self, state):
        if state == 'near kitchen door':
            self.show('You find yourself rushing into the Kitchen. You can \
                      either a:stop or b:keep running')
                        
        action = raw_input('>')

        if action == 'a':
            return ('Die', 'Before you know it, a sharp machete cuts across your throat. And you fall dead.', None)
        elif action == 'b':
            self.next_room = 'Lobby'
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
