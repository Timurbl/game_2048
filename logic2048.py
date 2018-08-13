from random import choice

class Game():
    def __init__(self, N=4):
        self.field = [[''] * N for i in range(N)]
        self.N = N
        self.add_tile()
        self.add_tile()
  
    def __getitem__(self, index):
        return self.field[index]
    
    def __str__(self):
        return '\n'.join(':'.join(map(str, self[i])) for i in range(self.N))
  
    def left(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N):
                if not self[i][j]: 
                    free += 1
                else:
                    if free > 0:
                        self[i][j - free] = self[i][j]
                        self[i][j] = ''
                        j -= free
                        change = True
                    if j > 0 and self[i][j] == self[i][j - 1]:
                        self[i][j - 1] *= 2
                        self[i][j] = ''
                        change = True                
        if change:          
            self.add_tile()
    
    def right(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N - 1, -1, -1):
                if not self[i][j]: 
                    free += 1
                else:
                    if free > 0:
                        self[i][j + free] = self[i][j]
                        self[i][j] = ''
                        j += free
                        change = True
                    if j < self.N - 1 and self[i][j] == self[i][j + 1]:
                        self[i][j + 1] *= 2
                        self[i][j] = ''
                        change = True                
        if change:          
            self.add_tile()    

    def up(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N):
                if not self[j][i]: 
                    free += 1
                else:
                    if free > 0:
                        self[j - free][i] = self[j][i]
                        self[j][i] = ''
                        j -= free
                        change = True
                    if j > 0 and self[j][i] == self[j - 1][i]:
                        self[j - 1][i] *= 2
                        self[j][i] = ''
                        change = True                
        if change:          
            self.add_tile()    
        
    def down(self):
        change = False
        for i in range(self.N):        
            free = 0
            for j in range(self.N - 1, -1, -1):
                if not self[j][i]: 
                    free += 1
                else:
                    if free > 0:
                        self[j + free][i] = self[j][i]
                        self[j][i] = ''
                        j += free
                        change = True
                    if j < self.N - 1 and self[j][i] == self[j + 1][i]:
                        self[j + 1][i] *= 2
                        self[j][i] = ''
                        change = True                
        if change:          
            self.add_tile()            
    
    def add_tile(self):
        free = [(i, j) for i in range(self.N) 
                for j in range(self.N) if not self[i][j]]
        i, j = choice(free)
        self[i][j] = 2
          
    def game_over(self):
        for line in self.field:
            if '' in line:
                return False
        
        for i in range(self.N):
            for j in range(self.N - 1):
                if self[i][j] == self[i][j + 1]: return False
                if self[j][i] == self[j + 1][i]: return False
        
        return True