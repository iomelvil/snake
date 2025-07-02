class Snake:
    def __init__(self,initial_position):
        self.body = [initial_position] # list of (x,y) tuples
        self.direction = (0,1) # start moving up

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def check_collision(self):
        pass

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)

        self.body.pop()



