# Globals for the directions
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)

class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x,y)
        self.direction = direction
    
    def move(self, instructions):
        for instr in instructions:
            if instr == "A":
                self.coordinates = tuple(sum(item) for item in zip(self.coordinates,self.direction))
            elif instr =="L":
                self.direction = (-self.direction[1],self.direction[0])
            elif instr =="R":
                self.direction = (self.direction[1],-self.direction[0])


