from random import *

class Game:
    def __init__(self, play_board):
        self.pb = play_board
        
    def shift(self, left = True):
        new_m = []
        for line in self.pb:
            line=[x for x in line if x != 0]
            for i in range(len(line)-1):
                if line[i] == line[i+1]:
                    line[i] = line[i] * 2
                    line[i+1] = 0
            line=[x for x in line if x != 0]
            for i in range(4 - len(line)):
                if left == True:
                    line.append(0)
                else:
                    line.insert(0,0)
            new_m.append(line)
        self.pb = new_m
        print(self.pb)
        new_m = 0
        return self.pb

    def random_two_or_four(self,calc):
        kon = 1
        for x in range(4):
            if kon != 0:
                for y in range(4):
                    if self.pb[x][y] == 0:
                        kon = 0
        while True:
            if kon == calc:
                break
            chislo=choices([2, 4], weights=[90, 10])
            x=randrange(0,4)
            y=randrange(0,4)
            if self.pb[x][y] == 0:
                self.pb[x][y] = chislo[0]
                kon += 1
            else:
                continue
        return self.pb

    def new_game(self):
    	self.pb = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    	return self.pb
        
    def move_left(self):
        temp_pb = self.pb
        self.pb = Game.shift(self)
        for i in range(4):
            if temp_pb[i] != self.pb[i]:
                self.pb = Game.random_two_or_four(self, 1)
                break
        return self.pb

    def move_right(self):
        temp_pb = self.pb
        self.pb = Game.shift(self, left = False)
        for i in range(4):
            if temp_pb[i] != self.pb[i]:
                self.pb = Game.random_two_or_four(self, 1)
                break
        return self.pb

    def move_up(self):
        temp_pb = self.pb
        self.pb = list(zip(*self.pb))
        self.pb = Game.shift(self, left = False)
        self.pb = [list(i) for i in zip(*self.pb)]
        for i in range(4):
            if temp_pb[i] != self.pb[i]:
                self.pb = Game.random_two_or_four(self, 1)
                break
        return self.pb
             
    def move_down(self):
        temp_pb = self.pb
        self.pb = list(zip(*self.pb))
        self.pb = Game.shift(self)
        self.pb = [list(i) for i in zip(*self.pb)]
        for i in range(4):
            if temp_pb[i] != self.pb[i]:
                self.pb = Game.random_two_or_four(self, 1)
                break
        return self.pb
