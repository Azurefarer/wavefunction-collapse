import numpy as np

class scene:

    def __init__(self, tiles, contraints):

        self.tiles = tiles              #size of scene
        self.contraints = contraints    #if =0, 1, 2, ..., n have set initial conditions for scene

        self.set_tiles = 0

        self.scene = np.zeros([tiles, tiles])

    def collapse(self):
        n = self.tiles
        i, j = np.random.randint(n), np.random.randint(n)
        self.scene[i][j] = np.random.randint(1, 10)
        self.set_tiles += 1
        while self.set_tiles <= n**2:
            if i == n:
                i = -1
            i += 1

            if self.scene[i][j] == 0:
                #call function for adjecent cells

                #collapse current cell(include self.set_tiles += 1)
                pass    
            else:
                j += 1
                if j > n:
                    j = 0


